Django Dynamic Settings
==================

It often happens that we need to be able dynamically to create/edit some settings and site variables, 
for example site title, logo and counter code.

`dynamic-settings` module is tailored specifically for these purposes allowing dynamically to create and further on to edit via django-admin records of the following types:

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

`$ pip install dynamic-settings`
or
`$ easy_install dynamic-settings`

If you want to install it from source, grab the git repository from GitHub and run setup.py:

```
$ git clone git://github.com/zvadim/django-dynamic-settings.git
$ cd dynamic-settings
$ python setup.py install
```

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
    'dynamic_settings.context_processors.dynamic_settings',
)
```

Using It
---------
in template  `{{ dynamic_settings.my_key }}`

TinyMCE
-------

For HTML fields TinyMCE can be applied. To enable `tinymce` support in `dynamic-settings` you need to add to `settings.py` the following:

```python

DYNAMIC_SETTINGS_TINYMCE_ENABLE = True

```