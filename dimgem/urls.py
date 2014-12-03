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
        ShowPostView.as_view(template_name='gramatyka.html',
                             template_type='dim', category_name='Gramatyka'),
        name='dim_grammar'),
    url(r'^gem/gramatyka/$',
        ShowPostView.as_view(template_name='gramatyka.html',
                             template_type='gem', category_name='Gramatyka'),
        name='gem_grammar'),
    url(r'^dim/slownictwo/$',
        ShowPostView.as_view(template_name='slownictwo.html',
                             template_type='dim', category_name='Słownictwo'),
        name='dim_vocabulary'),
    url(r'^gem/slownictwo/$',
        ShowPostView.as_view(template_name='slownictwo.html',
                             template_type='gem', category_name='Słownictwo'),
        name='gem_vocabulary'),
    url(r'^dim/ciekawostki/$', 'show_posts', name='curiosity1'),
    url(r'^gem/ciekawostki/$', 'show_posts', name='curiosity2'),
    url(r'^dim/false_friends/$', 'show_posts', name='false_friends1'),
    url(r'^gem/false_friends/$', 'show_posts', name='false_friends2'),
    url(r'^szukaj/$', 'search', name='search'),
    url(r'^kontakt/$', 'contact', name='contact'),

    url(r'^admin/', include(admin.site.urls)),
)


