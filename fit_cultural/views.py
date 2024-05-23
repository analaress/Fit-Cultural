from django.http import HttpResponse
from django.shortcuts import render
from .models import Pessoa

def index(request):
    if request.method == 'POST':
        pessoa = Pessoa(request.POST['nome'], request.POST['data'])
        pessoa.save()
    return render(request, 'fit_cultural/index.html')
