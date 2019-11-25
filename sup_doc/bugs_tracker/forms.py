from django import forms
from bugs_tracker.models import Ticket, BugUser
from django.contrib.auth.models import User


class NewTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'title',
            'description'
        ]


class NewUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]
