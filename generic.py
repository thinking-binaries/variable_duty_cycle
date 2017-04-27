# generic.py  26/04/2017  D.J.Whale
#
# A generic Variable Duty Cycle algorithm
#
# Use this as a template for other implementations

from Timer import Timer

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
duty_cycle      = 1609344
prescale        = 10000
IN              = "Mile"
duty_master     = 10000000
postscale       = 1000
OUT             = "Kilometer"
in_stop         = 1000000
out_stop        = None
LOOP_RATE       = None

# STATE
in_count     = 0
out_count    = 0
duty_counter = 0
timer = Timer(LOOP_RATE)

def action(in_reason, in_count, in_value, out_reason, out_count, out_value):
    print("%d (%f) * %s = %d (%f) * %s" % (in_count, in_value, in_reason, out_count, out_value, out_reason))
    if in_stop  is not None and in_count  >= in_stop \
    or out_stop is not None and out_count >= out_stop:
        raise RuntimeError("STOP")

print("Ratio: %d:%d" % (duty_cycle, duty_master))

while True:
    timer.wait()
    in_count += 1
    duty_counter -= duty_cycle
    if duty_counter < 0:
        out_count += 1
        duty_counter += duty_master
        action(IN, in_count, float(in_count)/prescale, OUT, out_count, float(out_count)/postscale)

# END


# END

# END


# END


# END
