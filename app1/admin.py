from django.contrib import admin

from .models import Entregable, Profesor, Estudiante, Curso

admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Entregable)

# Register your models here.
