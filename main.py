#!/usr/bin/env python3

import argparse
import signal
import sys

from sara.language import get_language, set_language
from sara.sara import SaraController
from sara.decorators import log


def signal_handler(cancelling):

    @log('You pressed Ctrl+C!')
    def cancel(s, r):
        # commented because speech recognition waits until microphone
        # stops to hear something and only then will be called exit
        # cancelling()
        sys.exit(0)

    return cancel


def parse_args():
    parser = argparse.ArgumentParser(description='Sara arguments')
    parser.add_argument('-ln', nargs='?', default='en', help='russian language')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    set_language(args.ln)
    language = get_language()
    sara = SaraController(language)

    signal.signal(signal.SIGINT, signal_handler(sara.cancelling))
    print('Press Ctrl+C')
    signal.pause()
