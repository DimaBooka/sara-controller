#!/usr/bin/env python3

import argparse
import signal
import sys

from procedures.registry import ProcedureRegistry
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
    parser.add_argument('-cmd', nargs='?', default='', help='procedure activator')

    return parser.parse_args()


def run_command(command):
    r = ProcedureRegistry()

    ps = r.detect_procedures(command)
    for p in ps:
        p.proceed(command)


def run_sara():
    sara = SaraController()

    signal.signal(signal.SIGINT, signal_handler(sara.cancelling))
    print('Press Ctrl+C')
    signal.pause()


def main():
    args = parse_args()

    if args.cmd:
        run_command(args.cmd)
        return

    run_sara()


if __name__ == '__main__':
    main()
