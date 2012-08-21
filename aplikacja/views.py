
# -*- coding: utf-8 -*-
from datetime import datetime
from django.contrib.comments import forms
from django.http import HttpResponseRedirect

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template.response import TemplateResponse
from django.views.generic.list_detail import object_list
from aplikacja.forms import OpinionForm, UserForm
from aplikacja.models import Room, Comment, User


def index(request):
    categories = Room.objects.all()
    context = {'categories': categories}
    return TemplateResponse(request, 'index.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = User()
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.username = form.cleaned_data['username']
            user.password = form.cleaned_data['password']
            user.save()

            return HttpResponseRedirect('/success/')
    else:
        form = UserForm()

    return TemplateResponse(request, 'registration.html', {'form': form})


def login(request):
    return TemplateResponse(request, 'login.html')


def opinions(request, id_category):
    room = Room.objects.get(pk=id_category)
    opinions = Comment.objects.filter(room=room)

    context = {
        'room_name': room.name,
        'room_pk': room.pk,
        'opinions': opinions,
    }
    return TemplateResponse(request, 'opinions.html', context)


def add_opinion(request, id):
    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            opinion = Comment()
            opinion.text = form.cleaned_data['text']
            opinion.date = datetime.today()
            opinion.room = Room.objects.get(pk=id)

            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')

            opinion.ip = ip
            opinion.save()

            return HttpResponseRedirect('/success/')
    else:
        form = OpinionForm()

    return TemplateResponse(request, 'add_opinion.html', {'form': form})


def success(request):
    return TemplateResponse(request, 'success.html')


