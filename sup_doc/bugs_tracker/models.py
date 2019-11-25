from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Ticket(models.Model):
    title = models.CharField(max_length=100)
    time_created = models.DateTimeField(timezone.now())
    description = models.CharField(max_length=500)
    submitters_name = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    assigned_dev = models.ForeignKey('BugUser', on_delete=models.CASCADE)
    completed_dev = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class BugUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tickets = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.title
