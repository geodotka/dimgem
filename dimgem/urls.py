from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^dim/$', 'dimgem.views.home', name='home1'),
    url(r'^gem/$', 'dimgem.views.home', name='home2'),
    url(r'^dim/gramatyka/$', 'dimgem.views.show_posts', name='gramma1'),
    url(r'^gem/gramatyka/$', 'dimgem.views.show_posts', name='gramma2'),
    url(r'^dim/slownictwo/$', 'dimgem.views.show_posts', name='vocabulary1'),
    url(r'^gem/slownictwo/$', 'dimgem.views.show_posts', name='vocabulary2'),
    url(r'^dim/ciekawostki/$', 'dimgem.views.show_posts', name='curiosity1'),
    url(r'^gem/ciekawostki/$', 'dimgem.views.show_posts', name='curiosity2'),
    url(r'^dim/false_friends/$', 'dimgem.views.show_posts', name='false_friends1'),
    url(r'^gem/false_friends/$', 'dimgem.views.show_posts', name='false_friends2'),
    url(r'^szukaj/$', 'dimgem.views.search', name='search'),
    url(r'^kontakt/$', 'dimgem.views.contact', name='contact'),

    url(r'^admin/', include(admin.site.urls)),
)
