from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .recomendacionesIA import recomendacionesIA
from formulario.models import Profile

# Create your views here.

def home(request):
    return render(request, 'home.html')

def subprofile(request):
    profile = Profile.objects.filter(user=request.user).first()
    subprofiles=[]
    for i in range(len(profile.occupation_list)):
        ia = recomendacionesIA(request)
        subprofiles.append([ia.generateSubprofile(i),profile.occupation_list[i], profile.photo])
    return render(request, 'subprofile.html', {'subprofiles':subprofiles})  # Retorna un JSON con los datos generados