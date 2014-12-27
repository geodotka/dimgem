#!/usr/bin/env python
# encoding: utf-8

import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from django.views.generic import ListView
from django.shortcuts import render, redirect

from dimgem.const import DIM
from dimgem.forms import SearchingForm, RegisterForm, LoginForm,\
    AddNewPostForm, ReportMistakeToPost
from dimgem.models import Category, Post, Vote


def home(request):
    return render(request, 'home.html')


def dimgem(request, view_name):
    votes = {}
    if request.method == 'GET' and request.GET.get('post-id') and \
            request.GET.get('vote'):
        votes = vote(request)
    context = {
        'posts': show_todays_posts(view_name),
        'view_name': view_name,
        'votes': votes,
    }
    return render(request, 'dimgem.html', context)


def contact(request):
    return render(request, 'contact.html')


class ShowPostView(ListView):
    model = Post
    paginate_by = 10
    template_type = ''
    category_name = ''
    view_name = ''
    # set name of queryset
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        votes = {}
        if self.request.method == "GET" and \
                self.request.GET.get('post-id') and \
                self.request.GET.get('vote'):
            votes = vote(self.request)
        form = ReportMistakeToPost()
        context = {
            'template_type': self.template_type,
            'category_name': self.category_name,
            'view_name': self.view_name,
            'votes': votes,
            'form': form,
        }
        return super(ShowPostView, self).get_context_data(**context)

    def get_queryset(self):
        category = Category.objects.filter(name=self.category_name)
        dim = self.template_type == DIM
        posts = Post.objects.filter(
            dim=dim, categories=category, is_approved=True).all()
        return posts


def vote(request):

    post_id = int(request.GET.get('post-id'))
    vote = False
    if request.GET.get('vote') == '1':
        vote = True
    elif request.GET.get('vote') == '0':
        vote = False
    ip_adress = request.META.get('HTTP_X_FORWARDED_FOR','') or \
                request.META.get('REMOTE_ADDR')
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
    dimgem = dimgem_type == DIM
    posts = Post.objects.filter(
        posted_date=today_date, dim=dimgem, is_approved=True)\
        .order_by('categories').all()
    return posts


def search(request):
    form = SearchingForm(request.POST or None)

    if form.is_valid():
        word = form.cleaned_data['word']
        posts = Post.objects.filter(text__icontains=word, is_approved=True)
        return render(request, 'search.html', {'form': form,
                                               'posts': posts,
                                               'word': word})

    return render(request, 'search.html', {'form': form})


def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = request.POST.get('login')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()
        login(request, user)

        redirect_url = reverse('home')
        return redirect(redirect_url)

    return render(request, 'registration.html', {'form': form})


def log_in(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('login')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        # TODO: nie podoba mi się takie coś, ale nie chcę w metodzie clean
        # drugi raz authenticate usera
        if user is None:
            context = {
                'form': form,
                'error': u'Błędne hasło',
            }
            return render(request, 'login.html', context)
        login(request, user)
        next_page = request.GET.get('next', None)
        if next_page == '/logout/':
            next_page = '/'
        return redirect(next_page or '/')

    return render(request, 'login.html', {'form': form})


def log_out(request):
    logout(request)
    return render(request, 'logout.html')


@login_required
def add_post(request):
    form = AddNewPostForm(request.POST or None)

    user = request.user.username
    if user == 'geodotka':
        author = 'DIM'
    elif user == 'jerzyt':
        author = 'GEM'
    else:
        author = user

    if form.is_valid():
        data_dict = {
            'title': form.cleaned_data['title'],
            'posted_date': datetime.datetime.now().date(),
            'author': author,
            'text': form.cleaned_data['text'],
            'dim': form.cleaned_data['dim'],
            'categories': form.cleaned_data['categories'],
            'picture': request.FILES['picture'],
            'is_approved': False,
        }
        iter_dict = data_dict.copy()
        for k, v in iter_dict.items():
            if v is None or v == '':
                del data_dict[k]

        post = Post.objects.create(**data_dict)
        redirect_url = reverse('waiting_room')
        return redirect(redirect_url)
    else:
        return render(request, 'add_post.html', {'form': form})


def waiting_room(request):
    """
    keeps the posts that are not approved by superuser
    """
    posts = Post.objects.filter(is_approved=False)
    curiosities_id = Category.objects.get(name='Ciekawostki').id
    vocabulary_id = Category.objects.get(name='Słownictwo').id
    grammar_id = Category.objects.get(name='Gramatyka').id
    false_friends_id = Category.objects.get(name='False friends').id
    context = {
        'posts_dim_curiosities': posts.filter(dim=True,
                                              categories=curiosities_id),
        'posts_dim_vocabulary': posts.filter(dim=True,
                                             categories=vocabulary_id),
        'posts_dim_grammar': posts.filter(dim=True, categories=grammar_id),
        'posts_dim_false_friends': posts.filter(dim=True,
                                                categories=false_friends_id),
        'posts_gem_curiosities': posts.filter(dim=False,
                                              categories=curiosities_id),
        'posts_gem_vocabulary': posts.filter(dim=False,
                                             categories=vocabulary_id),
        'posts_gem_grammar': posts.filter(dim=False, categories=grammar_id),
        'posts_gem_false_friends': posts.filter(dim=False,
                                                categories=false_friends_id),
    }
    return render(request, 'waiting_room.html', context)