from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

@apphook_pool.register
class BooksApphook(CMSApp):
    name = _("Books Apphook")
    app_name = "books"
    
    def get_urls(self, page=None, language=None, **kwargs):
        return ["books.urls"]       # replace this with the path to your application's URLs module


