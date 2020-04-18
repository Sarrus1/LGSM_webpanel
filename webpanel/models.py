from django.db import models
from servers.models import Server
from django_cron import CronJobBase, Schedule
from servers.models import Server

class PlayerCount(models.Model):
    timestamp = models.TextField()
    player_count = models.IntegerField()
    max_player = models.IntegerField()
    Name = models.ForeignKey(Server, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name