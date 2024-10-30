from django.shortcuts import render
from django.http import HttpResponse

def list_client(request):
    return render (request, 'client/list_client.html')
