from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from HotelApp.models import Reserva
from HotelApp.forms import ReservaModel2Form
from django.http.response import HttpResponseRedirect

# Create your views here.

# Cadastro de um novo usuário

class ReservaListView(View):

    def get(self, request, *args, **kwargs):
        objReservas = Reserva.objects.all()
        context = { 'reservas': objReservas }
        return render(request, 'HotelApp/reserva.html', context)

    def post(self, request, *args, **kwargs):
        pass

class ReservaDetail(View):

    def get(self, request, pk, *args, **kwargs):
        reserva = Reserva.objects.get(pk=pk)
        context = { 'reserva': reserva }
        return render(request, 'HotelApp/reserva_detalhes.html', context)

    def post(self, request, *args, **kwargs):
        pass

    
# class UsuarioCreateView(View):
#     def get(self, request, *args, **kwargs):
#         context = {'formulario': UsuarioModel2Form}
#         return render(request, "HotelApp/cadastro.html", context)
    
#     def post(self, request, *args, **kwargs):
#         pass

# class HomeCreateView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'HotelApp/home.html')

    
