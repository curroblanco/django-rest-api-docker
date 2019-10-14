from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^superhero/$', views.SuperHeroList.as_view()),
    url(r'^superhero/$', views.SuperHeroInsert.as_view()),
    url(r'^superhero/(?P<pk>[0-9]+)/$', views.SuperHeroDetail.as_view()),
    url(r'^superhero/(?P<pk>[0-9]+)/$', views.SuperHeroDelete.as_view()),
    url(r'^publisher/$', views.PublisherList.as_view()),
    url(r'^publisher/(?P<pk>[0-9]+)/$', views.PublisherDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
