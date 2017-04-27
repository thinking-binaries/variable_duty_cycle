# generic.py  26/04/2017  D.J.Whale
#
# A generic Variable Duty Cycle algorithm
#
# Use this as a template for other implementations

from Timer import Timer
from screen import Screen

try:
    ask = raw_input #Python 2
except AttributeError:
    ask = input #Python 3

#initialise duty_master, duty_counter
#    where duty_master > 0
#    and   duty_counter >= 0
#    and   duty_counter <= duty_master
#
#kickor_loop:
#do forever
#    wait for next time period
#    duty_counter = duty_counter - duty_cycle
#    if duty_counter is negative
#        initiate_kickee_action
#        duty_counter = duty_counter + duty_master
#    end if
#end do

# PARAMETERS
duty_cycle      = 57
duty_master     = 100

prescale        = 1
IN              = ""
postscale       = 1
OUT             = ""
in_stop         = 100
out_stop        = None
LOOP_RATE       = None

# STATE
in_count     = 0
out_count    = 0
duty_counter = 0
finished     = False
timer = Timer(LOOP_RATE)
screen = Screen()

def action(in_reason, in_count, in_value, out_reason, out_count, out_value):
    global finished
    print("%d (%f) * %s = %d (%f) * %s" % (in_count, in_value, in_reason, out_count, out_value, out_reason))
    if in_stop  is not None and in_count  >= in_stop \
    or out_stop is not None and out_count >= out_stop:
        finished = True

print("Ratio: %d:%d" % (duty_cycle, duty_master))

def point(x, y):
    screen.line_to(x*10, duty_master - y)

def draw_axies():
    LEN = 640
    screen.line(0, duty_master, LEN, duty_master) # actually the lower line
    screen.line(0, 4, LEN, 4) # actually the upper line
    screen.goto(None, None)

draw_axies()

while not finished:
    timer.wait()
    in_count += 1
    duty_counter -= duty_cycle
    point(in_count, duty_counter)

    if duty_counter < 0:
        out_count += 1
        duty_counter += duty_master
        action(IN, in_count, float(in_count)/prescale, OUT, out_count, float(out_count)/postscale)

    point(in_count, duty_counter)

ask("finished?")

# END
