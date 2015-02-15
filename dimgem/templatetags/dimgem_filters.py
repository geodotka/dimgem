#!/usr/bin/env python
# encoding: utf-8

import re

from django import template


register = template.Library()


@register.filter(name='color_searched_word')
def color_searched_word(value, arg):
    arg_list = [arg, arg.lower(), arg.upper(), arg.capitalize()]
    for argument in arg_list:
        value = re.sub(argument, '<span class="searched-word">{}</span>'
                       .format(argument), value)
    return value
