import re
from django.utils.translation import get_language
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
#from filer.fields.file import FilerFileField

class ABCscore(CMSPlugin):
    name = models.CharField(verbose_name=_('Score Name en'), max_length=50,)
    name_ar = models.CharField(verbose_name=_('Score Name ar'), max_length=50,)
    abc_score_text = models.TextField(verbose_name=_('ABC Text'), blank=True, null=True)
    class Meta:
      verbose_name = _('ABC Score')
      verbose_name_plural = _('ABC Scores')
    '''
    abctxt = FilerFileField(
        verbose_name=_('file'),
        null=True,
        on_delete=models.SET_NULL,
        )
    '''
    def __str__(self):
      if get_language() == 'ar':
          return self.name_ar
      else:
        return self.name
