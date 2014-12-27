#!/usr/bin/env python
# encoding: utf-8
from annoying.decorators import ajax_request
from dimgem.forms import ReportMistakeToPost


@ajax_request
def report_mistake_to_post(request):
    """
    function add note to post to database
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
