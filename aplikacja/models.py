# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Sala(models.Model):
    nazwa = models.CharField(u'Nazwa Sali', max_length=20)
    adres = models.CharField(max_length=50, verbose_name='Adres Sali')
    akustyka = models.CharField(max_length=20, verbose_name='Akustyka Sali')
    cena = models.FloatField(max_length=10, verbose_name='Cena Za Godzine')
    instrumenty = models.CharField(max_length=200, verbose_name='Dostepne Instrumenty')
    sprzet = models.CharField(max_length=200, verbose_name='Dostepny Sprzet')
#    slug = models.SlugField(max_length=255, unique=True, verbose_name='Odnośnik')

    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Sale"

    def __unicode__(self):
        return self.nazwa

    def get_absolute_url(self):
        return '/aplikacja/' + self.slug + '/'


class Komentarz(models.Model):
    sala = models.ForeignKey(Sala, verbose_name='Sala')
    tekst = models.TextField(verbose_name='Opinie')
    data = models.DateTimeField(verbose_name='Data dodania')


    class Meta:
        verbose_name = "Komentarz"
        verbose_name_plural = "Komentarze"
    def __str__(self):
        return str(self.sala)
    def __unicode__(self):
        return unicode(self.sala)
