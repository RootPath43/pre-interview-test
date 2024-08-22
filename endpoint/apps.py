from django.apps import AppConfig
from endpoint.calculations import Calculation


class EndpointConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'endpoint'


class InitializeCalculationsConfig(AppConfig):
    name = 'your_app'

    def ready(self):
        # Burada sınıf örneğinizi oluşturabilirsiniz
        Calculation().initialize()