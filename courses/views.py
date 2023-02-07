from django.shortcuts import render
from . models import Catagory, Course, Lesson
from django.db.models import Prefetch
# Create your views here.

def index(request):
  catagories = Catagory.objects.all().prefetch_related('course_set')
  context = {'catagories': catagories,}
  return render(request, 'courses/index.html', context)

def course(request, course_id):
  
  course = Course.objects.filter(pk=course_id).prefetch_related(Prefetch('lesson_set', queryset=Lesson.objects.order_by('lesson_order'))).all()
  
  context = {'course': course,}
  return render(request, 'courses/course.html', context)

def lesson(request, lesson_id):
           
  lesson = Lesson.objects.filter(pk=lesson_id).prefetch_related(Prefetch('question_set')).all()
  context = {'lesson': lesson,}
  return render(request, 'courses/lesson.html', context)
