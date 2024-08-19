from django.urls import path
from .views import HomePageView, FormPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('form/', FormPageView.as_view(), name='form'),
]