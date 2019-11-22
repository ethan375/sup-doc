from django.db import models
from django.utils import timezone


class Bug(models.Model):
    title = models.CharField(max_length=100)
    time_created = models.DateTimeField(timezone.now())
    description = models.CharField(max_length=500)
    submitters_name = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    assigned_dev = models.CharField(max_length=100)
    completed_dev = models.CharField(max_length=100)

    def __str__(self):
        return self.title