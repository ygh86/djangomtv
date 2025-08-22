from django.shortcuts import render
from .models import Familiares

# Create your views here.
def index(request):
    context = {
        'titulo': 'App de Familiares',
        'mensaje': 'Bienvenido a la sección de Familiares'
    }
    return render(request, 'appfamiliares/index.html',context)

def lista_familiares(request):
    familiares = Familiares.objects.all()
    context = {
        'titulo': 'Listado de Familiares',
        'familiares': familiares
    }
    return render(request, 'appfamiliares/lista_familiares.html', context)

def detalle_familiar(request, id):
    familiar = Familiares.objects.get(id=id)
    context = {
        'titulo': 'Detalle del Familiar',
        'familiar': familiar
    }
    return render(request, 'appfamiliares/detalle_familiar.html', context)