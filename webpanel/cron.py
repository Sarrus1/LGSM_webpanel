import a2s
from time import strftime
from servers.models import Server
from .models import PlayerCount

def playercounter():
    labels = []
    number = []
    for server in Server.objects.all():
        address = (server.IP, server.Port)
        query = a2s.info(address, timeout=3.0, encoding=None)
        playernumber = query.player_count
        maxplayer = query.max_players
        now = strftime("%H:%M")
        serverstat = PlayerCount(timestamp=now, player_count=playernumber, max_player=maxplayer, Name=server)
        serverstat.save()
        queryset = PlayerCount.objects.all()[:]
        for data in queryset:
            labels.append(data.timestamp)
            number.append(data.player_count)
        if len(labels) >= 288:
            Name_id = Server.objects.get(Name=server.Name)
            queryset = PlayerCount.objects.filter(Name=Name_id)[:]
            to_delete = PlayerCount.objects.values()[:1].get()
            PlayerCount.objects.filter(id=to_delete['id']).delete()

