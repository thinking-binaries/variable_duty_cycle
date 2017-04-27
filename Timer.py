# Timer.py  27/04/2017  D.J.Whale

import time

class Timer():
    def __init__(self, rate=1.0):
        self.rate = rate
        self.next_time = None

    def wait(self):
        if self.rate is None: return

        while True:
            now = time.time()
            if self.next_time is None or now > self.next_time:
                self.next_time = now + self.rate
                return

#TODO: add in the work we did on another project for accurate timers
#cooperative scheduling option, returning remaining time
#if within a threshold, stay in loop and sleep wait
#if within another threshold, busy wait for precise point
#capture how much late by, and if greater than a threshold, timing error

# END
