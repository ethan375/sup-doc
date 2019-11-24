from django.shortcuts import render
from . models import BugUser, Ticket


def index(request):
    tickets = Ticket.objects.all()
    context = {'tickets': tickets}

    return render(request, 'index.html', context)
