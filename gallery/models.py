from django.db import models
from filer.fields.image import FilerImageField
from django.utils.translation import get_language
from django.utils.translation import ugettext_lazy as _
from cms.models.fields import PlaceholderField

# Create your models here.
class Maker(models.Model):
  first_name_en = models.CharField(verbose_name=_('First Name en'), max_length=50, blank=True)
  first_name_ar = models.CharField(verbose_name=_('First Name ar'), max_length=50, blank=True)
  middle_name_en = models.CharField(verbose_name=_('Middle Name en'), max_length=50, blank=True)
  middle_name_ar = models.CharField(verbose_name=_('Middle Name en'), max_length=50, blank=True)
  last_name_en = models.CharField(verbose_name=_('Last Name en'), max_length=50, blank=True)
  last_name_ar = models.CharField(verbose_name=_('Last Name ar'), max_length=50, blank=True)
  birth_place_en = models.CharField(verbose_name=_('Birth Place en'), max_length=50, blank=True)
  birth_place_ar = models.CharField(verbose_name=_('Birth Place ar'), max_length=50, blank=True)
  birth_year = models.IntegerField( verbose_name=_('Birth Year'), blank=True, null=True )
  birth_month = models.IntegerField( verbose_name=_('Birth Month'), blank=True, null=True )
  birth_day = models.IntegerField( verbose_name=_('Birth Day'), blank=True, null=True )
  death_year = models.IntegerField( verbose_name=_('Death Year'), blank=True, null=True )
  death_month = models.IntegerField( verbose_name=_('Death Month'), blank=True, null=True )
  death_day = models.IntegerField( verbose_name=_('Death Day'), blank=True, null=True )
  maker_placeholder = PlaceholderField('maker_placeholder')
  
  class Meta:
    verbose_name = _('Maker')
    verbose_name_plural = _('Makers')
    
  def __str__(self):
    if get_language() == 'ar':
      return self.first_name_ar + ' ' + self.last_name_ar
    else:
      return self.first_name_en + ' ' + self.last_name_en

class Oud(models.Model):
  year = models.IntegerField( verbose_name=_('Year'), blank=True, null=True )
  place_of_manufacture_en = models.CharField(verbose_name=_('Place of Manufacture'), max_length=50, blank=True)
  place_of_manufacture_ar = models.CharField(verbose_name=_('Place of Manufacture'), max_length=50, blank=True)
  serial_number = models.CharField(verbose_name=_('Serial'), max_length=50, blank=True)
  rosetta_shape_en = models.CharField(verbose_name=_('Rosetta Shape'), max_length=50, blank=True)
  rosetta_shape_ar = models.CharField(verbose_name=_('Rosetta Shape'), max_length=50, blank=True)
  rosetta_diameter = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
  #maker = models.ForeignKey(Maker, on_delete=models.PROTECT, verbose_name=_('Oud Maker'), )
  maker = models.ManyToManyField(Maker)
  number_of_ribs = models.IntegerField(blank=True)
  bowel_width = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
  bowel_height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
  bowel_depth = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
  bowel_wood_en = models.CharField(verbose_name=_('Bowel Wood en'), max_length=50, blank=True)
  bowel_wood_ar = models.CharField(verbose_name=_('Bowel Wood ar'), max_length=50, blank=True)
  neck_length = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
  soundboard_wood_en = models.CharField(verbose_name=_('Soundboard Wood en'), max_length=50, blank=True)
  soundboard_wood_ar = models.CharField(verbose_name=_('Soundboard Wood ar'), max_length=50, blank=True)
  pegs_wood_en = models.CharField(verbose_name=_('Pegs Wood en'), max_length=50, blank=True)
  pegs_wood_ar = models.CharField(verbose_name=_('Pegs Wood ar'), max_length=50, blank=True)
  oud_placeholder = PlaceholderField('oud_placeholder')
  
  class Meta:
    verbose_name = _('Oud')
    verbose_name_plural = _('Ouds')
  
  def __str__(self):
    if get_language() == 'ar':
      makers = ''
      for maker in self.maker.all():
        makers = makers + maker.first_name_ar + ' ' + maker.last_name_ar + ', '
      return makers + ' - ' + str(self.year) + ' - ' + self.serial_number
    else:
      makers = ''
      for maker in self.maker.all():
        makers = makers + maker.first_name_en + ' ' + maker.last_name_en + ', '
      return makers + ' - ' + str(self.year) + ' - ' + self.serial_number

class OudImage(models.Model):
  oud = models.ForeignKey(Oud, on_delete=models.PROTECT, verbose_name=_('Oud'), )
  image_file = FilerImageField(
        verbose_name=_('Oud Image'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='oud_image',
    )
  description_en = models.CharField(verbose_name=_('Image Description en'), max_length=200, blank=True)
  description_ar = models.CharField(verbose_name=_('Image Description ar'), max_length=200, blank=True)
  source_en = models.CharField(verbose_name=_('Image Source en'), max_length=200, blank=True)
  source_ar = models.CharField(verbose_name=_('Image Source ar'), max_length=200, blank=True)
  is_featured = models.BooleanField(verbose_name=_('Is Featured?'))
  is_main = models.BooleanField(verbose_name=_('Main Image'), blank=True)
  oud_image_placeholder = PlaceholderField('oud_image_placeholder')
  
  class Meta:
    verbose_name = _('Oud Image')
    verbose_name_plural = _('Oud Images')
