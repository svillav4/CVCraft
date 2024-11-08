from django.urls import path
from .views import *
urlpatterns = [
    path('createreview/', createreview, name='createreview'),
    path("delete_review/<int:review_id>/", delete_review, name="delete_review"),
]