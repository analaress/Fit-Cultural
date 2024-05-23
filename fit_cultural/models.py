from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')

    def __init__(self, nome, data_nascimento, *args, **kwargs):
        super()
        self.nome = nome
        self.data_nascimento = data_nascimento

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        db_table = 'pessoa'

    def __str__(self):
        return f'[{self.pk}] - {self.nome}'
