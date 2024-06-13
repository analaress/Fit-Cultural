from django.db import models
from django.contrib.auth.models import User


class DadosUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    cpf = models.CharField(max_length=11, verbose_name='CPF')
    data_nascimento = models.DateField(verbose_name='Data Nascimento')
    telefone = models.CharField(max_length=20, verbose_name='Telefone')
    logradouro = models.CharField(max_length=60, verbose_name='Logradouro')
    bairro = models.CharField(max_length=60, verbose_name='Bairro')
    cidade = models.CharField(max_length=30, verbose_name='Cidade')
    uf = models.CharField(max_length=30, verbose_name='UF')

    class Meta:
        db_table = 'app_dados_usuario'
        verbose_name = 'Dados Usuário'
        verbose_name_plural = 'Dados Usuários'
