from django.db import models


class Links(models.Model):
    link = models.CharField(max_length=20000)
    uuid = models.CharField(max_length=10)