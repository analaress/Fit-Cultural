from django.shortcuts import render, redirect
from usuarios.forms import LoginForm, CadastroForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
# from .models import Usuario


def loginIndexView(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cpf=form['cpf'].value()
            senha=form['senha'].value()

            usuario = auth.authenticate(
                request,
                username=cpf,
                password=senha
            )

            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f"{cpf} logado com sucesso!")
                return redirect('home')

            else:
                messages.error(request, f"O login digitado não existe!")
                return redirect('index')
        print(form.errors)


    return render(request, 'usuarios/index.html', {"form": form})

def cadastroView(request):
    form = CadastroForm()

    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            nome=form["nome_cadastro"].value()
            email=form["email"].value()
            senha=form["senha"].value()

            if User.objects.filter(username=nome).exists():
                messages.success(request, f"Usuário já existente!")
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )

            usuario.save()
            messages.success(request, 'Cadastro efetuado com sucesso! Agora é só logar!')
            return redirect('index')

    return render(request, 'usuarios/cadastro.html', {"form": form})


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso')
    return redirect('index')

# def listaUsuarios(request):
#     usuarios = Usuario.objects.all()
#     return render(request, 'usuarios/lista.html', {'usuarios': usuarios})