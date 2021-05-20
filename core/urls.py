from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^artifacts/$', views.artifacts, name='artifacts'),
    url(r'^artifacts/details/(?P<artifactName>.+)/?$', views.artifactDetails, name='artifactDetails'),
    url(r'^artifacts/create/$', views.artifactNew, name='artifactNew'),
    url(r'^endpoints/$', views.endpoints, name='endpoints'),
    url(r'^endpoints/details/(?P<endpointName>.+)/?$', views.endpointDetails, name='endpointDetails'),
    url(r'^endpoints/create/$', views.endpointNew, name='endpointNew'),
    url(r'^compromise/$', views.compromise, name='compromise'),
    url(r'^compromise/details/(?P<compromiseId>[0-9]+)/?$', views.compromiseDetails, name='compromiseDetails'),
    url(r'^compromise/create/$', views.compromiseNew, name='compromiseNew'),
    url(r'^actors/$', views.actors, name='actors'),
    url(r'^actors/details/(?P<actorName>.+)/?$', views.actorDetails, name='actorDetails'),
    url(r'^actors/create/$', views.actorNew, name='actorNew'),
    url(r'^areas/$', views.areas, name='areas'),
    url(r'^areas/details/(?P<areaName>.+)/?$', views.areaDetails, name='areaDetails'),
    url(r'^areas/create/$', views.areaNew, name='areaNew'),
    url(r'^users/$', views.users, name='users'),
    url(r'^users/details/(?P<accountName>.+)/?$', views.userDetails, name='userDetails'),
    url(r'^users/create/$', views.userNew, name='userNew'),
    url(r'^search/$', views.search),
]
