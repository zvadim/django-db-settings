from django.conf import settings

ENABLE_TINYMCE = getattr(settings, 'DYNAMIC_SETTINGS_TINYMCE_ENABLE', False)

UPLOAD_TO_DIRECTORY = getattr(settings, 'DYNAMIC_SETTINGS_UPLOAD_TO', 'dynamic-settings')