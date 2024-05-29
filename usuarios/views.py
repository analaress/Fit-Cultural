from django.shortcuts import render
from usuarios.forms import LoginForms, CadastroForms
def LoginIndexView(request):
    form = LoginForms()
    return render(request, 'usuarios/index.html', {"form": form})

def CadastroIndexView(request):
    form = CadastroForms()
    return render(request, 'usuarios/cadastro.html', {"form": form})
