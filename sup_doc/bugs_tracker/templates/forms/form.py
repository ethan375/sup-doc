from django import forms


class NewTicketForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500, widget=forms.Textarea())


class NewUserForm(forms.Form):
    name = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
