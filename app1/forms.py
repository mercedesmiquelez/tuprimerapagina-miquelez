# from django import forms
# from .models import Entregable, Profesor, Estudiante

# class EntregableForm(forms.ModelForm):
#     class Meta:
#         model = Entregable
#         fields = '__all__'

# class ProfesorForm(forms.ModelForm):
#     class Meta:
#         model = Profesor
#         fields = '__all__'

# class EstudianteForm(forms.ModelForm):
#     class Meta:
#         model = Estudiante
#         fields = '__all__'

# class CursoSearchForm(forms.Form):
#     nombre = forms.CharField(required=False)

from django import forms
from .models import Comprador, Vendedor, Producto
class Comprador_forms(forms.ModelForm):
    class Meta:
        model = Comprador
        fields = '__all__'

class Vendedor_forms(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields ='__all__'
        

class Producto_forms(forms.ModelForm):
    class Meta:
        model = Producto
        fields  ='__all__'

class UsuSearchForm(forms.Form):
    nombre = forms.CharField(required=False)