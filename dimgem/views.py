#!/usr/bin/env python
# encoding: utf-8

import datetime

from django.views.generic import ListView
from django.shortcuts import render

from dimgem.forms import SearchingForm
from dimgem.models import Category, Post, Vote


def home(request):
    return render(request, 'home.html')


def dimgem(request, template_name):
    votes = {}
    if request.method == 'GET' and request.GET.get('post-id') and \
            request.GET.get('vote'):
        votes = vote(request)
    context = {
        'posts': show_todays_posts(template_name.replace('.html', '')),
        'votes': votes,
    }
    return render(request, template_name, context)


def contact(request):
    return render(request, 'kontakt.html')


class ShowPostView(ListView):
    model = Post
    paginate_by = 10
    template_type = ''
    category_name = ''

    def get_context_data(self, **kwargs):
        votes = {}
        if self.request.method == "GET" and \
                self.request.GET.get('post-id') and \
                self.request.GET.get('vote'):
            votes = vote(self.request)
        context = {
            'posts': self.get_queryset(),
            'page': self.template_type,
            'votes': votes,
        }
        return super(ShowPostView, self).get_context_data(**context)

    def get_queryset(self):
        category = Category.objects.filter(name=self.category_name)
        dim = self.template_type == 'dim'
        posts = Post.objects.filter(dim=dim, categories=category).all()
        return posts


def vote(request):

    post_id = int(request.GET.get('post-id'))
    vote = False
    if request.GET.get('vote') == '1':
        vote = True
    elif request.GET.get('vote') == '0':
        vote = False
    ip_adress = request.META.get('HTTP_X_FORWARDED_FOR', '') or request.META.get('REMOTE_ADDR')
    post = Post.objects.get(pk=post_id)

    result = request.session.get('has_voted', False)
    if result:
        if post_id in result:
            return {
                'vote': False,
                'post_id': post_id,
            }
        else:
            result.append(post_id)
    else:
        result = [post_id]

    request.session['has_voted'] = result
    Vote.objects.create(ip=ip_adress, post=post, vote=vote)
    return {
        'vote': True,
        'post_id': post_id,
    }


def show_todays_posts(dimgem_type):
    today_date = datetime.datetime.now().date()
    dimgem = dimgem_type == 'dim'
    posts = Post.objects.filter(posted_date=today_date,
                                dim=dimgem).order_by('categories').all()
    return posts


def search(request):
    if request.method == 'POST':
        form = SearchingForm(request.POST)
        posts = {}
        if form.is_valid():
            word = form.cleaned_data['word']
            posts = Post.objects.filter(text__icontains=word)
            return render(request, 'search.html', {'form': form,
                                                  'posts': posts, 'word': word})
        # else:
        #     return render(request, 'search.html', {'form': form, 'error': True})
    form = SearchingForm()
    return render(request, 'search.html', {'form': form})
