from .models import Title, Author, Genre

from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from django.db.models import Sum, Avg
from django.db.models import Count

from os import path
from PIL import Image
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud, STOPWORDS
#from wordcloudgen.wordcloud import *
import io
import urllib, base64

import networkx as nx
import json

from functools import wraps
import time

def timer(func):
    """helper function to estimate view execution time"""

    @wraps(func)  # used for copying func metadata
    def wrapper(*args, **kwargs):
        # record start time
        start = time.time()

        # func execution
        result = func(*args, **kwargs)
        
        duration = (time.time() - start) * 1000
        # output execution time to console
        print('view {} takes {:.2f} ms'.format(
            func.__name__, 
            duration
            ))
        return result
    return wrapper


# Create your views here.

#index
@timer
def index(request):
  #Determine The order of presentation of books
  if not request.GET.get('order_by'):
      order_by = 'year'
  else:
      order_by = request.GET.get('order_by')
  
  print(order_by)
  
  #get the books
  #all_books = Title.objects.order_by(order_by)
  all_books = Title.objects.order_by(order_by).prefetch_related('authors', 'publisher' ).all
  

  authors_count = Author.objects.count()
  genres_count = Genre.objects.count()
  
  
  context = {
    'order_by': order_by,
    'all_books': all_books,
    'authors_count': authors_count,
    'genres_count': genres_count,
    }
  
  return render(request, 'books/books_index.html', context)

#book_detail
@timer
def book_detail(request, book_id):
    try:
        book = Title.objects.get(pk=book_id)
    except Title.DoesNotExist:
        raise Http404("Book does not exist")
    return render(request, 'books/book_detail.html', {'book': book,})

#authors
@timer
def authors(request):
  authors = Author.objects.prefetch_related('title_set').all
  #authors = Author.objects.order_by('last_name')
  return render(request, 'books/authors_index.html', {'authors': authors})

#author_detail
def author_detail(request, author_id):
    try:
        author = Author.objects.get(pk=author_id)
    except Author.DoesNotExist:
        raise Http404("Author does not exist")
    return render(request, 'books/author_detail.html', {'author': author})
  
#genres
@timer
def genres(request):
  genres = Genre.objects.prefetch_related('title_set', 'title_set__authors', 'title_set__publisher').all
  
  #genres = Genre.objects.order_by('name')
  titles = Title.objects.all()
  #topics_graph = books_graph(genres, titles)
  
  genres_count = Genre.objects.values("name_en").annotate(count=Count("title"))
  
  frequency_dict = {r['name_en'] : r['count'] for r in genres_count}
  
  books_wc = books_wordcloud(frequency_dict)
  return render(request, 'books/genres_index.html', {'genres': genres,
                                                     #'topics_graph': topics_graph,
                                                     'books_wordcloud': books_wc,
                                                     })

def d3graph(request):
    #initialize a variable to hold the graph
  G = nx.Graph()
  
  #Add book topics as nodes in the graph
  genres_with_titles_counts = Genre.objects.annotate(Count('title'))

  for genre in genres_with_titles_counts:
    G.add_node(genre.name, size=genre.title__count)
  
  #Add book titles as nodes
  titles = Title.objects.all() #to make the edges
  for title in titles:
    G.add_node(title.id)
    #Add edges for the topics the title is related to
    for genre in title.genres.all():
      G.add_edge(genre.name, title.id)
    
    #Clear the title node and concatate its edges
    neighbors = list(nx.neighbors(G, title.id)) #finding the neighbors of each title
    G.remove_node(title.id) #Remove the title node and its edges
    
    for neighbor in neighbors:
      remaining_ns = neighbors
      if remaining_ns: #make sure the node has neighbors
        for remaining_n in remaining_ns: #a loop to add edges
          if remaining_n != neighbor: #check that the neighbor is different than the starting node
            if G.has_edge(neighbor, remaining_n): #Check if the edge is already exsisting, add to its weight, else add edge
              G[neighbor][remaining_n]['weight'] += 1
            else:
              G.add_edge(neighbor, remaining_n, weight=1)
  data1 = nx.readwrite.json_graph.node_link_data(G)
  print(data1)
  s1 = json.dumps(data1) 
  authors = 'nafez'
  return render(request, 'books/d3graph.html', {'authors': authors,
                                                's1': s1,})

