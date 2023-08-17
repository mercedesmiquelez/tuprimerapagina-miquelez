# Register your models here.
from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Comprador)
admin.site.register(models.Vendedor)
admin.site.register(models.Producto)