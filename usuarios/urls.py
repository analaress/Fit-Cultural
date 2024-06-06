from django.urls import path
from usuarios.views import loginIndexView, cadastroIndexView, logout

urlpatterns = [
    path("", loginIndexView, name="index"),
    path("cadastro", cadastroIndexView, name="cadastro"),
    path("logout", logout, name="logout")
]