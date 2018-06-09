from django.db import models
from django.utils.translation import ugettext_lazy as _
from boogie.rest import rest_api


@rest_api()
class File(models.Model):
    """
    Represents a file.
    """
    text = models.TextField()
    name = models.CharField(max_length=100)
    uri = models.CharField(max_length=140, unique=True, blank=True, null=True)
    folder = models.ForeignKey('Folder', null=True, blank=True, on_delete=models.CASCADE)


@rest_api()
class Folder(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('Folder', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    uri = models.CharField(max_length=140)
