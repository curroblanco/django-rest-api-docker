from datetime import datetime

from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    founder = models.CharField(max_length=100, blank=True, default='')
    date = models.DateField(blank=True, default=datetime.now)

    class Meta:
        ordering = ('name',)


class SuperHero(models.Model):
    hero_name = models.CharField(max_length=100, blank=True, default='')
    gender = models.CharField(max_length=1, blank=True, default='M')
    real_name = models.CharField(max_length=100, blank=True, default='')
    publisher = models.ForeignKey(Publisher, on_delete='cascade')

    class Meta:
        ordering = ('hero_name',)
