#!/usr/bin/env python
# encoding: utf-8

from annoying.decorators import ajax_request
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
