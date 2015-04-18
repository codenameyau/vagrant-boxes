"""
Description:
This app contains core application models that are meant
to be reused throughout an entire project.
"""
from django.db import models

class TimeStampedModel(models.Model):
    """
    Abstract model that provides the date created and modified fields.
    """
    created  = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
