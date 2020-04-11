from django.shortcuts import render
from django.http import HttpResponse
from .models import Server

servers = [
    {
        'Name': 'AWP_only',
        'IP': '192.168.1.107',
        'Port': '27015',
        'Status': 'Running'
    },
    {
        'Name': 'Surf',
        'IP': '192.168.1.107',
        'Port': '27015',
        'Status': 'Running'
    }
]


def index(request):
    context= {
        'servers': Server.objects.all()
    }
    return render(request, 'webpanel/index.html', context)

def buttons(request):
    return render(request, 'webpanel/buttons.html')