from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('dimgem.views',
    url(r'^$', 'home', name='home'),
    url(r'^dim/$', 'dim', name='dim'),
    url(r'^gem/$', 'gem', name='gem'),
    url(r'^dim/gramatyka/$', 'show_posts', name='gramma1'),
    url(r'^gem/gramatyka/$', 'show_posts', name='gramma2'),
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
