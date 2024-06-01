from django.urls import path
from usuarios.views import loginIndexView, cadastroIndexView

urlpatterns = [
    path("", loginIndexView, name="index"),
    path("cadastro", cadastroIndexView, name="cadastro")
]