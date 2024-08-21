from django.urls import path
from .views import HomePageView, FormPageView, TemplateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('form/', FormPageView.as_view(), name='form'),
    path('success/', TemplateView.as_view(template_name='pages/success.html'), name='success'),
]