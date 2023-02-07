# -*- coding: utf-8 -*-

####################################################################################################

from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from .models import ABCscore

####################################################################################################

class ABCscore_plugin(CMSPluginBase):

    model = ABCscore
    name = _("ABC Score")
    text_enabled = True
    render_template = "abc_scores/plugin.html"


####################################################################################################

plugin_pool.register_plugin(ABCscore_plugin)
