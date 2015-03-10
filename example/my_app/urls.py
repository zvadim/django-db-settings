# coding: utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('my_app.views',
    url(r'^$', 'main_page', name='main_page'),
)
