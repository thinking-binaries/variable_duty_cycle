# generic.py  26/04/2017  D.J.Whale
#
# A generic Variable Duty Cycle algorithm
#
# Use this as a template for other implementations

#TODO: There are additional improvements in miles_to_kilometers that should be reflected here



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
duty_master     = 100
duty_cycle      = 95
ACTION          = "quarter event"
out_event_limit = 100

# STATE
cycle_no     = 0
kicks        = 0
duty_counter = 0

def action(reason, cycle_no, kick_seq):
    print("in#:%d out#%d %s" % (cycle_no, kick_seq, reason))

print("Ratio: %d:%d" % (duty_cycle, duty_master))

while kicks < out_event_limit:
    cycle_no += 1
    duty_counter -= duty_cycle
    if duty_counter < 0:
        kicks += 1
        action(ACTION, cycle_no, kicks)
        duty_counter += duty_master

# END


# END
