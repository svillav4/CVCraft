from django.contrib import admin
from django.urls import path, include
from recomendations import views as recomendation
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', recomendation.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('formulario/', include('formulario.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)