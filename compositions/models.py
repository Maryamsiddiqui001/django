from django.db import models
from django.utils.html import mark_safe
from cms.models.fields import PlaceholderField

# Create your models here.

class Composer(models.Model):
  monthes = [(1, "January"),(2, "Febraury"),(3, "March"),(4, "April"),(5, "May"),(6, "June"),(7, "July"),(8, "August"),(9, "September"),(10, "October"),(11, "November"),(12, "December"),]
  
  days = [(1, "1"),(2, "2"),(3, "3"),(4, "4"),(5, "5"),(6, "6"),(7, "7"),(8, "8"),(9, "9"),(10, "10"),(11, "11"),(12, "12"),(13, "13"),(14, "14"),(15, "15"),(16, "16"),(17, "17"),(18, "18"),(19, "19"),(20, "20"),(21, "21"),(22, "22"),(23, "23"),(24, "24"),(25, "25"),(26, "26"),(27, "27"),(28, "28"),(29, "29"),(30, "30"),(31, "31"),]
  
  composer_first_name_en = models.CharField(max_length=50, blank=True)
  composer_first_name_ar = models.CharField(max_length=50, blank=True)
  composer_middle_name_en = models.CharField(max_length=50, blank=True)
  composer_middle_name_ar = models.CharField(max_length=50, blank=True)
  composer_last_name_en = models.CharField(max_length=50)
  composer_last_name_ar = models.CharField(max_length=50)
  arabic_definite_article = models.BooleanField(default=False, blank=True, null=True,)
  composer_birth_city_en = models.CharField(max_length=50, blank=True)
  composer_birth_city_ar = models.CharField(max_length=50, blank=True)
  composer_birth_locality_en = models.CharField(max_length=50, blank=True)
  composer_birth_locality_ar = models.CharField(max_length=50, blank=True)
  composer_birth_country_en = models.CharField(max_length=50, blank=True)
  composer_birth_country_ar = models.CharField(max_length=50, blank=True)
  
  composer_birth_year = models.SmallIntegerField(blank=True, null=True)
  composer_birth_month = models.SmallIntegerField(choices=monthes, blank=True, null=True)
  composer_birth_day = models.SmallIntegerField(choices=days,blank=True, null=True)
  
  composer_death_year = models.SmallIntegerField(blank=True, null=True)
  composer_death_month = models.SmallIntegerField(choices=monthes, blank=True, null=True)
  composer_death_day = models.SmallIntegerField(choices=days,blank=True, null=True)
  
  def __str__(self):
        return self.composer_last_name_en

    
class ComposerImage(models.Model):
  composer = models.ForeignKey(Composer, on_delete=models.CASCADE)
  composer_image = models.ImageField(upload_to='compositions/composers/images/')
  profile_image = models.BooleanField(default=False)
  image_description_en = models.CharField(max_length=150)
  image_description_ar = models.CharField(max_length=150)
  
  def image_tag(self):
        if self.composer_image:
            return mark_safe('<img src="%s" style="width: 150px; height:150px;" />' % self.composer_image.url)
        else:
            return 'No Image Found'
  image_tag.short_description = 'Composer Image'
  
  def save(self, *args, **kwargs):
        if self.profile_image:
            try:
                temp = ComposerImage.objects.filter(composer=self.composer).get(profile_image=True)
                if self != temp:
                    temp.profile_image = False
                    temp.save()
            except ComposerImage.DoesNotExist:
                pass
        super(ComposerImage, self).save(*args, **kwargs)
  
  def __str__(self):
        return mark_safe('<img src="%s" style="width: 150px; height:150px;" />' % self.composer_image.url)

class Composition(models.Model):
  class Meta:
        ordering = ['year']
  title_en = models.CharField(max_length=150)
  title_ar = models.CharField(max_length=150)
  composer = models.ForeignKey(Composer, on_delete=models.CASCADE)
  year = models.SmallIntegerField(blank=True, null=True)
  
  def __str__(self):
        return self.title_en + ' - ' + self.composer.composer_last_name_en

class Rhythm(models.Model):
  rhythm_en = models.CharField(max_length=50, blank=True, null=True)
  rhythm_ar = models.CharField(max_length=50, blank=True, null=True)
  rhythm_svg = models.FileField(upload_to='compositions/rhythms/')
  
  def __str__(self):
        return self.rhythm_en
      
class Score(models.Model):
  composition = models.ForeignKey(Composition, on_delete=models.CASCADE) 
  maqam_en = models.CharField(max_length=50, blank=True, null=True)
  maqam_ar = models.CharField(max_length=50, blank=True, null=True)
  rhythm_en = models.CharField(max_length=50, blank=True, null=True)
  rhythm_ar = models.CharField(max_length=50, blank=True, null=True)
  rhythm = models.ForeignKey(Rhythm, on_delete=models.CASCADE, blank=True, null=True)
  #abc_score = models.FileField(upload_to='compositions/scores/')
  abc_score_text = models.TextField()
  notation_source_en = models.CharField(max_length=50, blank=True, null=True)
  notation_source_ar = models.CharField(max_length=50, blank=True, null=True)
  #Comment = PlaceholderField('comment')
  
  def __str__(self):
        return self.composition.title_en + ' - ' + self.notation_source_en

