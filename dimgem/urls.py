#!/usr/bin/env python
# encoding: utf-8

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from dimgem.const import DIM, GEM
from dimgem.views import ShowPostView


admin.autodiscover()


urlpatterns = patterns('dimgem.views',
    url(r'^$', 'home', name='home'),
    url(r'^dim/$', 'dimgem',
        {'template_name': 'dim.html', 'template_type': DIM},
        name=DIM),
    url(r'^gem/$', 'dimgem',
        {'template_name': 'gem.html', 'template_type': GEM},
        name=GEM),
    url(r'^dim/gramatyka/$',
        ShowPostView.as_view(template_name='posts.html',
                             template_type=DIM, category_name='Gramatyka',
                             view_name='dim_grammar'),
        name='dim_grammar'),
    url(r'^gem/gramatyka/$',
        ShowPostView.as_view(template_name='posts.html',
                             template_type=GEM, category_name='Gramatyka',
                             view_name='gem_grammar'),
        name='gem_grammar'),
    url(r'^dim/slownictwo/$',
        ShowPostView.as_view(template_name='posts.html',
                             template_type=DIM, category_name='Słownictwo',
                             view_name='dim_vocabulary'),
        name='dim_vocabulary'),
    url(r'^gem/slownictwo/$',
        ShowPostView.as_view(template_name='posts.html',
                             template_type=GEM, category_name='Słownictwo',
                             view_name='gem_vocabulary'),
        name='gem_vocabulary'),
    url(r'^dim/ciekawostki/$',
        ShowPostView.as_view(template_name='posts.html',
                             template_type=DIM, category_name='Ciekawostki',
                             view_name='dim_curiosities'),
        name='dim_curiosities'),
    url(r'^gem/ciekawostki/$',
        ShowPostView.as_view(template_name='posts.html',
                             template_type=GEM, category_name='Ciekawostki',
                             view_name='gem_curiosities'),
        name='gem_curiosities'),
    url(r'^dim/false_friends/$',
        ShowPostView.as_view(template_name='posts.html',
                             template_type=DIM,
                             category_name='False friends',
                             view_name='dim_false_friends'),
        name='dim_false_friends'),
    url(r'^gem/false_friends/$',
        ShowPostView.as_view(template_name='posts.html',
                             template_type=GEM,
                             category_name='False friends',
                             view_name='gem_false_friends'),
        name='gem_false_friends'),
    url(r'^szukaj/$', 'search', name='search'),
    url(r'^kontakt/$', 'contact', name='contact'),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
