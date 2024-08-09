from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def atletas(request):
    lista_jogadoras = [
        {"nome": "Ana Cristina", "idade": 20, "local_nascimento": "Santo André, SP", "posicao": "Ponteira", "foto":"imgs/Anacris.jpg"},
        {"nome": "Gabi Guimarães", "idade": 29, "local_nascimento": "Belo Horizonte, MG", "posicao": "Ponteira", "foto":"imgs/Gabi.jpg"},
        {"nome": "Julia Bergmann", "idade": 23, "local_nascimento": "Munich, Alemanha", "posicao": "Ponteira", "foto":"imgs/juliab.jpg"},
        {"nome": "Carol Gattaz", "idade": 42, "local_nascimento": "São José do Rio Preto, SP", "posicao": "Central", "foto":"imgs/Carol.jpg"},
        {"nome": "Diana Duarte", "idade": 27, "local_nascimento": "Maringá, PR", "posicao": "Central", "foto":"imgs/Diana.jpg"},
        {"nome": "Thaisa Menezes", "idade": 37, "local_nascimento": "Rio de Janeiro, RJ", "posicao": "Central", "foto":"imgs/Thaisa.jpg"},
        {"nome": "Tainara Santos", "idade": 23, "local_nascimento": "Volta Redonda, RJ", "posicao": "Oposta", "foto":"imgs/Tainara.jpg"},
        {"nome": "Rosamaria Montibeller", "idade": 29, "local_nascimento": "Nova Trento, SC", "posicao": "Oposta", "foto":"imgs/Rosam.jpg"},
        {"nome": "Nyeme Costa", "idade": 25, "local_nascimento": "Miracema, RJ", "posicao": "Líbero", "foto":"imgs/Nyeme.jpg"},
        {"nome": "Macris Carneiro", "idade": 35, "local_nascimento": "Santo André, SP", "posicao": "Levantadora", "foto":"imgs/macris.jpg"},
        {"nome": "Roberta Ratzke", "idade": 34, "local_nascimento": "Curitiba, PR", "posicao": "Levantadora", "foto":"imgs/Roberta.jpg"},

    ]
    
    context = {
        "lista_jogadoras": lista_jogadoras,
    }
    return render(request, "atletas.html",context)

def sobre(request):
    criadores = [
        {"Nome":"Ellainy Nayara Motta dos Santos", "Idade": 17, "Turma": "INFOWEB3M", "foto":"imgs/lindia.jpg"},
        {"Nome":"Wescley Plínio Damasceno Galdino", "Idade": 18, "Turma": "INFOWEB3M", "foto":"imgs/lindio.jpg" }

    ]
    context = {
        "criadores": criadores
    }
    return render(request, "sobre.html",context)
