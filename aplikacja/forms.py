from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class OpinionForm(forms.Form):
    text = forms.CharField()


class UserForm(forms.Form):
    first_name = forms.CharField(max_length=20, )
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)


#    def validator_for_first_name(self):
#        data_first_name = self.cleaned_data['first_name']
#
#        return data_first_name
#
#    def validate_email(email):
#        try:
#            validate_email(email)
#            return True
#        except ValidationError:
#            return False


