from django.shortcuts import render
from django.http import HttpResponse

def list_client(request):
    return HttpResponse("La liste des clients")
