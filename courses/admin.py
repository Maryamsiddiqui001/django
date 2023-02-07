from django.contrib import admin
from django.utils.translation import get_language
from .models import Catagory, Course, Lesson, Question, Answer
from cms.admin.placeholderadmin import PlaceholderAdminMixin

class CoursesAdminSite(admin.AdminSite):
    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        if get_language() == 'ar':
          ordering = {
              "التصنيفات": 1,
              "الدورات": 2,
              "الدروس": 3,
              "الأسئلة": 4
          }
        else:
          ordering = {
              "Catagories": 1,
              "Courses": 2,
              "Lessons": 3,
              "Questions": 4
          }
        app_dict = self._build_app_dict(request)
        # a.sort(key=lambda x: b.index(x[0]))
        # Sort the apps alphabetically.
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # Sort the models alphabetically within each app.
        for app in app_list:
            app['models'].sort(key=lambda x: ordering[x['name']])

        return app_list

admin.site.register(Catagory)
admin.site.register(Course)

class LessonAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass

admin.site.register(Lesson, LessonAdmin)
#admin.site.register(Lesson)

class AnswerInline(admin.TabularInline):
    model = Answer
    #readonly_fields = ('votes',)
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['lesson', 'question_text_en', 'question_text_ar'],
        }),
    ]
    inlines = [AnswerInline]
    #list_display = ('question',)
    #search_fields = ['question']

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)

#admin.site.register(Question)
#admin.site.register(Answer)
