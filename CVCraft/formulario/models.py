from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)  # Guardamos las ocupaciones como una cadena separada por comas
    tecnical_information = models.TextField(null=True, blank=True)
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
    
    @property
    def tecnical_information_list(self):
        if self.tecnical_information:
            return self.occupation.split(',')
        return []
    
    @property
    def hobbies_list(self):
        if self.hobbies:
            return self.hobbies.split(',')
        return []  
    
    @property
    def soft_skills_list(self):
        if self.soft_skills:
            return self.soft_skills.split(',')
        return []  
    
    @property
    def references_list(self):
        if self.references:
            return self.references.split(',')
        return []  

    @property
    def education_list(self):
        if self.education:
            return self.education.split(',')
        return []

    @property
    def work_experience_list(self):
        if self.work_experience:
            return self.work_experience.split(',')
        return []