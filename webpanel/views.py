from django.shortcuts import render
from django.http import HttpResponse
from .models import Server

def index(request):
    context= {
        'servers': Server.objects.all()
    }
    return render(request, 'webpanel/index.html', context)

def buttons(request):
    return render(request, 'webpanel/buttons.html')