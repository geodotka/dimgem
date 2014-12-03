#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import patterns, include, url
from django.contrib import admin
from dimgem.views import ShowPostView


admin.autodiscover()


urlpatterns = patterns('dimgem.views',
    url(r'^$', 'home', name='home'),
    url(r'^dim/$', 'dimgem', {'template_name': 'dim.html'}, name='dim'),
    url(r'^gem/$', 'dimgem', {'template_name': 'gem.html'}, name='gem'),
    url(r'^dim/gramatyka/$',
        ShowPostView.as_view(template_name='gramatyka.html'),
        name='dim_grammar'),
    url(r'^gem/gramatyka/$',
        ShowPostView.as_view(template_name='gramatyka.html'),
        name='gem_grammar'),
    url(r'^dim/slownictwo/$', 'show_posts', name='vocabulary1'),
    url(r'^gem/slownictwo/$', 'show_posts', name='vocabulary2'),
    url(r'^dim/ciekawostki/$', 'show_posts', name='curiosity1'),
    url(r'^gem/ciekawostki/$', 'show_posts', name='curiosity2'),
    url(r'^dim/false_friends/$', 'show_posts', name='false_friends1'),
    url(r'^gem/false_friends/$', 'show_posts', name='false_friends2'),
    url(r'^szukaj/$', 'search', name='search'),
    url(r'^kontakt/$', 'contact', name='contact'),

    url(r'^admin/', include(admin.site.urls)),
)


