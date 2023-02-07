from django.urls import path

from . import views

app_name = 'courses'
urlpatterns = [
    path('', views.index, name='index'),
    path('course/<int:course_id>/', views.course, name='course'),
    path('lesson/<int:lesson_id>/', views.lesson, name='lesson'),
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
