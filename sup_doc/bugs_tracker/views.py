from django.shortcuts import render
from . models import BugUser, Ticket
from django.contrib.auth.models import User
from . forms import NewUserForm, NewTicketForm
from django.utils import timezone


def index(request):
    tickets = Ticket.objects.all()
    context = {'tickets': tickets}

    return render(request, 'index.html', context)


def new_ticket(request):
    # need to import the form and instantiate and all that good stuff
    if request.method == 'POST':
        form = NewTicketForm(request.POST)

        if form.is_valid():
            form_data = form.cleaned_data
        
        Ticket.objects.create(
            title = form_data['title'],
            time_created = timezone.now(),
            description = form_data['description'],
            submitters_name = request.user.name,
            status = 'New',
            assigned_dev = 'None',
            completed_dev = 'None'
        )

        return render(request, 'dev.html')
    else:
        form = NewTicketForm()
        context = {'form': form}

        return render(request, 'ticket/new_ticket.html', context)


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
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form_data = form.cleaned_data
            user = form.save()

            BugUser.objects.create(
                name = form_data['username'],
                user = user
            )
            
            return render(request, 'dev.html')
    else:
        form = NewUserForm()
        context = {'form': form}

        return render(request, 'auth/new_user.html', context)
