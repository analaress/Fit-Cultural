from django.shortcuts import render
from usuarios.forms import LoginForm, CadastroForm
def loginIndexView(request):
    form = LoginForm()
    return render(request, 'usuarios/index.html', {"form": form})

def cadastroIndexView(request):
    form = CadastroForm()
    return render(request, 'usuarios/cadastro.html', {"form": form})
