
from datetime import datetime
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.response import TemplateResponse
from rooms.forms import OpinionForm, CaptchaOpinionForm
from rooms.models import Room, Comment

def index(request):
    categories = Room.objects.all()
    form = AuthenticationForm(None, request.POST or None)
    user = form.get_user()
    context = {
        'categories': categories,
        'user': user,
        }
    return TemplateResponse(request, 'index.html', context)


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
    if request.user.is_authenticated():
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

                return HttpResponseRedirect('/index/')
        else:
            form = OpinionForm()

        return TemplateResponse(request, 'add_opinion.html', {'form': form})

    else:
        return HttpResponseRedirect('/c_add_opinion/1')


def c_add_opinion(request, id):

    if request.method == 'POST':
        form = CaptchaOpinionForm(request.POST)
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

            return HttpResponseRedirect('/index/')
    else:
        form = CaptchaOpinionForm()

    return TemplateResponse(request, 'add_opinion.html', {'form': form})


def some_view(request):
    if request.POST:
        form = CaptchaTestForm(request.POST)

        # Validate the form: the captcha field will automatically
        # check the input
        if form.is_valid():
            human = True
    else:
        form = CaptchaTestForm()

    return render_to_response('accounts/done.html',locals())
