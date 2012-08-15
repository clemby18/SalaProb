# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(u'Nazwa Sali', max_length=20)
    address = models.CharField(max_length=50, verbose_name='Adres Sali')
    acoustics = models.CharField(max_length=20, verbose_name='Akustyka Sali')
    price = models.FloatField(max_length=10, verbose_name='Cena Za Godzine')
    instruments = models.CharField(max_length=200, verbose_name='Dostepne Instrumenty')
    equipment = models.CharField(max_length=200, verbose_name='Dostepny Sprzet')

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
