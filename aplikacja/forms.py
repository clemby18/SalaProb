from django import forms


class OpinieForm(forms.Form):
    tekst = forms.CharField()


