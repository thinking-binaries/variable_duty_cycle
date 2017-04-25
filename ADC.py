# ADC.py  25/04/2017  D.J.Whale
#
# A Python implementation of the Variable Duty Cycle algorithm
# implementing a simple analog to digital convertor.
#
# Essentially, this is a software PWM generator.
#
# Idea from:
# https://archive.org/stream/byte-magazine-1981-10/1981_10_BYTE_06-10_Local_Networks#page/n389/mode/2up

# 10 C = 0
# 20 READ V
# 30 B = 0
# 40 C = C - V
# 50 IF C >= 0 THEN 80
# 60 B = 1
# 70 C = C + 5
# 80 OUTPUT B TO PIN
# 90 GOTO 30
# 100 DATA 3.75

import time

duty_master  = 100    # number in line 70
duty_cycle   = 27     # V
duty_counter = 0      # C
LOOP_RATE    = 1      # run the loop once per second

timer = None

def sync_wait(rate_sec):
    global timer

    while True:
        now = time.time()
        if timer is None or now > timer:
            timer = now + rate_sec
            return

def output(b):
    print(b)

while True:
    sync_wait(LOOP_RATE)
    bit = 0
    duty_counter -= duty_cycle
    if duty_counter < 0:
        bit = 1
        duty_counter += duty_master
    output(bit)

# END
