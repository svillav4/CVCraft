from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # Relación con el modelo User
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100) #Texto para la ocupacion
    hobbies = models.TextField()  # Texto para los gustos o hobbies
    soft_skills = models.TextField()  # Texto para las soft skills
    languages = models.TextField()  # Idiomas
    references = models.TextField()  # Referencias
    education = models.TextField()  # Estudios
    work_experience = models.TextField()  # Experiencia laboral
    photo = models.ImageField(upload_to='profile_photos/')  # Campo para la foto

    def __str__(self):
        return self.name