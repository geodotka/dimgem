#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import patterns, url


urlpatterns = patterns(
    'dimgem.views.api',
    url(r'^report_mistake_to_post$', 'report_mistake_to_post',
        name='report_mistake_to_post'),
    url(r'^accept_note_to_post$', 'accept_note_to_post',
        name='accept_note_to_post'),
    url(r'^refuse_note_to_post$', 'refuse_note_to_post',
        name='refuse_note_to_post'),
    url(r'^show_newest_post', 'show_newest_post',
        name='show_newest_post'),
)
