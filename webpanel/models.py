from django.db import models

class Server(models.Model):
    Name = models.CharField(max_length=100)
    IP = models.CharField(max_length=15)
    Port = models.CharField(max_length=5)
    Path = models.CharField(max_length=200)

    def __str__(self):
        return self.Name