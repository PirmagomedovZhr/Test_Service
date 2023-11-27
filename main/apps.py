from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'


class AppConfig(AppConfig):
    name = 'main'

    def ready(self):
        from .utils import load_data
        load_data()