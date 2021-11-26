from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View
from django.views.generic.list import ListView
#from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from HotelApp.models import Reserva
from HotelApp.forms import ReservaModel2Form
from HotelApp.forms import ReservaModel2FormCreate

from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

class ReservaLoginView(LoginView):
    template_name = 'HotelApp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("HotelApp:reservas-exibe")

class ReservaListView(LoginRequiredMixin, ListView):
    model = Reserva
    template_name = 'HotelApp/reserva.html'
    context_object_name = 'reservas'

    # def get(self, request, *args, **kwargs):
    #     objReservas = Reserva.objects.all()
    #     context = { 'reservas': objReservas }
    #     return render(request, 'HotelApp/reserva.html', context)

    # def post(self, request, *args, **kwargs):
    #     pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservas'] = context['reservas'].filter(user = self.request.user) # Apenas os itens do usuário logado
        return context
        

class ReservaDetail(LoginRequiredMixin, CreateView):
    def get(self, request, pk, *args, **kwargs):
        reserva = Reserva.objects.get(pk=pk)
        context = { 'reserva': reserva }
        return render(request, 'HotelApp/reserva_detalhes.html', context)

    def post(self, request, *args, **kwargs):
        pass

class ReservaCreate(LoginRequiredMixin, CreateView):
    # def get(self, request, *args, **kwargs):
    #     # reserva = Reserva.objects.get(pk=pk)
    #     # context = { 'reserva': reserva }
    #     # return render(request, 'HotelApp/reserva_detalhes.html', context)
    #     #formulario = Reserva.objects.only('dataEntrada')
    #     formulario = ReservaModel2FormCreate
    #     context = {'formulario': formulario,}
    #     return render(request, 'HotelApp/reserva_criar.html', context)

    # def post(self, request, *args, **kwargs):
    #     formulario = ReservaModel2Form(request.POST)
    #     if formulario.is_valid():
    #         contato = formulario.save() # Registro compatível com o banco criado
    #         contato.save() # Salvo efetivamente no banco
    #         return HttpResponseRedirect(reverse_lazy("HotelApp:reservas-exibe"))

    model = Reserva
    template_name = 'HotelApp/reserva_criar.html'
    context_object_name = 'reserva'
    fields = ['dataEntrada', 'dataSaida', 'horarioEntrada', 'horarioSaida']
    success_url = reverse_lazy("HotelApp:reservas-exibe") # Após post submetido

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ReservaCreate, self).form_valid(form)

        
class ReservaUpdate(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs): # Busca os dados de uma reserva e exibe como um formulário
        reserva = Reserva.objects.get(pk=pk)
        formulario = ReservaModel2FormCreate(instance=reserva)
        context = {'form': formulario, } # Coloca o registro recuperado do banco e coloca num formulário
        return render(request, 'HotelApp/reserva_criar.html', context)

    def post(self, request, pk, *args, **kwargs): # Recebe os dados de uma reserva e atualiza o banco de dados
        reserva = get_object_or_404(Reserva, pk=pk) # Pega a reserva ou retorna erro 404
        formulario = ReservaModel2FormCreate(request.POST, instance=reserva)
        if formulario.is_valid():
            contato = formulario.save()
            contato.save()
            return HttpResponseRedirect(reverse_lazy("HotelApp:reservas-exibe"))
        else:
            context = {'formulario': formulario, } # Coloca o registro recuperado e coloca num formulário
            return render(request, 'HotelApp/reserva_criar.html', context)

class ReservaDelete(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        reserva = Reserva.objects.get(pk=pk)
        context = { 'reserva': reserva }
        return render(request, 'HotelApp/reserva_confirmar_deletar.html', context)

    def post(self, request, pk, *args, **kwargs):
        reserva = Reserva.objects.filter(pk=pk).delete()
        return HttpResponseRedirect(reverse_lazy("HotelApp:reservas-exibe"))



    
# class UsuarioCreateView(View):
#     def get(self, request, *args, **kwargs):
#         context = {'formulario': UsuarioModel2Form}
#         return render(request, "HotelApp/cadastro.html", context)
    
#     def post(self, request, *args, **kwargs):
#         pass

# class HomeCreateView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'HotelApp/home.html')

    
