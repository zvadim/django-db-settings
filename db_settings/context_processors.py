# -*- coding: utf-8 -*-
from .models import Settings
from django.db.models.fields.files import ImageFieldFile
from django.db. models import ImageField


def settings(request):

    s = Settings.objects.all()
    ret = {}
    for it in s:
        if it.type == 'box':
            if it.value:
                it.value = True
            else:
                it.value = False
        elif it.type == 'image':
            it.value = ImageFieldFile(instance=it, field=ImageField(upload_to='settings'), name=it.value)

        ret[it.key] = it.value

    return {'db_settings': ret}