# -*- coding: utf-8 -*-
from django.contrib import admin
from rooms.models import Comment, Room


admin.site.register(Room)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('room', 'text', 'date')
    list_filter = ['date']

admin.site.register(Comment, CommentAdmin)

#admin.site.register(User)