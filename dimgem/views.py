import datetime

from django import forms

from dimgem.models import Category, Post, Vote
from django.shortcuts import render

from dimgem.forms import SearchingForm


def home(request):
    page = request.META['PATH_INFO'][-4:-1]
    url = ''
    votes = {}
    if request.method == "GET" and request.GET.get('post-id') and request.GET.get('vote'):
        votes = vote(request)

    if page == 'dim':
        url = 'dim.html'
        context = {
            'posts': show_todays_posts('dim'),
            'votes': votes,
        }
    if page == 'gem':
        url = 'gem.html'
        context = {
            'posts': show_todays_posts('gem'),
            'votes': votes,
        }
    return render(request, url, context)


def contact(request):
    w = CalendarWidget()
    return render(request, 'kontakt.html', {'widget': w})


def show_posts(request):

    category_path = request.META['PATH_INFO']
    votes = {}
    if request.method == "GET" and request.GET.get('post-id') and request.GET.get('vote'):
        votes = vote(request)

    page = ''
    url = ''
    category = None
    if category_path.endswith('gramatyka/'):
        page = request.META['PATH_INFO'][-14:-11]
        url = 'gramatyka.html'
        category = Category.objects.filter(name='Gramatyka')
    elif category_path.endswith('slownictwo/'):
        page = request.META['PATH_INFO'][-15:-12]
        url = 'slownictwo.html'
        category = Category.objects.filter(name='Słownictwo')
    elif category_path.endswith('ciekawostki/'):
        page = request.META['PATH_INFO'][-16:-13]
        url = 'ciekawostki.html'
        category = Category.objects.filter(name='Ciekawostki')
    elif category_path.endswith('false_friends/'):
        page = request.META['PATH_INFO'][-18:-15]
        url = 'false_friends.html'
        category = Category.objects.filter(name='False friends')

    dim = True if page == 'dim' else False
    posts = Post.objects.filter(dim=dim, categories=category).all()
    context = {
        'posts': posts,
        'page': page,
        'votes': votes,
    }
    return render(request, url, context)


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
    dimgem = True if dimgem_type == 'dim' else False
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


class CalendarWidget(forms.TextInput):
    class Media:
        css = {
            'all': ('pretty.css',)
        }
        js = ('animations.js', 'actions.js')