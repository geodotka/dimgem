#!/usr/bin/env python
# encoding: utf-8

from annoying.decorators import ajax_request

from ..forms import ReportMistakeToPost, AcceptNoteToPostForm, \
    RefuseNoteToPostForm
from ..models import Post


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
def change_post_text(request):
    post_id = request.POST['post_id']
    post_text = request.POST['post_text']
    result = {}
    if request.user.is_superuser:
        post = Post.objects.get(id=post_id)
        if post:
            post.old_text = post.text
            post.text = post_text
            post.save()
            result['success'] = True
            result['post_id'] = post_id
        else:
            result['success'] = False
            result['error'] = 'Coś poszło nie tak. Spróbuj jeszcze raz'
    else:
        result['success'] = False
        result['error'] = 'Nie masz uprawnień do zmiany treści posta.'
    return result