def json_data_sender(request): #helper function for d3graph to send data as json
    #initialize a variable to hold the graph
  G = nx.Graph()
  
  #Add book topics as nodes in the graph
  genres = Genre.objects.all() #representing the nodes
  for genre in genres:
    G.add_node(genre.name)
  
  #Add book titles as nodes
  titles = Title.objects.all() #to make the edges
  for title in titles:
    G.add_node(title.id)
    #Add edges for the topics the title is related to
    for genre in title.genres.all():
      G.add_edge(genre.name, title.id)
    
    #Clear the title node and concatate its edges
    neighbors = list(nx.neighbors(G, title.id)) #finding the neighbors of each title
    G.remove_node(title.id) #Remove the title node and its edges
    
    for neighbor in neighbors:
      remaining_ns = neighbors
      if remaining_ns: #make sure the node has neighbors
        for remaining_n in remaining_ns: #a loop to add edges
          if remaining_n != neighbor: #check that the neighbor is different than the starting node
            if G.has_edge(neighbor, remaining_n): #Check if the edge is already exsisting, add to its weight, else add edge
              G[neighbor][remaining_n]['weight'] += 1
            else:
              G.add_edge(neighbor, remaining_n, weight=1)
  data1 = nx.readwrite.json_graph.node_link_data(G)
  s1 = json.dumps(data1) 
  return JsonResponse(list(s1), safe=False)

def books_graph(genres, titles):
  #a function that returns a png image of the graph of movie genres
  G = nx.Graph()
  
  #genres = Genre.objects.all() #representing the nodes
  for genre in genres:
    G.add_node(genre)
    
  #titles = Title.objects.all() #to make the edges
  for title in titles:
    G.add_node(title.id)
    for genre in title.genres.all():
      G.add_edge(genre, title.id)
    neighbors = list(nx.neighbors(G, title.id))
    #print(neighbors)
    G.remove_node(title.id)
    for neighbor in neighbors:
      #remaining_ns = neighbors.remove(neighbor)
      remaining_ns = neighbors
      print(remaining_ns)
      if remaining_ns:
        for remaining_n in remaining_ns:
          if remaining_n != neighbor:
            if G.has_edge(neighbor, remaining_n):
              G[neighbor][remaining_n]['weight'] += 1
            else:
              G.add_edge(neighbor, remaining_n, weight=1)
              
  pos = nx.spring_layout(G)
  __location__ = os.path.realpath(
                    os.path.join(os.getcwd(), os.path.dirname(__file__)))
  font_path = path.join(__location__, "AvenirArabic_Regular.otf")
  
  options = {
    'font_path': font_path,
    'pos': pos,
    'node_color': 'lightgreen', 
    'node_size': 100,
    'with_labels': True,
    'linewidths': 0,
    'width': 0.1,
    }
  
  nx.draw(G, **options)
  
  ''' To create custom labls uncomment the following section:
  edge_labels = nx.get_edge_attributes(G,'weight')
  custom_node_attrs = {}
  for node, attr in edge_labels.items():
    custom_node_attrs[node] = attr
  '''
  
  for edge in G.edges(data='weight'):
    nx.draw_networkx_edges(G, pos, edgelist=[edge], width=edge[2]/5)
    #connectionstyle'arc3, rad=0.2'
  #to draw custom labels uncomment the following line:
  #nx.draw_networkx_edge_labels(G, pos, edge_labels = custom_node_attrs)

  fig = plt.gcf()
  buf = io.BytesIO()
  fig.savefig(buf, format='png')
  buf.seek(0)
  string = base64.b64encode(buf.read())
  plt.close() 
  image_uri = 'data:image/png;base64,' + urllib.parse.quote(string)
  return image_uri

from django.contrib.staticfiles import finders
@timer
def books_wordcloud(frequency_dict):
    '''
    text = ""
    #genres = Genre.objects.order_by('genre_name')
    for genre in genres:
      books_count = Title.objects.filter(genres=genre).count()
      i = 0
      while i < int(books_count):
        text += str(genre)
        text += " "
        i += 1
    
    processed_text = text.lower().split()
    text_dict = {}
    for item in processed_text:
        text_dict[item] = item.count(item)
    '''
    
    #Getting the font file
    #__location__ = os.path.realpath(
                  #os.path.join(os.getcwd(), os.path.dirname(__file__)))
    #font_path = path.join(__location__, "AvenirArabic_Regular.otf")
    font_path = finders.find('oudwithrad/DubaiWebFont/webfonts/DubaiW23-Bold.ttf')
    #font_path = static('oudwithrad/DubaiWebFont/webfonts/DubaiW23-Regular.ttf')
    print(font_path)
    #Creating a circular mask
    x, y = np.ogrid[:300, :300]
    mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
    mask = 255 * mask.astype(int)
    
    wc = WordCloud(scale=10, max_words=100, mask=mask, font_path=font_path, colormap="tab20", background_color="#fff", repeat=False).generate_from_frequencies(frequency_dict)
    plt.figure(figsize=(4,4))
    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
            hspace = 0, wspace = 0)
    plt.axis("off")
    plt.margins(0,0)
    plt.imshow(wc, interpolation="bilinear", aspect='auto')
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    plt.close() 
    #figure.close()
    image_uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    return image_uri
  
