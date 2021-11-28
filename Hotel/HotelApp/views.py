from django.forms.forms import Form
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import View
from django.views.generic.list import ListView
#from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.models import User

from HotelApp.models import Reserva
from HotelApp.forms import ReservaModel2Form
from HotelApp.forms import ReservaModel2FormCreate

from django.http.response import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class ReservaLoginView(LoginView):
    template_name = 'HotelApp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("HotelApp:reservas-exibe")

class ReservaRegisterPage(FormView):
    template_name = 'HotelApp/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("HotelApp:reservas-exibe")

    def form_valid(self, form):
        user = form.save()

        if user is not None:
            login(self.request, user)
        return super(ReservaRegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("HotelApp:reservas-exibe")
        return super(ReservaRegisterPage, self).get(*args, **kwargs)

def verificaReserva(request):
    search_input_hrEntrada = request.GET.get('hrEntrada')
    search_input_hrSaida = request.GET.get('hrSaida')
    search_input_dtEntrada = request.GET.get('dtEntrada')
    search_input_dtSaida = request.GET.get('dtSaida')
    
    #print('opa', request.user)
    print(request)

    if(search_input_hrEntrada == search_input_hrSaida and search_input_dtEntrada == search_input_dtSaida and search_input_hrEntrada != ""):
        resposta = {
                'hrIgual':
                    'True'}
        return JsonResponse(resposta)
    else:
        resposta = {
                'hrIgual':
                    'False'}
        return JsonResponse(resposta)


class ReservaListView(LoginRequiredMixin, ListView):
    model = Reserva
    template_name = 'HotelApp/reserva.html'
    context_object_name = 'reservas'
    success_url = reverse_lazy("HotelApp:reservas-exibe")

    # def get(self, request, *args, **kwargs):
    #     objReservas = Reserva.objects.all()
    #     context = { 'reservas': objReservas }
    #     return render(request, 'HotelApp/reserva.html', context)

    # def post(self, request, *args, **kwargs):
    #     pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservas'] = context['reservas'].filter(user = self.request.user) # Apenas os itens do usuário logado

        search_input = self.request.GET.get('search-area') or ''
        #if search_input[4] != '-' and search_input[7] != '-' and search_input[]
        #0000-00-00

        if search_input:
            context['reservas'] = context['reservas'].filter(dataEntrada__exact=search_input)
            #print(context['reservas'])
        

        context['search_input'] = search_input
        print(context)
        #print('opa', context['search_input'])

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
        return render(request, 'HotelApp/reserva_editar.html', context)

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

    
