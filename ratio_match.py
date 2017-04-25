# ratio_match.py  25/04/2017  D.J.Whale
#
# A Python implementation of the Variable Duty Cycle algorithm
# implementing a simple rising number ratio tracker
#
# Specifically, "two integer quantities need to be kept as close to a given ratio
# as possible, while both are gradually increased from zero to some higher number"
#
# Idea from:
# https://archive.org/stream/byte-magazine-1981-10/1981_10_BYTE_06-10_Local_Networks#page/n389/mode/2up
#
# e.g. this could be used to generate two time-synchronised ramps, where their target
# amplitude is different but their zero-crossing time and peak-achieved time are identical.
# The below example is as close as possible to the original presentation, but you can see
# how a reset of I,J to zero could be synthesised at a key moment (e.g. when any one of
# then reaches a target maximum, both could be reset to zero, which would create
# a repeating ramp pattern for both).

# Original Pseudo Code:
# I and J   are two integers where their ratio needs to be maintained
# K:L       is the desired ratio between them
# C and D   are duty counters
# M         is the duty master, which is greater than or equal to both K and L
#
# C := C - K
# if C < 0
# then do
#     <increment I>
#     C := C + M
# end
# D := D - L
# if D < 0
# then do
#    <increment J>
#    D := D + M
# end

import time

duty_counter_1   = 0   # C
duty_counter_2   = 0   # D
value_1          = 0   # I
value_2          = 0   # J
duty_cycle_1     = 33  # K
duty_cycle_2     = 100 # L
duty_master      = 100 # M

LOOP_RATE    = 1      # run the loop once per second

timer = None

def sync_wait(rate_sec):
    global timer

    while True:
        now = time.time()
        if timer is None or now > timer:
            timer = now + rate_sec
            return

def output(a, b):
    print(a, b)

while True:
    sync_wait(LOOP_RATE)

    # VDC#1
    duty_counter_1 -= duty_cycle_1
    if duty_counter_1 < 0:
        # kickee 1
        value_1 += 1
        duty_counter_1 += duty_master

    # VDC#2
    duty_counter_2 -= duty_cycle_2
    if duty_counter_2 < 0:
        # kickee 2
        value_2 += 1
        duty_counter_2 += duty_master

    output(value_1, value_2)

# END
