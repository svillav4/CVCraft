from django import forms
from .models import Reviews

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = [
            'review'
        ]

        widgets = {
            'review': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }