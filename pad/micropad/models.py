from django.db import models
from django.utils.translation import ugettext_lazy as _
from boogie.rest import rest_api


@rest_api()
class File(models.Model):
    """
    Represents a file.
    """
    text = models.TextField()
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=140)
