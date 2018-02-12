from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_text_ckeditor.fields import HTMLField


class Block(CMSPlugin):
    title = models.CharField(_('Title'), max_length=64)
    content = HTMLField(_('Content'), blank=True)


# ------------------------------------------------------------------------------
# CMS Plugin/Admin
# ------------------------------------------------------------------------------
class BlockPlugin(CMSPluginBase):
    name = 'Block Plugin'
    module = 'Content'
    model = Block
    allow_children = True
    child_classes = (
        'CardPlugin',
    )
    render_template = "plugins/block.html"


class CardPlugin(CMSPluginBase):
    name = 'Card Plugin'
    module = 'Content'
    model = Block
    allow_children = True
    parent_classes = (
        'BlockPlugin',
    )
    render_template = "plugins/card.html"


plugin_pool.register_plugin(BlockPlugin)
plugin_pool.register_plugin(CardPlugin)
