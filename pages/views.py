# pages/views.py
from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import MyForm

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class FormPageView(FormView):
    template_name = 'pages/form.html'
    form_class = MyForm
    success_url = '/form/'  # URL a la que redirigir después del envío del formulario

    def form_valid(self, form):
        # Procesa los datos del formulario aquí
        # Ejemplo: guardar los datos en la base de datos, enviar un email, etc.
        return super().form_valid(form)