from django.shortcuts import render
from . models import BugUser, Ticket


def index(request):
    tickets = Ticket.objects.all()
    context = {'tickets': tickets}

    return render(request, 'index.html', context)


def new_ticket(request):
    # need to import the form and instantiate and all that good stuff
    if request.method == 'POST':
        pass
    else:
        pass


def edit_ticket(request, ticket_id):
    # going to need to handle the form and the put/patch request, whatever it is going to be
    pass


def ticket_detail(request, ticket_id):
    ticket = Ticket.objects.filter(id=ticket_id)
    context = {'ticket', ticket}

    return render(request, 'ticket/ticket_detail.html', context)


def tickets_by_user(request, user_id):
    user = BugUser.objects.filter(id=user_id)
    context = {'user': user}

    return render(request, 'ticket/ticket_by_user.html', context)


def login_user(request):
    # going to handle the fun of loggin in and all that shit 
    pass


def new_user(request):
    # going to register new users and shit 
    pass
