# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Help text')),
                ('key', models.CharField(unique=True, max_length=100, verbose_name='Field key')),
                ('value', models.TextField(verbose_name='Value', blank=True)),
                ('type', models.CharField(default=b'char', max_length=16, verbose_name='Field type', choices=[(b'char', 'One line input'), (b'boolean', 'Checkbox'), (b'image', 'Image Field'), (b'text', 'Multi-line field'), (b'text_html', 'Multi-line field with HTML')])),
            ],
            options={
                'verbose_name': 'Setting',
                'verbose_name_plural': 'Stored Settings',
            },
            bases=(models.Model,),
        ),
    ]
