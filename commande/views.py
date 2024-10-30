from django.shortcuts import render
from django.http import HttpResponse

def list_commande(request):
    return HttpResponse("La liste des commandes")