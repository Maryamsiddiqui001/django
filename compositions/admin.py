from django.contrib import admin
#from cms.admin.placeholderadmin import PlaceholderAdminMixin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from .models import Composer, ComposerImage, Composition, Score, Rhythm
from django.utils.html import format_html


admin.site.register(Composer)

@admin.register(ComposerImage) 
class ComposerImageAdmin(admin.ModelAdmin):
  fields = ['image_tag', 'composer', "composer_image", "profile_image", "image_description_en", "image_description_ar"]
  readonly_fields = ['image_tag']

admin.site.register(Composition)

class ScoreAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass
admin.site.register(Score, ScoreAdmin)

class RhythmAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass
admin.site.register(Rhythm, RhythmAdmin)
#admin.site.register(Score)
#admin.site.register(ComposerImages)
