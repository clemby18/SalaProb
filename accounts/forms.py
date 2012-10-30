# coding=utf-8
from django import forms
from django.contrib.auth import login, logout, authenticate, models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.template.response import TemplateResponse


#class RegisterForm(UserCreationForm):
#    first_name = forms.CharField(label=u'Imię')
#    last_name = forms.CharField(label=u'Nazwisko')
#    address = forms.CharField(label=u'Adres', required=False)
#
#
#    def save(self, commit=True):
#        user = super(UserCreationForm, self).save(commit=False)
#        user.first_name = self.cleaned_data["first_name"]
#        user.last_name = self.cleaned_data["last_name"]
#        print self.cleaned_data['address']
#        if commit:
#            user.save()
#        return user


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('/done/')
    else:
        form = UserCreationForm()
    return render_to_response('accounts/register.html', {'form': form, }, context_instance = RequestContext(request))


def login_view(request):
    form = AuthenticationForm(None, request.POST or None)

    if form.is_valid():
        login(request, form.get_user())
        next_page = request.GET.get('next')
        if next_page:
            return HttpResponseRedirect(next_page)

        return HttpResponseRedirect('/welcome/')

    context = {'form': form}
    return TemplateResponse(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/index/')


def done(request):
    return TemplateResponse(request, 'accounts/done.html')

def welcome(request):
    form = AuthenticationForm(None, request.POST or None)
    user = form.get_user()
    context = {'user': user}
    return TemplateResponse(request, 'accounts/welcome.html', context)

def users(request):
    all_users = User.objects.all()
    context = {'users': all_users}
    return TemplateResponse(request, 'accounts/users.html', context)

def test_view(request):
    return HttpResponse('To tylko test.<br/><a href="/">strona główna</a>')

test_view = login_required(test_view, login_url='/logowanie/')



