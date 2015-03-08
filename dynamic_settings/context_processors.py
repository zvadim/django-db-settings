# -*- coding: utf-8 -*-
from django.db.models.fields.files import ImageFieldFile
from django.db. models import ImageField
from dynamic_settings.models import Settings


def dynamic_settings(request):
    s = Settings.objects.all()
    ret = {}
    for it in s:
        if it.type == 'box':
            it.value = bool(it.value)
        elif it.type == 'image':
            it.value = ImageFieldFile(instance=it, field=ImageField(upload_to='settings'), name=it.value)

        ret[it.key] = it.value

    return {'dynamic_settings': ret}