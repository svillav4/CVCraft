
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name', 'occupation', 'tecnical_information', 'hobbies', 'soft_skills', 
            'languages', 'references', 'education', 'work_experience', 'photo'
        ]
    def clean_occupation(self):
        # Limpiar los datos del campo occupation antes de guardarlos
        occupation = self.cleaned_data.get('occupation', '')
        # Dividimos la cadena por comas y quitamos espacios en blanco
        occupation_list = [item.strip() for item in occupation.split(',') if item.strip()]
        # Convertimos la lista a un string separado por comas para almacenarlo en la base de datos
        return ','.join(occupation_list)