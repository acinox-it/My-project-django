from django.urls import path
from .views import *


urlpatterns = [
    #path("",test_page, name="Test page"),
    path("", accueil, name="Acceuil page")
]
