
from django.urls import path
from . import views

urlpatterns = [
    path('create-profile/', views.create_profile, name='create_profile'),
    path('success/', views.success_page, name='success_page'),
]
