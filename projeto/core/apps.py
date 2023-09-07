from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'projeto.core'

class AuthenticationSystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projeto.core'

    def ready(self):
        import projeto.core.signals  # Importe o arquivo signals.py