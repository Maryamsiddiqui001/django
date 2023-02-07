from django.urls import path, include

from . import views

app_name = 'manuscripts'

urlpatterns = [
    path('', views.index, name='index'),
    path('manuscript/<int:manuscript_id>/', views.manuscript, name='manuscript'),
    
]
