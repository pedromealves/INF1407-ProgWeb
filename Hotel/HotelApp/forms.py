from django.db.models import fields
from django import forms
from HotelApp.models import Usuario

class UsuarioModel2Form(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'