from django.shortcuts import render
from catalogo_viloes.models import Viloes

# Create your views here.

def mostrar_index(request):
    viloes = Viloes.objects.all()
    return render(request, 'index.html', {'viloes': viloes})

def mostrar_vilas(request):
    vilas = Viloes.objects.filter(categoria='Mana')
    return render(request, 'manas.html',  {'vilas': vilas})
