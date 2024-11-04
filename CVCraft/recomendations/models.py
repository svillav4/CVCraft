from django.db import models
from django.contrib.auth.models import User
import json

class SubprofileData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.JSONField()  # JSONField para guardar el JSON completo de subprofiles
    occupation_count = models.IntegerField()  # Para almacenar el número de ocupaciones
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación

    def __str__(self):
        return f"Subprofile data for {self.user.username} with {self.occupation_count} occupations"
