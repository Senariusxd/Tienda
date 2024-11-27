# forms.py
from django import forms
from .models import Producto, Generos

class GenerosForm(forms.ModelForm):
    class Meta:
        model = Generos
        fields = ['nombre']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'foto']  # Incluir generos

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['descripcion'].widget.attrs.update({'class': 'form-control', 'rows': 3})
        self.fields['precio'].widget.attrs.update({'class': 'form-control'})
        self.fields['foto'].widget.attrs.update({'class': 'form-control'})
        