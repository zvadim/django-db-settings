Django Dynamic Settings
==================

Часто случается, что нам нужно иметь возможность динамически изменять некоторые настройки/переменные 
как название сайта, логотип или код счетчика к примеру. 

Для этого и написал этот модуль. dynamic-settings позволяет создавать и в дальнейчем редактивать через django-admin записи следующих типов:

* Char
* Text
* HTML text
* Boolean
* Image

Requirements
------------

Django dynamic-settings requires Django 1.3 or later.

Getting It
-----------
You can get Django dynamic-settings by using pip or easy_install:

$ pip install dynamic-settings
or
$ easy_install dynamic-settings

If you want to install it from source, grab the git repository from GitHub and run setup.py:

$ git clone git://github.com/zvadim/django-dynamic-settings.git
$ cd dynamic-settings
$ python setup.py install

Installing It
------------

To enable `dynamic_settings` in your project you need to add it to `INSTALLED_APPS` in your projects `settings.py` file:


```python
INSTALLED_APPS = (
    ...
    'dynamic_settings',
)
```

And also add new content processor

```python
TEMPLATE_CONTEXT_PROCESSORS = (
    ...
    dynamic_settings.context_processors.dynamic_settings
)
```

Using It
---------
in template  `{{ dynamic_settings.my_key }}`

TinyMCE
-------
...