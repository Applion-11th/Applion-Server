from re import T
from django.db import models
from django.conf import settings

class Application(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Application', primary_key=True)
    app1 = models.TextField(null=True)
    app2 = models.TextField(null=True)
    app3 = models.TextField(null=True)
    app4 = models.TextField(null=True)

    objects = models.Manager()

    def __str__(self):
        return str(self.user) + " application"