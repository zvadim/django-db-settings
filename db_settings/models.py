# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings

FIELD_TYPE = (
    ('char', u'Однострочный'),
    ('text', u'Многострочный'),
    ('box', u'Чекбокс'),
    ('image', u'Изображение'),
)

if 'tinymce' in settings.INSTALLED_APPS:
    FIELD_TYPE += (('text_html', u'Многострочный с редактором'),)


class Settings(models.Model):
    name = models.CharField(u'Описание', max_length=100)
    key = models.CharField(u'Ключ', max_length=100, unique=True)
    value = models.TextField(u'Значение', blank=True)
    type = models.CharField(u'Тип поля', choices=FIELD_TYPE, max_length=16, default=FIELD_TYPE[0][0])

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.key)

    class Meta:
        verbose_name = u'Настройка'
        verbose_name_plural = u'Настройки'