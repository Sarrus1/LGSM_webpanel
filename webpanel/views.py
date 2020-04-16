from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Server
from django.contrib.auth.decorators import login_required
import subprocess


@login_required
def index(request):
    context= {
        'servers': Server.objects.all()
    }
    return render(request, 'webpanel/index.html', context)

def controlserver(request, server_path, control):
    if request.POST:
        subprocess.run(['bash', server_path, control])
    return HttpResponse(request.path_info)