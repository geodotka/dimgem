#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import patterns, url


urlpatterns = patterns(
    'dimgem.views.api',
    url(r'^report_mistake_to_post$', 'report_mistake_to_post',
        name='report_mistake_to_post'),
)