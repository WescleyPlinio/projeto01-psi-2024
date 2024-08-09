from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def atletas(request):
    lista_jogadoras = [
        {"nome": "Ana Cristina Souza", "idade": 20, "local_nascimento": "Santo André, SP", "posicao": "Ponteira"},
        {"nome": "Gabi Guimarães", "idade": 29, "local_nascimento": "Belo Horizonte, MG", "posicao": "Ponteira"},
        {"nome": "Julia Bergmann", "idade": 23, "local_nascimento": "Munich, Alemanha", "posicao": "Ponteira"},
        {"nome": "Carol Gattaz", "idade": 42, "local_nascimento": "São José do Rio Preto, SP", "posicao": "Central"},
        {"nome": "Diana Duarte", "idade": 27, "local_nascimento": "Maringá, PR", "posicao": "Central"},
        {"nome": "Thaisa Menezes", "idade": 37, "local_nascimento": "Rio de Janeiro, RJ", "posicao": "Central"},
        {"nome": "Tainara Santos", "idade": 23, "local_nascimento": "Volta Redonda, RJ", "posicao": "Oposta"},
        {"nome": "Rosamaria Montibeller", "idade": 29, "local_nascimento": "Nova Trento, SC", "posicao": "Oposta"},
        {"nome": "Nyeme Costa", "idade": 25, "local_nascimento": "Miracema, RJ", "posicao": "Líbero"},
        {"nome": "Roberta Ratzke", "idade": 34, "local_nascimento": "Curitiba, PR", "posicao": "Levantadora"},
        {"nome": "Macris Carneiro", "idade": 34, "local_nascimento": "Itajubá, MG", "posicao": "Levantadora"},

    ]
    
    context = {
        "jogadoras": lista_jogadoras,
    }
    return render(request, "atletas.html",context)

def sobre(request):
    criadores = [
        {"Nome":"Ellainy Nayara", "Idade": 17, "Turma": "INFOWEB3M" },
        {"Nome":"Wescley Plínio", "Idade": 18, "Turma": "INFOWEB3M" }

    ]
    context = {
        "criadores": criadores
    }
    return render(request, "sobre.html",context)
