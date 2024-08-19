# pages/forms.py
from django import forms

class MyForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    ocupacion = forms.CharField(label='Ocupación', max_length=100)
    hobbies = forms.CharField(label='Gustos o Hobbies', max_length=100, required=False)
    skills = forms.CharField(label='Soft Skills', max_length=100, required=False)
    idiomas = forms.CharField(label='Idiomas', max_length=100, required=False)
    referencias = forms.CharField(label='Referencias', max_length=100, required=False)
    estudios = forms.CharField(label='Estudios', widget=forms.Textarea, required=False)
    experiencia = forms.CharField(label='Experiencia Laboral', widget=forms.Textarea, required=False)
    archivo = forms.FileField(label='Foto', required=False)
