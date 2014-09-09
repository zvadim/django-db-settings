# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Settings
from .forms import *


class SettingsAdmin(admin.ModelAdmin):
    add_form = SettingsCreationForm

    change_readonly_fields = ('name', 'key')

    form = SettingsForm
    ordering = ['key']
    list_display = ('name', 'key')

    fieldsets = [
        (None, {
            'fields': ('key', 'name', 'value',),
            }
        ),
    ]
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('type', 'key', 'name',)
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.change_readonly_fields
        return super(SettingsAdmin, self).get_readonly_fields(request, obj)

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super(SettingsAdmin, self).get_fieldsets(request, obj)

    def get_form(self, request, obj=None, **kwargs):
        defaults = {}
        if obj is None:
            defaults.update({
                'form': self.add_form,
                'fields': admin.util.flatten_fieldsets(self.add_fieldsets),
            })

        defaults.update(kwargs)
        return super(SettingsAdmin, self).get_form(request, obj, **defaults)

    def response_add(self, request, obj, post_url_continue='../%s/'):
        # 'Save' -> 'Save and continue editing'
        if '_addanother' not in request.POST and '_popup' not in request.POST:
            request.POST['_continue'] = 1
        return super(SettingsAdmin, self).response_add(request, obj, post_url_continue)

admin.site.register(Settings,SettingsAdmin)
