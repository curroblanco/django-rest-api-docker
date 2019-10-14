from rest_framework import serializers

from .models import *


class SuperHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperHero
        fields = ('id', 'hero_name', 'gender', 'real_name', 'publisher')


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id', 'name', 'founder')
