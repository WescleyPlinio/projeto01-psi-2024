from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index.html', views.index, name="index"),
    path('atletas.html', views.atletas, name="atletas")
    path('sobre.html', views.sobre, name="sobre")
]