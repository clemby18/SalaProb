# coding=utf-8
from django import forms
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.template.response import TemplateResponse

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label=u'Imię')
    last_name = forms.CharField(label=u'Nazwisko')
    address = forms.CharField(label=u'Adres', required=False)


    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        print self.cleaned_data['address']
        if commit:
            user.save()
        return user


def register(request):
    form = RegisterForm(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        form.save()
        return HttpResponseRedirect ('/done/')

    return render_to_response('accounts/register.html', context, context_instance = RequestContext(request))


def login_view(request):
    form = AuthenticationForm(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        login(request, form.get_user())
        return TemplateResponse(request, 'index.html')

    return render_to_response('accounts/login.html', context, context_instance = RequestContext(request))


def done(request):
    return TemplateResponse(request, 'accounts/done.html')

