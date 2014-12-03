#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import patterns, include, url
from django.contrib import admin
from dimgem.views import ShowPostView


admin.autodiscover()


urlpatterns = patterns('dimgem.views',
    url(r'^$', 'home', name='home'),
    url(r'^dim/$', 'dimgem',
        {'template_name': 'dim.html', 'template_type': 'dim'},
        name='dim'),
    url(r'^gem/$', 'dimgem',
        {'template_name': 'gem.html', 'template_type': 'gem'},
        name='gem'),
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
    url(r'^dim/ciekawostki/$',
        ShowPostView.as_view(template_name='ciekawostki.html',
                             template_type='dim', category_name='Ciekawostki'),
        name='dim_curiosities'),
    url(r'^gem/ciekawostki/$',
        ShowPostView.as_view(template_name='ciekawostki.html',
                             template_type='gem', category_name='Ciekawostki'),
        name='gem_curiosities'),
    url(r'^dim/false_friends/$',
        ShowPostView.as_view(template_name='false_friends.html',
                             template_type='dim',
                             category_name='False friends'),
        name='dim_false_friends'),
    url(r'^gem/false_friends/$',
        ShowPostView.as_view(template_name='false_friends.html',
                             template_type='gem',
                             category_name='False friends'),
        name='gem_false_friends'),
    url(r'^szukaj/$', 'search', name='search'),
    url(r'^kontakt/$', 'contact', name='contact'),

    url(r'^admin/', include(admin.site.urls)),
)


