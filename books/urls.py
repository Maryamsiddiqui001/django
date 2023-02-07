from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.index, name='index'),
    path('plain/', views.index, name='index1'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    
    path('authors/', views.authors, name='authors_index'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('authors/paginated_list', views.authors_paginated_list, name='authors_paginated_list'),
    
    path('genres/', views.genres, name='genres_index'),
    path('d3graph/', views.d3graph, name='d3graph'),
    path('d3graph/json_data_sender', views.json_data_sender, name='json_data_sender'),
]

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
