#!/usr/bin/env python3

import signal
import sys

from sara import SaraController
from decorators import log


def signal_handler(cancelling):

    @log('You pressed Ctrl+C!')
    def cancel(s, r):
        cancelling()
        sys.exit(0)

    return cancel


if __name__ == '__main__':
    sara = SaraController()

    signal.signal(signal.SIGINT, signal_handler(sara.cancelling))
    print('Press Ctrl+C')
    signal.pause()
