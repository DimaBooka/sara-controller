#!/usr/bin/env python3

EN = 'en-US'
RU = 'ru-RU'

languages = {
    'en': EN,
    'ru': RU
}

language = 'en-US'


def get_language():
    return language


def set_language(ln):
    if ln in languages:
        global language
        language = languages[ln]
    else:
        print("Language '%s' is not supported by Sara" % ln)

    return language
