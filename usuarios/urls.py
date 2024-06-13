from django.urls import path
from usuarios.views import loginIndexView, cadastroView, logout

urlpatterns = [
    path("", loginIndexView, name="index"),
    path("cadastro", cadastroView, name="cadastro"),
    path("logout", logout, name="logout"),
]
