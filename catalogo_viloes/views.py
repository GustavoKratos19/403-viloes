from django.shortcuts import render
from catalogo_viloes.models import Viloes

# Create your views here.

def mostrar_index(request):
    viloes = Viloes.objects.all()
    return render(request, 'index.html', {'viloes': viloes})
