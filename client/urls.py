from django.urls import path
from .views import list_client

urlpatterns = [
    path('', list_client),
]