from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('atletas.html', views.atletas, name="atletas")
]