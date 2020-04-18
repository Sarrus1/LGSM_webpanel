from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from servers.models import Server
from .models import PlayerCount
from django.contrib.auth.decorators import login_required
import subprocess
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


##à supprimer
import a2s
from time import strftime
from servers.models import Server

def playercounter():
    for server in Server.objects.all():
        address = (server.IP, server.Port)
        playernumber=a2s.info(address, timeout=3.0, encoding=None).player_count
        maxplayer=a2s.info(address, timeout=3.0, encoding=None).max_players
        now = strftime("%H:%M")
        serverstat=PlayerCount(timestamp=now, player_count=playernumber, max_player=maxplayer, Name=server)
        serverstat.save()
    #to_delete = PlayerCount.objects.values()[:1].get()
    #PlayerCount.objects.filter(id=to_delete['id']).delete()
##

@login_required
def index(request):
    playercounter()
    context= {
        'servers': Server.objects.all()
    }
    queryset= (PlayerCount.objects.values())
    return render(request, 'webpanel/index.html', context)

@login_required
def controlserver(request, server_path, control):
    subprocess.run(['bash', server_path, control])
    return HttpResponse(request.path_info)

def get_data(request):
    labels = []
    number = []
    queryset = PlayerCount.objects.all()[:]
    for data in queryset:
        labels.append(data.timestamp)
        number.append(data.player_count)
    playerdata={
        'labels': labels,
        'data': number,
    }
    print(labels)
    return JsonResponse(playerdata)
