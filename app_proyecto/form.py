from django import forms

class Cliente(forms.Form):
    empresa = forms.CharField(max_length=40)
    mail = forms.EmailField()
    fecha_compra = forms.DateField()

class Vendedor(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    mail = forms.EmailField()
    antiguedad = forms.IntegerField()

class Productos(forms.Form):
    producto = forms.CharField(max_length=40)
    stock = forms.IntegerField()
