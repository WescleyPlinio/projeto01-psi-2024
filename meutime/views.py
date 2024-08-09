from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def atletas(request):
    

    return render(request, "atletas.html")