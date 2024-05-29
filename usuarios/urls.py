from django.urls import path
from usuarios.views import LoginIndexView, CadastroIndexView

urlpatterns = [
    path("", LoginIndexView, name="index"),
    path("cadastro", CadastroIndexView, name="cadastro")
]