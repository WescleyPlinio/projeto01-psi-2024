from django.shortcuts import render
from .models import Atleta

def index(request):
    return render(request, "index.html")

def atletas(request):
    context = {
        "atletas" : Atleta.objects.all
    }
    return render(request, "atletas.html",context)

def sobre(request):
    criadores = [
        {"Nome":"Ellainy Nayara Motta dos Santos", "Idade": 17, "Turma": "INFOWEB3M", "foto":"static/imgs/lindia.jpg"},
        {"Nome":"Wescley Plínio Damasceno Galdino", "Idade": 18, "Turma": "INFOWEB3M", "foto":"static/imgs/lindio.jpg"}

    ]
    context = {
        "criadores": criadores
    }
    return render(request, "sobre.html", context)
