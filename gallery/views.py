from django.shortcuts import render
from . models import Maker, Oud, OudImage
from django.db.models import Prefetch
# Create your views here.

def index(request):
  makers = Maker.objects.all().prefetch_related('oud_set')
  featured_images = OudImage.objects.filter(is_featured=True)
  context = {'makers': makers,
             'featured_images': featured_images,}
  return render(request, 'gallery/index.html', context)

def maker(request, maker_id):
  maker = Maker.objects.get(pk=maker_id)
  #ouds = Oud.objects.prefetch_related('OudImage_set')
  #ouds.filter(maker=maker_id)
  ouds = Oud.objects.filter(maker=maker_id).prefetch_related(Prefetch('oudimage_set')).all()
  context = {'maker': maker,
             'ouds' : ouds,}
  return render(request, 'gallery/maker.html', context)

def oud(request, oud_id):
  ouds = Oud.objects.filter(pk=oud_id).prefetch_related(Prefetch('OudImage_set')).all()
  context = {'ouds': ouds,}
  return render(request, 'gallery/oud.html', context)

#def lesson(request, lesson_id):
           
  #lesson = Lesson.objects.filter(pk=lesson_id).prefetch_related(Prefetch('question_set')).all()
  #context = {'lesson': lesson,}
  #return render(request, 'courses/lesson.html', context)
