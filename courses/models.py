from django.db import models
from django.utils.translation import get_language
from django.utils.translation import ugettext_lazy as _
from cms.models.fields import PlaceholderField

# Create your models here.
class Catagory(models.Model):
  name_en = models.CharField(verbose_name=_('Name en'), max_length=200)
  name_ar = models.CharField(verbose_name=_('Name ar'), max_length=200)
  
  class Meta:
    verbose_name = _('Catagory')
    verbose_name_plural = _('Catagories')
  
  def __str__(self):
    if get_language() == 'ar':
      return self.name_ar
    else:
      return self.name_en
      
class Course(models.Model):
  catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, verbose_name=_('Catagory'), )
  name_en = models.CharField(verbose_name=_('Name en'), max_length=200)
  name_ar = models.CharField(verbose_name=_('Name ar'), max_length=200)
  
  class Meta:
    verbose_name = _('Course')
    verbose_name_plural = _('Courses')
  
  def __str__(self):
    if get_language() == 'ar':
      return self.catagory.name_ar + ' - ' + self.name_ar
    else:
      return self.catagory.name_en + ' - ' + self.name_en

def lesson_placeholder_slotname(instance):
    return 'lesson_placeholder'

class Lesson(models.Model):
  course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_('Course'), )
  name_en = models.CharField(verbose_name=_('Name en'), max_length=200)
  name_ar = models.CharField(verbose_name=_('Name ar'), max_length=200)
  video_link = models.URLField(verbose_name=_('Video Link'), max_length = 200)
  lesson_placeholder = PlaceholderField('lesson_placeholder')
  lesson_order = models.IntegerField(verbose_name=_('Lesson Order'), blank=True, null=True,)
  class Meta:
    verbose_name = _('Lesson')
    verbose_name_plural = _('Lessons')
  
  def __str__(self):
    if get_language() == 'ar':
      return self.course.catagory.name_ar + ' - ' + self.course.name_ar + ' - ' + self.name_ar
    else:
      return self.course.catagory.name_en + ' - ' + self.course.name_en + ' - ' + self.name_en


class Question(models.Model):
  lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
  question_text_en = models.CharField(verbose_name=_('Question Text en'), max_length=200)
  question_text_ar = models.CharField(verbose_name=_('Question Text ar'), max_length=200)
  
  class Meta:
    verbose_name = _('Question')
    verbose_name_plural = _('Questions')
  
  def __str__(self):
    if get_language() == 'ar':
      return self.question_text_ar
    else:
      return self.question_text_en
    
class Answer(models.Model):
  answer_text_en = models.CharField(verbose_name=_('Answer Text en'), max_length=200)
  answer_text_ar = models.CharField(verbose_name=_('Answer Text ar'), max_length=200)
  question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name=_('Question'), )
  is_correct = models.BooleanField(verbose_name=_('Is Correct?'))
  
  class Meta:
    verbose_name = _('Answer')
    verbose_name_plural = _('Answers')
  
  def __str__(self):
    if get_language() == 'ar':
      return self.answer_text_ar
    else:
      return self.answer_text_en
