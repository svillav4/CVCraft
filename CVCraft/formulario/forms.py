
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name', 'occupation', 'hobbies', 'soft_skills', 
            'languages', 'references', 'education', 'work_experience', 'photo'
        ]
