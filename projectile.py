# projectile.py  25/04/2017  D.J.Whale
#
# A Python implementation of the Variable Duty Cycle algorithm
# implementing a simple projectile plotter
#
# Idea from:
# https://archive.org/stream/byte-magazine-1981-10/1981_10_BYTE_06-10_Local_Networks#page/n389/mode/2up

# Original Pseudo Code
#  C horizontal duty counter
#  D vertical duty counter
#  H horizontal duty cycle (velocity)
#  V vertical duty cycle (velocity)
#  M duty master

# C := C - H
# if C < 0
# then do
#     <move projectile one cell to the right>
#     C := C + M
# end
# D := D - V
# if D < 0
# then do
#    <move projectile one cell up>
#    D := C + M     #NOTE: should be D := D + M??
# end
# else if D >= M    #NOTE: indentation fixed from original code
# then do
#    <move projectile one cell down>
#    D := D - M
# end
# <decrease V by a fixed amount>

from Timer import Timer

try:
    ask = raw_input # python2
except AttributeError:
    ask = input #python3

duty_counter_h   = 0     # C
duty_counter_v   = 0     # D
duty_cycle_h     = 45    # H horizontal velocity (rightwards direction)
duty_cycle_v     = 125    # V vertical velocity (75 in upwards direction)
v_adjust         = -1    # amount to adjust V by each time round loop
duty_master      = 125   # M
x                = 0     # x position of projectile
y                = 0     # y position of projectile

LOOP_RATE        = None     # run the loop as fast as possible

timer = Timer(LOOP_RATE)
screen = None


def output(x,y):
    global screen
    if screen is None:
        from screen import Screen
        screen = Screen()
        screen.start()

    screen.plot(x, screen.height - y)

while y >= 0: # stop when projectile hits ground
    timer.wait()

    # VDC#1 for x movement
    duty_counter_h -= duty_cycle_h
    if duty_counter_h < 0:
        x += 1 # move one cell to the right
        duty_counter_h += duty_master

    # VDC#2 for y movement
    duty_counter_v -= duty_cycle_v
    if duty_counter_v < 0:
        y += 1 # move one cell up
        duty_counter_v += duty_master
    elif duty_counter_v >= duty_master:
        y -= 1 # move one cell down
        duty_counter_v -= duty_master

    # vertical velocity adustment due to gravity
    duty_cycle_v += v_adjust
    #print(duty_cycle_v)

    output(x*5, y*5)

ask("finished?")
# END
