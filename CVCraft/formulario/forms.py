
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name', 'PhoneNumber', 'Email', 'occupation', 'tecnical_information', 'hobbies', 'soft_skills', 
            'languages', 'references', 'education', 'work_experience', 'photo'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'PhoneNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'occupation': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'tecnical_information': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'hobbies': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'soft_skills': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'languages': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'references': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'education': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'work_experience': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
        }