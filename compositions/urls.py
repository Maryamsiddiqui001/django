from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('score/<int:score_id>/', views.score, name='score'),
    path('i18n/', include('django.conf.urls.i18n')),
    
]
