from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _



from .models import Composer, Composition, Score, ComposerImage
# Create your views here.



def index(request):
  #composers_count = Composer.objects.count()
  #compositions_count = Composition.objects.count()
  #scores_count = Score.objects.count()
  
  #composers = Composer.objects.prefetch_related('ComposerImage', 'Composition', 'Score' ).all
  composers  = Composer.objects.order_by('composer_last_name_en')
  composers_count = Composer.objects.count()
  
  #profile_images = ComposerImage.objects.filter(profile_image=True)
  return render(request, 'compositions/index.html', {'composers': composers, 'composers_count': composers_count,})
  #return HttpResponse(_("Hello, world. The database has {0} composers, {1} compositions, and {2} scores. ".format(composers_count, compositions_count, scores_count)))
  
def score(request, score_id):
  try:
    score = Score.objects.get(pk=score_id)
    composition = Composition.objects.get(score__pk=score_id)
    composer = Composer.objects.get(composition__pk=composition.pk)
    
  except Score.DoesNotExist:
    raise Http404("Score does not exist")
  return render(request, 'compositions/score.html', {'score': score, 'composer': composer, 'composition': composition})
