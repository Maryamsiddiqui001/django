from django.contrib import admin
#from cms.admin.placeholderadmin import PlaceholderAdminMixin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from .models import Author, Title, Manuscript, Folio
from django.utils.html import format_html


admin.site.register(Author)


admin.site.register(Title)

admin.site.register(Manuscript)

#admin.site.register(Chapter)

admin.site.register(Folio)
