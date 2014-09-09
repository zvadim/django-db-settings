# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

FIELD_TYPE = (
    ('char', _('One line input')),
    ('text', _('Multi-line field')),
    ('box', _('Checkbox')),
    ('image', _('Image')),
)

if 'tinymce' in settings.INSTALLED_APPS:
    FIELD_TYPE += (('text_html', _('Multi-line field with HTML')),)


class Settings(models.Model):
    name = models.CharField(_('Help text'), max_length=100)
    key = models.CharField(_('Field key'), max_length=100, unique=True)
    value = models.TextField(_('Value'), blank=True)
    type = models.CharField(_('Field type'), choices=FIELD_TYPE, max_length=16, default=FIELD_TYPE[0][0])

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.key)

    class Meta:
        verbose_name = _('Setting')
        verbose_name_plural = _('Settings')