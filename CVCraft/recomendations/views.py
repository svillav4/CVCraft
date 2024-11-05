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
        
    # Verificamos si ya existen subperfiles guardados para este usuario
    subprofile_data = SubprofileData.objects.filter(user=request.user).first()

    if not subprofile_data.data:
        # Si no hay subperfiles, redirige a la página de advertencia
        return render(request, 'no_subprofile.html')

    subprofiles = subprofile_data.data  # Usamos los datos JSON ya guardados
    subprofile_id = subprofile_data.id  # Accedemos al id existente

    # Pasamos el id al contexto si lo necesitas en el HTML
    return render(request, 'subprofile.html', {'subprofiles': subprofiles, 'subprofile_id': subprofile_id})


def selected_subprofile(request,subprofile_id, index):
    subprofile = SubprofileData.objects.get(id=subprofile_id).data[index]
    return render(request, 'selected_subprofile.html',{'subprofile':subprofile, 'id':subprofile_id, 'indice': index})


def download_pdf(request, id, indice):
    print(f"Subprofile ID: {id}, Index: {indice}")
    # Suponiendo que obtienes el JSON de algún lugar
    subprofile = SubprofileData.objects.get(id=id).data[indice]  # Función que retorna el JSON
    
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
