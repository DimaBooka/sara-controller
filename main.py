#!/usr/bin/env python3

import argparse
import signal
import sys

from procedures.registry import ProcedureRegistry
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
    parser.add_argument('-cmd', nargs='?', default='', help='procedure activator')

    return parser.parse_args()


def run_command(ln, command):
    r = ProcedureRegistry(ln)

    ps = r.detect_procedures(command)
    for p in ps:
        p.proceed(command)


def run_sara(ln):
    sara = SaraController(ln)

    signal.signal(signal.SIGINT, signal_handler(sara.cancelling))
    print('Press Ctrl+C')
    signal.pause()


if __name__ == '__main__':
    args = parse_args()
    set_language(args.ln)
    language = get_language()

    if args.cmd:
        run_command(language, args.cmd)
    else:
        run_sara(language)
