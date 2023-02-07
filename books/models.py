from django.db import models
from filer.fields.image import FilerImageField
from django.utils.translation import get_language
from django.utils.translation import ugettext_lazy as _
from cms.models.fields import PlaceholderField

# Create your models here.
class Author(models.Model):
    first_name_en = models.CharField(max_length=200, blank=True)
    first_name_ar = models.CharField(max_length=200, blank=True)
    last_name_en = models.CharField(max_length=200, blank=True)
    last_name_ar = models.CharField(max_length=200, blank=True)
    arabic_definite_article = models.BooleanField(default=False)
    
    def __str__(self):
        return self.first_name_en + " " + self.last_name_en

class Translator(models.Model):
    first_name_en = models.CharField(max_length=200, blank=True)
    first_name_ar = models.CharField(max_length=200, blank=True)
    last_name_en = models.CharField(max_length=200, blank=True)
    last_name_ar = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self. first_name_en + " " + self.last_name_en
      
class Publisher(models.Model):
    name_en = models.CharField(max_length=200, unique=True)
    name_ar = models.CharField(max_length=200, default='غير معروف')
    def __str__(self):
        return self.name_en 

class Genre(models.Model):
    name_en = models.CharField(max_length=200, unique=True)
    name_ar = models.CharField(max_length=200, blank=True, default='تصنيف')
    def __str__(self):
        return self.name_en
      
class Type(models.Model):
    type = models.CharField(max_length=10, unique=True)
    
    def __str__(self):
        return self.type
      
class Title(models.Model):
    LANGUAGES = (
        ('en', 'English'),
        ('fr', 'French'),
        ('de', 'German'),
        ('sr', 'Serbian'),
        ('ar', 'Arabic'),
        ('cn', 'Chinese'),
        ('sw', 'Swedish'),
        ('ak', 'Akkadian'),
        ('la', 'Latin'),
        ('es', 'Spanish'),
        ('fa', 'Persian'),
        ('el', 'Greek'),
        ('ru', 'Russian'),
        ('pt', 'Portuguese'),
        ('tr', 'Turkish'),
        ('it', 'Italian'),
    )
    cover = FilerImageField(
        verbose_name=_('Book Cover'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='cover',
    )
    title_en = models.CharField(max_length=200, unique=True)
    title_ar = models.CharField(max_length=200, default='العنوان')
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre, blank=True)
    translated = models.BooleanField()
    translators = models.ManyToManyField(Translator, blank=True)
    year = models.IntegerField(default=0)
    original_language = models.CharField(max_length=2, choices=LANGUAGES, blank=True)
    language = models.CharField(max_length=2, choices=LANGUAGES)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    types = models.ForeignKey(Type, on_delete=models.CASCADE)
    file = models.CharField(max_length=500, blank=True)
    def __str__(self):
        return self.title_en
