#!/usr/bin/env python3

from decorators import delay


class Timer:
    clear_timer = False

    def set_timeout(self, fn, time):

        @delay(time)
        def some_fn():
            if self.clear_timer is False:
                fn()

        some_fn()

        return self.set_clear_timer

    def set_clear_timer(self):
        self.clear_timer = True
