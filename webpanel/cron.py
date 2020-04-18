import a2s
from time import strftime
from servers.models import Server

def playercounter():
    for server in Server.objects.all():
        address = (server.IP, server.Port)
        playernumber=a2s.info(address, timeout=3.0, encoding=None).player_count
        maxplayer=a2s.info(address, timeout=3.0, encoding=None).max_players
        now = strftime("%H:%M:%S")
        serverstat=Server(timestamp=now, player_count=playernumber, max_player=maxplayer, Name=server.Name)
        serverstat.save()
