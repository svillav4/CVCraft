from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .recomendacionesIA import recomendacionesIA

# Create your views here.

def home(request):
    return render(request, 'home.html')

def subprofile(request):
    return render(request, 'subprofile.html')

def generar_recomendacion(request):
    if request.method == 'POST':
        ia = recomendacionesIA(request)
       # for idx in range(len(request.))
        subprofile = ia.generateSubprofile()
        return JsonResponse(subprofile)  # Retorna un JSON con los datos generados
    return render(request, 'tu_template.html')  # Si es GET, carga el template