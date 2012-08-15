
# -*- coding: utf-8 -*-
from datetime import datetime
from django.contrib.comments import forms
from django.http import HttpResponseRedirect

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template.response import TemplateResponse
from django.views.generic.list_detail import object_list
from aplikacja.forms import OpinionForm
from aplikacja.models import Room, Comment


def index(request):

    categories = Room.objects.all()
    context = {'categories': categories}
    return TemplateResponse(request, 'index.html', context)


def opinions(request, id_Category):
    room = Room.objects.get(pk=id_Category)
    opinions = Comment.objects.filter(room=room)

    context = {
        'room_name': room.name,
        'room_pk': room.pk,
        'opinions': opinions,
    }
    return TemplateResponse(request, 'opinions.html', context)


def addOpinion(request, id):
    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            opinion = Comment()
            opinion.text = form.cleaned_data['text']
            opinion.date = datetime.today()
            opinion.room = Room.objects.get(pk=id)
            opinion.save()

            return HttpResponseRedirect('/success/')
    else:
        form = OpinionForm()

    return TemplateResponse(request, 'addOpinion.html', {'form': form})