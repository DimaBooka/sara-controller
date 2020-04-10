import threading
from functools import wraps


def delay(delay_time=0):
    def wrap(f):
        @wraps(f)
        def delayed(*args, **kwargs):
            timer = threading.Timer(delay_time, f, args=args, kwargs=kwargs)
            timer.start()

        return delayed

    return wrap


def log(phrase=''):
    def wrap(f):
        @wraps(f)
        def delayed(*args, **kwargs):
            if phrase is not '':
                print(phrase)
            f(*args, **kwargs)

        return delayed

    return wrap
