from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .recomendacionesIA import recomendacionesIA

# Create your views here.

def home(request):
    return render(request, 'home.html')

def subprofile(request):
    ia = recomendacionesIA(request)
    subprofile = ia.generateSubprofile()
    return render(request, 'subprofile.html', {'subprofiles':subprofile})  # Retorna un JSON con los datos generados