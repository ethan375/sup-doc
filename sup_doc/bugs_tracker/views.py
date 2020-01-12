from django.shortcuts import render, redirect
from . models import BugUser, Ticket
from . forms import NewUserForm, NewTicketForm, LoginForm, EditTicketForm
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def landing(request):
    return render(request, 'landing.html')


def index(request):
    tickets = Ticket.objects.all()

    new = [t for t in tickets if t.status == 'New']
    in_progress = [t for t in tickets if t.status == "In progress"]
    completed = [t for t in tickets if t.status == "Completed"]
    invalid = [t for t in tickets if t.status == "Invalid"]
    sorted_tickets = new + in_progress + completed + invalid
    context = {"tickets": sorted_tickets}

    return render(request, 'index.html', context)


def new_ticket(request):
    # need to import the form and instantiate and all that good stuff
    if request.method == 'POST':
        form = NewTicketForm(request.POST)

        if form.is_valid():
            form_data = form.cleaned_data

            Ticket.objects.create(
                title=form_data['title'],
                time_created=timezone.now(),
                description=form_data['description'],
                submitters_name=request.user.buguser,
                status='New',
                assigned_dev=None,
                completed_dev=None
            )

        return redirect('/bugs-tracker/ticket/all')
    else:
        form = NewTicketForm()
        context = {'form': form}

        return render(request, 'ticket/new_ticket.html', context)


def edit_ticket(request, ticket_id):
    ticket = Ticket.objects.filter(id=ticket_id).first()
    if request.method == 'POST':
        form = EditTicketForm(request.POST)

        if form.is_valid():
            form = form.cleaned_data

            if form['Invalidate_ticket'] == 'True':
                ticket.status = 'Invalid'
                ticket.completed_dev = ticket.assigned_dev
                ticket.assigned_dev = None
                ticket.save()

            elif form['Mark_complete'] == 'True':
                ticket.status = 'Completed'
                ticket.completed_dev = ticket.assigned_dev
                ticket.assigned_dev = None
                ticket.save()

            elif form['assigned_dev'] is not None and ticket.assigned_dev == None:
                ticket.assigned_dev = form['assigned_dev']
                ticket.status = "In progress"
                ticket.save()

        return redirect('/bugs-tracker/ticket/{}'.format(ticket.id))
     
    else:
        form = EditTicketForm(instance=ticket)
        context = {'form': form}

        return render(request, 'ticket/edit_ticket.html', context)


def ticket_detail(request, ticket_id):
    ticket = Ticket.objects.filter(id=ticket_id).first()
    context = {'ticket': ticket}

    return render(request, 'ticket/ticket_detail.html', context)


def tickets_by_user(request, user_id):
    user = BugUser.objects.filter(id=user_id).first()

    current_tickets = Ticket.objects.filter(submitters_name=user)
    filed = Ticket.objects.filter(submitters_name=user)
    completed = Ticket.objects.filter(completed_dev=user)
    merged_queries = current_tickets | filed | completed

    context = {'tickets': merged_queries}

    return render(request, 'ticket/tickets_by_user.html', context)


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            form_data = form.cleaned_data

            user = authenticate(
                username=form_data['username'],
                password=form_data['password']
            )

            if user is not None:
                login(request, user)
                return redirect('/bugs-tracker/ticket/all')
            else:
                form = LoginForm()
                context = {
                    'error': "incorrect username or password ", 
                    'form': form
                }
                return render(request, 'auth/login.html', context)
    else:
        form = LoginForm()
        context = {'form': form}

        return render(request, 'auth/login.html', context)


def new_user(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form_data = form.cleaned_data

            user = User.objects.create_user(
                username=form_data['username'],
                password=form_data['password']
            )

            BugUser.objects.create(
                name=form_data['username'],
                user=user
            )
            
            return render(request, 'index.html')
    else:
        form = NewUserForm()
        context = {'form': form}

        return render(request, 'auth/new_user.html', context)


def all_users(request):
    users = BugUser.objects.all()
    context = {"users": users}
    return render(request, 'all_users.html', context)