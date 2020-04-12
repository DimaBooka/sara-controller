#!/usr/bin/env python3

from sara.language import EN, RU, UA

SARA_ACTIVATOR = 'SARA ACTIVATOR'

languages = {
    EN: {
        SARA_ACTIVATOR: 'hey sara',
    },
    RU: {
        SARA_ACTIVATOR: 'привет сара',
    },
    UA: {
        SARA_ACTIVATOR: 'привіт сара',
    },
}


class Melody:
    ACTIVATING = 'sounds/activating.mp3'


def get_constants(language=EN):
    return languages[language]
