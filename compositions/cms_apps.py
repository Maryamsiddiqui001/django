from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

@apphook_pool.register
class compositionsApphook(CMSApp):
    app_name = "compositions"  # must match the application namespace
    name = "compositions Apphook"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["compositions.urls"] # replace this with the path to your application's URLs module
