from django import forms


class OpinionForm(forms.Form):
    text = forms.CharField()


class UserForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)