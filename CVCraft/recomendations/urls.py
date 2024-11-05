from django.urls import path, include
from .views import *

urlpatterns = [
    path('subprofile/', subprofile, name='subprofile'),
    path('selected_subprofile/<int:subprofile_id>/<int:index>/',selected_subprofile, name='selected_subprofile'),
    path('download_subprofile/<int:id>/<int:indice>/',download_pdf, name='download'),
    path('no-subprofile/', subprofile, name='no_subprofile'),
]