from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'titulo': 'App de Familiares',
        'mensaje': 'Bienvenido a la sección de Familiares'
    }
    return render(request, 'appfamiliares/index.html',context)