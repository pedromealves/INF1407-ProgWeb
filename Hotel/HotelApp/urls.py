from django.urls import path
from HotelApp import views
from .views import LoginView, ListView
from django.contrib.auth.views import LogoutView

app_name = 'HotelApp'

urlpatterns = [
    path('login/', views.ReservaLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page='HotelApp:login'), name = 'logout'),
    
    path('reservas_exibe/', views.ReservaListView.as_view(), name = 'reservas-exibe'),
    path('reserva_detalhes/<int:pk>/', views.ReservaDetail.as_view(), name = 'reserva-detalhes'),
    path('reserva_criar/', views.ReservaCreate.as_view(), name = 'reserva-criar'),
    path('reserva_editar/<int:pk>/', views.ReservaUpdate.as_view(), name = 'reserva-editar'),
    path('reserva_deletar/<int:pk>/', views.ReservaDelete.as_view(), name = 'reserva-deletar'),
]

"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeCreateView.as_view(), name = 'homepage'), 
    path('cadastro/', views.UsuarioCreateView.as_view(), name='cadastro-contato'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeCreateView.as_view(), name = 'homepage'), 
    path('cadastro/', views.UsuarioCreateView.as_view(), name='cadastro-contato'),
]


"""