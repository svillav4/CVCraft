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
         success_url = '/success/'  # Define una URL de éxito

         def form_valid(self, form):
             # Aquí puedes manejar lo que sucede cuando el formulario es válido
             return super().form_valid(form)