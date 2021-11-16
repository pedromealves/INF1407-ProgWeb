from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View
from HotelApp.models import Usuario
from HotelApp.forms import UsuarioModel2Form
from django.http.response import HttpResponseRedirect

# Create your views here.

# Cadastro de um novo usuário

class UsuarioCreateView(View):
    def get(self, request, *args, **kwargs):
        context = {'formulario': UsuarioModel2Form}
        return render(request, "HotelApp/cadastro.html", context)
    
    def post(self, request, *args, **kwargs):
        pass

class HomeCreateView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'HotelApp/home.html')

    
