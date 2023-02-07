from django.shortcuts import render
from . models import Author, Title, Manuscript, Folio
# Create your views here.
def index(request):
  titles = Title.objects.all()
  titles_count = Title.objects.count()
  manuscripts_count = Manuscript.objects.count()
  folio_count = Folio.objects.count()
  context = {'titles': titles,
             'titles_count': titles_count,
             'manuscripts_count': manuscripts_count,
             'folio_count': folio_count,
             }
  return render(request, 'manuscripts/index.html', context)

def manuscript(request, manuscript_id):
  manuscript = Manuscript.objects.get(pk=manuscript_id)
  print(manuscript)
  context = {'manuscript':manuscript,}
  return render(request, 'manuscripts/manuscript_detail.html', context)
