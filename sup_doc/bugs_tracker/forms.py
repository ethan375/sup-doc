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


class EditTicketForm(forms.ModelForm):
    Mark_complete = forms.CharField(widget=forms.CheckboxInput)
    Invalidate_ticket = forms.CharField(widget=forms.CheckboxInput)

    class Meta:
        model = Ticket
        fields = [
            'title',
            'description',
            'assigned_dev'
        ]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

