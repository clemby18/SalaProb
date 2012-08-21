# -*- coding: utf-8 -*-

from django.db import models

class Room(models.Model):
    name = models.CharField(u'Nazwa Sali', max_length=20)
    address = models.CharField(u'Adres Sali',max_length=50)
    acoustics = models.CharField(u'Akustyka Sali', max_length=20)
    price = models.FloatField(u'Cena Za Godzine', max_length=10)
    instruments = models.CharField(u'Dostepne Instrumenty', max_length=200)
    equipment = models.CharField(u'Dostepny Sprzet', max_length=200)

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"

    def __unicode__(self):
        return self.name


class Comment(models.Model):
    room = models.ForeignKey(Room, verbose_name='Sala')
    text = models.TextField(verbose_name='Opinie')
    date = models.DateTimeField(verbose_name='Data dodania')


    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
    def __str__(self):
        return str(self.room)
    def __unicode__(self):
        return unicode(self.room)
