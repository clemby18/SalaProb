# -*- coding: utf-8 -*-

from django.db import models

class Room(models.Model):
    name = models.CharField(u'Nazwa sali', max_length=20)
    address = models.CharField(u'Adres sali',max_length=50)
    acoustics = models.CharField(u'Akustyka sali', max_length=20)
    price = models.FloatField(u'Cena za godzine', max_length=10)
    instruments = models.CharField(u'Dostępne instrumenty', max_length=200)
    equipment = models.CharField(u'Dostępny sprzęt', max_length=200)

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"

    def __unicode__(self):
        return self.name


class Comment(models.Model):
    room = models.ForeignKey(Room, verbose_name=u'Sala')
    text = models.TextField(verbose_name=u'Opinie')
    date = models.DateTimeField(verbose_name=u'Data dodania')
    ip = models.IPAddressField(verbose_name=u'Adres ip')


    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
    def __str__(self):
        return str(self.room)
    def __unicode__(self):
        return unicode(self.room)
