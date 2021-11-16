from django.db import models

# Create your models here.

# Modelo de usuário

class Usuario(models.Model):
    nome = models.CharField(max_length = 100, help_text = 'Insira seu nome')
    email = models.EmailField(max_length = 200, help_text = 'Insira seu e-mail')
    dtNasc = models.DateField(verbose_name = 'Data de nascimento', help_text = 'Insira sua data de nascimento no formato DD/MM/AAAA')

    def __str__(self):
        return self.nome + ': ' + self.email
