from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)  # Guardamos las ocupaciones como una cadena separada por comas
    hobbies = models.TextField()
    soft_skills = models.TextField()
    languages = models.TextField()
    references = models.TextField()
    education = models.TextField()
    work_experience = models.TextField()
    photo = models.ImageField(upload_to='profile_photos/')

    def __str__(self):
        return self.name

    @property
    def occupation_list(self):
        # Accedemos al valor del campo occupation (no al campo en sí)
        if self.occupation:
            return self.occupation.split(',')
        return []  # Retorna una lista vacía si no hay ocupaciones