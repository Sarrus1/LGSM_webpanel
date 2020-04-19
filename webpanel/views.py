from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from servers.models import Server
from .models import PlayerCount
from django.contrib.auth.decorators import login_required
import subprocess
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
import a2s

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

@login_required
def get_data(request, server_name):
    labels = []
    number = []
    Name_id=Server.objects.get(Name=server_name)
    queryset = PlayerCount.objects.filter(Name=Name_id)[:]
    for data in queryset:
        labels.append(data.timestamp)
        number.append(data.player_count)
    server=Server.objects.get(Name=server_name)
    address = (server.IP, server.Port)
    queryset=a2s.info(address, timeout=3.0, encoding=None)
    max_player=queryset.max_players
    playerdata={
        'labels': labels,
        'data': number,
        'max': max_player,
    }
    return JsonResponse(playerdata)

@login_required
def admin(request):
    return render(request, 'admin')