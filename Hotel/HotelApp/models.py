from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Modelo de Reserva

"""

class Usuario(models.Model):
    nome = models.CharField(max_length = 100, help_text = 'Insira seu nome')
    email = models.EmailField(max_length = 200, help_text = 'Insira seu e-mail')
    dtNasc = models.DateField(verbose_name = 'Data de nascimento', help_text = 'Insira sua data de nascimento no formato DD/MM/AAAA')

    def __str__(self):
        return self.nome + ': ' + self.email

"""

class Reserva(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
    dataEntrada = models.DateField(verbose_name = 'Data de entrada')
    dataSaida =  models.DateField(verbose_name = 'Data de saída')
    horarioEntrada = models.TimeField(verbose_name = 'Horário de entrada')
    horarioSaida = models.TimeField(verbose_name = 'Horário de saída')

    def __str__(self):
        return str(self.dataEntrada) + ' - ' + str(self.dataSaida)
