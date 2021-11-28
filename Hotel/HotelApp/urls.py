from django.urls import path
from HotelApp import views
from .views import LoginView, ListView, ReservaRegisterPage
from django.contrib.auth.views import LogoutView

app_name = 'HotelApp'

urlpatterns = [
    path("", views.ReservaLoginView.as_view(), name = 'login'),
    path("reserva_ajax", views.verificaReserva, name = 'reserva-ajax'),

    path('login/', views.ReservaLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page='HotelApp:login'), name = 'logout'),
    path('register/', views.ReservaRegisterPage.as_view(), name='register'),
    
    path('reservas_exibe/', views.ReservaListView.as_view(), name = 'reservas-exibe'),
    path('reserva_detalhes/<int:pk>/', views.ReservaDetail.as_view(), name = 'reserva-detalhes'),
    path('reserva_criar/', views.ReservaCreate.as_view(), name = 'reserva-criar'),
    path('reserva_editar/<int:pk>/', views.ReservaUpdate.as_view(), name = 'reserva-editar'),
    path('reserva_deletar/<int:pk>/', views.ReservaDelete.as_view(), name = 'reserva-deletar'),
]