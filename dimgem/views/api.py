#!/usr/bin/env python
# encoding: utf-8

from annoying.decorators import ajax_request
from dimgem.const import DIM

from ..models import Post
from ..forms import ReportMistakeToPost, AcceptNoteToPostForm, \
    RefuseNoteToPostForm


@ajax_request
def report_mistake_to_post(request):
    """
    function adds note to post to database
    """
    post_id = request.POST['post_id']
    user_id = request.POST['user_id']

    result = {'post_id': post_id}
    form = ReportMistakeToPost(request.POST)
    if form.is_valid():
        form.cleaned_data['post_id'] = post_id
        if user_id:
            form.cleaned_data['user_id'] = user_id
        form.save()
        result['success'] = True
    else:
        result['success'] = False

    return result


@ajax_request
def accept_note_to_post(request):
    """
    function accepts note to post and changes text of post in database
    """
    form = AcceptNoteToPostForm(request.POST)
    result = get_result_of_accepting_or_refusing_note_to_post(request, form)
    return result


@ajax_request
def refuse_note_to_post(request):
    """
    function refuses note to post and changes refusal_reason
    of noteToPost in database
    """
    form = RefuseNoteToPostForm(request.POST)
    result = get_result_of_accepting_or_refusing_note_to_post(request, form)
    return result


def get_result_of_accepting_or_refusing_note_to_post(request, form):
    note_id = request.POST['note_id']
    result = {'note_id': note_id}
    if form.is_valid():
        form.cleaned_data['note_id'] = note_id
        form.cleaned_data['superuser'] = request.user
        form.save()
        result['success'] = True
    else:
        result['success'] = False
        result['errors'] = form.errors

    return result


@ajax_request
def show_newest_post(request):
    category = request.POST.get('category')
    dim = request.POST.get('dim')
    dim = True if dim == DIM else False
    try:
        post = Post.objects.filter(is_approved=True,
            dim=dim, categories__name=category).order_by('-id')[0]
    except IndexError:
        post = None
    if post:
        return {
            'date': str(post.posted_date.strftime('%d.%m.%Y')),
            'author': post.author,
            'url': post.url,
            'title': post.title,
            'text': post.text,
            'success': True
        }
    else:
        return {'success': False}
