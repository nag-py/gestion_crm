from django.urls import path
from .views import list_commande

urlpatterns = [
    path('', list_commande),
]