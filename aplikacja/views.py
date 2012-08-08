
# -*- coding: utf-8 -*-
from datetime import datetime
from django.contrib.comments import forms
from django.http import HttpResponseRedirect

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template.response import TemplateResponse
from django.views.generic.list_detail import object_list
from aplikacja.forms import OpinieForm
from aplikacja.models import Sala, Komentarz


def index(request):

    kategorie = Sala.objects.all()
    kontekst = {'kategorie': kategorie}
    return TemplateResponse(request, 'index.html', kontekst)

#class AddCommentForm(forms.ModelForm):
#    class Meta:
#        model = Comment
#
#    def opinie(request, slug):
#        kategorie = Kategorie.objects.get(slug=slug)
#        if request.POST:
#           data = request.POST.copy()
#           data['kategorie'] = kategorie.id
#           data['data'] = datetime.now()
#           form = AddCommentForm(data)
#           if form.is_valid():
#               form.save()
#        form = AddCommentForm()
#        render_to_response('opinie.html', {'kategorie':kategorie, 'form': form}, context_instance=RequestContext(request))



def opinie(request, id_kategorii):
    sala = Sala.objects.get(pk=id_kategorii)
    opinie = Komentarz.objects.filter(sala=sala)

    kontekst = {
        'nazwa_sali': sala.nazwa,
        'sala_pk': sala.pk,
        'opinie': opinie,
        'kto_jest_boss': 'Loczek'
    }

    return TemplateResponse(request, 'opinie.html', kontekst)
    #    kategorie = Kategorie.objects.all()
    #    nazwa = Kategorie.objects.get(id = 1)
    #    koment = Opinie.objects.all()
    #    komentarze = {'komentarze': koment}
    #    return TemplateResponse(request, 'opinie.html', komentarze, nazwa)

#def dodaj(request):
#    kategorie = Kategorie.objects.all()
#    komentarz = Opinie(opinia)
#    return TemplateResponse(request, 'dodaj.html')


def dodaj(request, id):
    if request.method == 'POST':
        form = OpinieForm(request.POST)
        if form.is_valid():
            opinia = Komentarz()
            opinia.tekst = form.cleaned_data['tekst']
            opinia.data = datetime.today()
            opinia.sala = Sala.objects.get(pk=id)
            opinia.save()

            return HttpResponseRedirect('/sukces/')
    else:
        form = OpinieForm()

    return TemplateResponse(request, 'dodaj.html', {'form': form})