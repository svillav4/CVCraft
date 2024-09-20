from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile  # Asegúrate de importar el modelo Profile

def create_profile(request):
    user = request.user  # Obtén el usuario autenticado

    # Intenta obtener el perfil existente o crear uno nuevo
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)  # Asocia el formulario con el perfil existente
        if form.is_valid():
            form.save()  # Guarda los datos en la base de datos
            return redirect('success_page')  # Redirige a una página de éxito
    else:
        form = ProfileForm(instance=profile)  # Pre-carga el formulario con los datos del perfil

    return render(request, 'create_profile.html', {'form': form})

def success_page(request):
    return render(request, 'success.html')
