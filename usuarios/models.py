from django.db import models
class Usuario(models.Model):
    cpf = models.CharField(max_length=100, unique=True)
    senha = models.CharField(max_length=128)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.cpf
