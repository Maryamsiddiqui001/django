from django.urls import path

from . import views

app_name = 'gallery'
urlpatterns = [
    path('', views.index, name='index'),
    path('maker/<int:maker_id>/', views.maker, name='maker'),
    path('oud/<int:oud_id>/', views.oud, name='oud'),
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
