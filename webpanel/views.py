from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from servers.models import Server
from django.contrib.auth.decorators import login_required
import subprocess
import valve.source
import valve.source.a2s
import valve.source.master_server


@login_required
def index(request):
    context= {
        'servers': Server.objects.all()
    }
    return render(request, 'webpanel/index.html', context)

@login_required
def controlserver(request, server_path, control):
    subprocess.run(['bash', server_path, control])
    return HttpResponse(request.path_info)

from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
