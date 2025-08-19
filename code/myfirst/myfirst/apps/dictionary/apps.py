from django.apps import AppConfig

# настройки локального приложения

class DictionaryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dictionary'
    verbose_name = 'Словарь'