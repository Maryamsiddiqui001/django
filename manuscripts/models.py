from django.db import models
from django.utils.translation import get_language
from django.utils.translation import ugettext_lazy as _
from cms.models.fields import PlaceholderField
#from cms.models import Page as cmsPage

# Create your models here.

class Author(models.Model):
  monthes = [(1, "January"),(2, "Febraury"),(3, "March"),(4, "April"),(5, "May"),(6, "June"),(7, "July"),(8, "August"),(9, "September"),(10, "October"),(11, "November"),(12, "December"),]
  
  days = [(1, "1"),(2, "2"),(3, "3"),(4, "4"),(5, "5"),(6, "6"),(7, "7"),(8, "8"),(9, "9"),(10, "10"),(11, "11"),(12, "12"),(13, "13"),(14, "14"),(15, "15"),(16, "16"),(17, "17"),(18, "18"),(19, "19"),(20, "20"),(21, "21"),(22, "22"),(23, "23"),(24, "24"),(25, "25"),(26, "26"),(27, "27"),(28, "28"),(29, "29"),(30, "30"),(31, "31"),]
  
  first_name_ar = models.CharField(max_length=150, blank=True)
  middle_name_ar = models.CharField(max_length=150, blank=True)
  last_name_ar = models.CharField(max_length=150)
  
  first_name_en = models.CharField(max_length=150, blank=True)
  middle_name_en = models.CharField(max_length=150, blank=True)
  last_name_en = models.CharField(max_length=150)
  
  arabic_definite_article = models.BooleanField(default=False, blank=True, null=True,)
  
  
  birth_city_ar = models.CharField(verbose_name=_('Birth City AR'), max_length=50, blank=True)
  birth_locality_ar = models.CharField(verbose_name=_('Birth Locality AR'), max_length=50, blank=True)
  birth_country_ar = models.CharField(verbose_name=_('Birth Country AR'), max_length=50, blank=True)
  
  birth_city_en = models.CharField(verbose_name=_('Birth City EN'), max_length=50, blank=True)
  birth_locality_en = models.CharField(verbose_name=_('Birth Locality EN'), max_length=50, blank=True)
  birth_country_en = models.CharField(verbose_name=_('Birth Country EN'), max_length=50, blank=True)
  
  birth_year_CE = models.SmallIntegerField(verbose_name=_('Birth Year CE'), blank=True, null=True)
  birth_month_CE = models.SmallIntegerField(verbose_name=_('Birth Month CE'), choices=monthes, blank=True, null=True)
  birth_day_CE = models.SmallIntegerField(verbose_name=_('Birth Day CE'), choices=days,blank=True, null=True)
  
  birth_year_AH = models.SmallIntegerField(verbose_name=_('Birth Year AH'), blank=True, null=True)
  birth_month_AH = models.SmallIntegerField(verbose_name=_('Birth Month AH'), choices=monthes, blank=True, null=True)
  birth_day_AH = models.SmallIntegerField(verbose_name=_('Birth Day AH'), choices=days,blank=True, null=True)
  
  death_year_CE = models.SmallIntegerField(verbose_name=_('Death Year CE'), blank=True, null=True)
  death_month_CE = models.SmallIntegerField(verbose_name=_('Death Month CE'), choices=monthes, blank=True, null=True)
  death_day_CE = models.SmallIntegerField(verbose_name=_('Death Day CE'), choices=days,blank=True, null=True)
  
  death_year_AH = models.SmallIntegerField(verbose_name=_('Death Year AH'), blank=True, null=True)
  death_month_AH = models.SmallIntegerField(verbose_name=_('Death Month AH'), choices=monthes, blank=True, null=True)
  death_day_AH = models.SmallIntegerField(verbose_name=_('Death Month AH'), choices=days,blank=True, null=True)
  
  class Meta:
    verbose_name = _('Author')
    verbose_name_plural = _('Authors')
  
  def __str__(self):
    if get_language() == 'ar':
      return self.first_name_ar + ' ' + self.last_name_ar
    else:
      return self.first_name_en + ' ' + self.last_name_en
    
class Title(models.Model):
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  arabic_name = models.CharField(max_length=250, blank=True)
  english_translated_name = models.CharField(max_length=250, blank=True)
  english_transliterated_name = models.CharField(max_length=250, blank=True)
  #cms_page = models.ForeignKey(cmsPage, related_name='title_cmsPage', on_delete=models.CASCADE, null=True, blank=True)
  def __str__(self):
    return self.arabic_name

class Manuscript(models.Model):
  title = models.ForeignKey(Title, on_delete=models.PROTECT)
  location = models.CharField(max_length=150, blank=True)
  call_number= models.CharField(max_length=150, blank=True)
  #cms_page = models.ForeignKey(cmsPage, related_name='manuscript_cmsPage', on_delete=models.CASCADE, null=True, blank=True)
  #aquisition_date = 
  acquisition_details = models.CharField(max_length=250, blank=True)
  arabic_copier_name = models.CharField(max_length=250, blank=True)
  english_copier_name = models.CharField(max_length=250, blank=True)
  def __str__(self):
    return self.call_number

class Folio(models.Model):
  title = models.ForeignKey(Title, on_delete=models.PROTECT)
  call_number= models.ForeignKey(Manuscript, on_delete=models.PROTECT)
  file_name = models.CharField(max_length=250, blank=True)
  page_index = models.IntegerField(blank=True, null=True)
  transcription = models.TextField(blank=True, null=True)
  def __str__(self):
    return self.file_name
