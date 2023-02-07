from django.contrib import admin
from django.utils.translation import get_language
from .models import Maker, Oud, OudImage
from cms.admin.placeholderadmin import PlaceholderAdminMixin

# Register your models here.
class MakerAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass
admin.site.register(Maker, MakerAdmin)

class OudAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass
admin.site.register(Oud, OudAdmin)

class OudImageAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass
admin.site.register(OudImage, OudImageAdmin)
