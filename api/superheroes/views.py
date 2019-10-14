from .models import SuperHero, Publisher
from .serializers import SuperHeroSerializer, PublisherSerializer
from rest_framework import generics


class SuperHeroList(generics.ListCreateAPIView):
    queryset = SuperHero.objects.all()
    serializer_class = SuperHeroSerializer


class SuperHeroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SuperHero.objects.all()
    serializer_class = SuperHeroSerializer


class SuperHeroInsert(generics.CreateAPIView):
    queryset = SuperHero.objects.all()
    serializer_class = SuperHeroSerializer


class SuperHeroUpdate(generics.RetrieveUpdateAPIView):
    queryset = SuperHero.objects.all()
    serializer_class = SuperHeroSerializer


class SuperHeroDelete(generics.DestroyAPIView):
    queryset = SuperHero.objects.all()
    serializer_class = SuperHeroSerializer


class PublisherList(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherInsert(generics.CreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherUpdate(generics.RetrieveUpdateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherDelete(generics.DestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer