from django import forms
from captcha.fields import CaptchaField

class OpinionForm(forms.Form):
    text = forms.CharField()


class CaptchaOpinionForm(forms.Form):
    text = forms.CharField()
    captcha = CaptchaField()