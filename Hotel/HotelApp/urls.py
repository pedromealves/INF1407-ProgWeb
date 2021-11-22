from django.urls import path
from HotelApp import views

app_name = 'HotelApp'

urlpatterns = [
    path('exibe_reservas/', views.ReservaListView.as_view(), name = 'exibe-reservas'),
    path('reserva_detalhes/<int:pk>/', views.ReservaDetail.as_view(), name = 'reserva-detalhes')
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