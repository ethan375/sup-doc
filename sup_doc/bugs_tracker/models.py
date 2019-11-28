from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    title = models.CharField(max_length=100)
    time_created = models.DateTimeField()
    description = models.CharField(max_length=500)
    submitters_name = models.ForeignKey('BugUser', on_delete=models.CASCADE, related_name="ticket_submitters_name")
    # status is going to be represented by numbers to make ordering the query sets easier
    # 1 = new, 2 = in progress, 3 = done, 4 = invalid
    status = models.IntegerField()
    assigned_dev = models.ForeignKey('BugUser', on_delete=models.CASCADE, null=True, blank=True)
    completed_dev = models.ForeignKey('BugUser', on_delete=models.CASCADE, null=True, blank=True, related_name="ticket_completed_dev")

    def __str__(self):
        return self.title


class BugUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tickets = models.ManyToManyField(Ticket)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
