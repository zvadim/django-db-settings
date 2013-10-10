django-settings
===============

Install:
pip install git+git://github.com/zvadim/django-db-settings.git

INSTALLED_APPS = (
    ...
    db_settings
)

TEMPLATE_CONTEXT_PROCESSORS = (
    ...
    db_settings.context_processors.settings
)


Use:
in template {{ db_settings.my_key }}