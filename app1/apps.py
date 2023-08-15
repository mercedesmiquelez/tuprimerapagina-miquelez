from django.apps import AppConfig


class AppcoderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app1'

def ready(self):
        # Importa tus modelos aquí para asegurarte de que las aplicaciones estén cargadas
        from .models import Entregable, Profesor, Estudiante, Curso