'''
  how to tsend json file from django to d3.js:
  ============================================
  
  1) create a view
  ================
  def Json_data_sender(request):
    data = 
    return JsonResponse(list(data), safe=False)
  
  2) add the view to urlconf:
  ===========================
  url(r'^api/json_data_sender', json_data_sender, name='json_data_sender'),

  3) in the template:
  ================
  d3.json("{% url "play_count_by_month" %}", function(error, data) {
  data.forEach(function(d) {
    d.month = parseDate(d.month);
    d.count_items = +d.count_items;
  });
  
  A Second approach:
  ==================
  in the views:
  import json
  formattedData=json.dumps([dict(item) in list(data)]) 
  #This is a two-fer. It converts each item in the Queryset to a dictionary and then formats it using the json from import json above
  #now we can pass formattedData via the render request
  return render(request, 'graph/graph.html',{'formattedData':formattedData})

  in the template:
  var data= {{formattedData|safe}}
'''

#import unicode
import collections
from django.core.paginator import InvalidPage, EmptyPage

class NamePaginator(object):
    """Pagination for string-based objects"""
    
    def __init__(self, object_list, on=None, per_page=25):
        self.object_list = object_list
        self.count = len(object_list)
        self.pages = []
        
        # chunk up the objects so we don't need to iterate over the whole list for each letter
        chunks = {}
        
        for obj in self.object_list:
            if on: 
              obj_str = str(getattr(obj, on))
              print(getattr(obj, on))
            else: obj_str = str(obj)
            
            letter = obj_str[0].upper()
            
            if letter not in chunks: chunks[letter] = []
            
            chunks[letter].append(obj)
        
        # the process for assigning objects to each page
        current_page = NamePage(self)
        
        chunks = collections.OrderedDict(sorted(chunks.items()))
        for letter, value in chunks.items():
            if letter not in chunks: 
                current_page.add([], letter)
                continue
            
            sub_list = chunks[letter] # the items in object_list starting with this letter
            
            new_page_count = len(sub_list) + current_page.count
            # first, check to see if sub_list will fit or it needs to go onto a new page.
            # if assigning this list will cause the page to overflow...
            # and an underflow is closer to per_page than an overflow...
            # and the page isn't empty (which means len(sub_list) > per_page)...
            if new_page_count > per_page and \
                    abs(per_page - current_page.count) < abs(per_page - new_page_count) and \
                    current_page.count > 0:
                # make a new page
                self.pages.append(current_page)
                current_page = NamePage(self)
            
            current_page.add(sub_list, letter)
        
        # if we finished the for loop with a page that isn't empty, add it
        if current_page.count > 0: self.pages.append(current_page)
        
    def page(self, num):
        """Returns a Page object for the given 1-based page number."""
        if len(self.pages) == 0:
            return None
        elif num > 0 and num <= len(self.pages):
            return self.pages[num-1]
        else:
            raise InvalidPage
    
    @property
    def num_pages(self):
        """Returns the total number of pages"""
        return len(self.pages)

class NamePage(object):
    def __init__(self, paginator):
        self.paginator = paginator
        self.object_list = []
        self.letters = []
    
    @property
    def count(self):
        return len(self.object_list)
    
    @property
    def start_letter(self):
        if len(self.letters) > 0: 
            self.letters.sort(key=str.upper)
            return self.letters[0]
        else: return None
    
    @property
    def end_letter(self):
        if len(self.letters) > 0: 
            self.letters.sort(key=str.upper)
            return self.letters[-1]
        else: return None
    
    @property
    def number(self):
        return self.paginator.pages.index(self) + 1
    
    def add(self, new_list, letter=None):
        if len(new_list) > 0: self.object_list = self.object_list + new_list
        if letter: self.letters.append(letter)
    
    def __str__(self):
        if self.start_letter == self.end_letter:
            return self.start_letter
        else:
            return '%c-%c' % (self.start_letter, self.end_letter)
          
def authors_paginated_list(request):
  authors_list = Author.objects.all()
  paginator = NamePaginator(authors_list, on="last_name", per_page=25)

  try:
    page = int(request.GET.get('page', '1'))
  except ValueError:
    page = 1

  try:
    page = paginator.page(page)
  except (InvalidPage):
    page = paginator.page(paginator.num_pages)

  return render(request, 'books/authors_paginated_list.html', {"page": page})
