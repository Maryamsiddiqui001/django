from django.contrib import admin

# Register your models here.
from .models import Author, Publisher, Type, Title, Translator, Genre

class AuthorAdmin(admin.ModelAdmin):
    ordering = ['first_name_en', 'last_name_en']
admin.site.register(Author, AuthorAdmin)

class PublisherAdmin(admin.ModelAdmin):
    ordering = ['name_en']
admin.site.register(Publisher, PublisherAdmin)

admin.site.register(Type)
admin.site.register(Title)

class TranslatorAdmin(admin.ModelAdmin):
    ordering = ['first_name_en', 'last_name_en']
admin.site.register(Translator, TranslatorAdmin)

class GenreAdmin(admin.ModelAdmin):
    ordering = ['name_en']
admin.site.register(Genre, GenreAdmin)
