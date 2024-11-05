from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile  # Asegúrate de importar el modelo Profile
from recomendations.models import SubprofileData
from recomendations.recomendacionesIA import recomendacionesIA
def create_profile(request):
    user = request.user  # Obtén el usuario autenticado

    # Intenta obtener el perfil existente o crear uno nuevo
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)  # Asocia el formulario con el perfil existente
        if form.is_valid():
            form.save()  # Guarda los datos en la base de datos

            # Obtenemos el perfil del usuario
            profile = Profile.objects.filter(user=request.user).first()

            # Verificamos si ya existen subperfiles guardados para este usuario
            subprofile_data = SubprofileData.objects.filter(user=request.user).first()

            # Si ya existen subperfiles, los eliminamos de la base de datos
            if subprofile_data:
                subprofile_data.delete()

            # Creamos nuevos subperfiles
            subprofiles = []
            ia = recomendacionesIA(request)

            for i in range(len(profile.occupation_list)):
                # Generamos el subperfil y lo añadimos a la lista
                subprofiles.append([ia.generateSubprofile(i), profile.occupation_list[i], profile.photo.url])

            # Guardamos los nuevos subperfiles en la base de datos
            subprofile_data = SubprofileData.objects.create(
                user=request.user,
                data=subprofiles,
                occupation_count=len(profile.occupation_list)
            )

            # Accedemos al id del nuevo subperfil guardado
            subprofile_id = subprofile_data.id

            return redirect('success_page')  # Redirige a una página de éxito
    else:
        form = ProfileForm(instance=profile)  # Pre-carga el formulario con los datos del perfil

    return render(request, 'create_profile.html', {'form': form})

def success_page(request):
    return render(request, 'success.html')