#!/usr/bin/env python
# encoding: utf-8

import re

from django import template


register = template.Library()


@register.filter(name='color_searched_word')
def color_searched_word(value, arg):
    word = arg[0]
    is_whole_word = arg[1]
    if is_whole_word:
        pattern = re.compile(r'\b(' + word + r')\b', flags=(re.I | re.U))
    else:
        pattern = re.compile(r'(' + word + r')', flags=(re.I | re.U))
    repl = r'<span class="searched-word">\1</span>'

    return re.sub(pattern, repl, value)
