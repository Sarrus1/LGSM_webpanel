from django.shortcuts import render
from django.http import HttpResponse
from .models import Server
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    context= {
        'servers': Server.objects.all()
    }
    return render(request, 'webpanel/index.html', context)