# -*- coding: utf-8 -*-
from django.contrib import admin
from aplikacja.models import Komentarz, Sala


#class cosiek(admin.ModelAdmin):
#    list_display =


admin.site.register(Sala)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('sala', 'tekst', 'data')
    list_filter = ['data']

admin.site.register(Komentarz, CommentAdmin)
