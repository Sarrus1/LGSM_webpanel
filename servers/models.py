from django.db import models

class Server(models.Model):
    Name = models.CharField(max_length=100)
    IP = models.GenericIPAddressField()
    Port = models.IntegerField()
    Path = models.CharField(max_length=200)

    def __str__(self):
        return str(self.Name) if self.Name else ''