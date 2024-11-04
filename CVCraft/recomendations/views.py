from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .recomendacionesIA import recomendacionesIA
from formulario.models import Profile
from .models import SubprofileData
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
# Create your views here.

def home(request):
    return render(request, 'home.html')


def subprofile(request):
    # Obtenemos el perfil del usuario actual
    profile = Profile.objects.filter(user=request.user).first()

    # Verificamos si ya existen subperfiles guardados para este usuario
    subprofile_data = SubprofileData.objects.filter(user=request.user).first()

    # Si ya existen subperfiles, los cargamos desde la base de datos
    if subprofile_data:
        subprofiles = subprofile_data.data  # Usamos los datos JSON ya guardados
        subprofile_id = subprofile_data.id  # Accedemos al id existente
    else:
        # Si no existen subperfiles guardados, generamos nuevos
        subprofiles = []
        ia = recomendacionesIA(request)
        
        for i in range(len(profile.occupation_list)):
            # Generamos el subperfil y lo añadimos a la lista
            subprofiles.append([ia.generateSubprofile(i), profile.occupation_list[i], profile.photo.url])
        
        # Guardamos los nuevos subperfiles en la base de datos y obtenemos el id
        new_subprofile_data = SubprofileData.objects.create(
            user=request.user,
            data=subprofiles,
            occupation_count=len(profile.occupation_list)
        )
        subprofile_id = new_subprofile_data.id  # Almacenamos el id del nuevo objeto

    # Pasamos el id al contexto si lo necesitas en el HTML
    return render(request, 'subprofile.html', {'subprofiles': subprofiles, 'subprofile_id': subprofile_id})


def selected_subprofile(request,subprofile_id, index):
    subprofile = SubprofileData.objects.get(id=subprofile_id).data[index]
    return render(request, 'selected_subprofile.html',{'subprofile':subprofile, 'subprofile_id':subprofile_id, 'index': index})


def download_pdf(request, subprofile_id, index):
    # Suponiendo que obtienes el JSON de algún lugar
    subprofile = SubprofileData.objects.get(id=subprofile_id).data[index]  # Función que retorna el JSON
    
    # Crear respuesta HTTP para PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="seccion_perfil.pdf"'
    
    # Renderizar solo la plantilla de la sección en PDF
    html = render_to_string('selected_subprofile.html', {'subprofile': subprofile})
    
    # Convertir HTML a PDF
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('Error al generar el PDF', status=500)
    return response
