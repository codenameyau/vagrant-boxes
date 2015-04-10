"""
Description:
This app contains core application models that are meant
to be reused throughout an entire project.
"""
from django.db import models

class TimeStampedModel(models.Model):
    """
    An abstract class model that provides the auto-updating
    fields: (1) created and (2) modified.
    """
    created  = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
