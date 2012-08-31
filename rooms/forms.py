from django import forms

class OpinionForm(forms.Form):
    text = forms.CharField()