# -*- coding: utf-8 -*-
from django.contrib.admin.widgets import AdminTextareaWidget, AdminTextInputWidget
from django.forms import widgets
from django.db import models
from django.db.models.fields.files import ImageFieldFile
from django import forms
from django.conf import settings

if 'tinymce' in settings.INSTALLED_APPS:
    from tinymce.widgets import TinyMCE

from .models import Settings


class SettingsCreationForm(forms.ModelForm):
    class Meta:
        model = Settings


class SettingsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SettingsForm, self).__init__(*args, **kwargs)

        if self.instance.type == 'char':
            self.fields['value'].widget = AdminTextInputWidget(attrs={})
        elif self.instance.type == 'text':
            self.fields['value'].widget = AdminTextareaWidget(attrs={'cols': 90, 'rows': 30},)
        elif self.instance.type == 'text_html':
                if 'tinymce' in settings.INSTALLED_APPS:
                    self.fields['value'].widget = TinyMCE(attrs={'cols': 90, 'rows': 30},)
                else:
                    self.fields['value'].widget = AdminTextareaWidget(attrs={'cols': 90, 'rows': 30},)
        elif self.instance.type == 'image':
            tmp = self.fields['value']
            #
            f = ImageFieldFile(instance=self.instance, field=models.ImageField(upload_to='db_settings'), name=self.instance.value)
            self.fields['value'] = forms.ImageField(label=tmp.label, required=True)
            self.initial['value'] = f
        else:
            self.fields['value'].widget = widgets.CheckboxInput(attrs={})

    def save(self, commit=True):
        m = super(SettingsForm, self).save(commit=False)

        if self.instance.type == u'box':
            #для чекбоксов если False, то сохраняем пустую строку
            if self.instance.value == u'False':
                self.instance.value = ''

        elif self.instance.type == u'image' and 'value' in self.changed_data:
            #для картинки самостоятельно делаем сохранение изображения
            nf = ImageFieldFile(instance=self.instance, field=models.ImageField(upload_to='db_settings'), name=self.instance.value.name)
            nf.field.name = 'value'
            nf.save(self.instance.value.name, self.instance.value, True)
            self.instance.value = self.instance.value.lower()

        if commit:
            m.save()
        return m
