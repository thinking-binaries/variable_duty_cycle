# miles_to_kilometers.py  26/04/2017  D.J.Whale
#
# Supposedly a MPH to KPH convertor.
# More realistically, it is an ODOMETER that has an input circuit measuring miles travelled,
# and an output circuit that displays kilometers travelled.

# 1 Mile            = 1.609344 km
# 0.621371192 Miles = 1 km
#
# Miles->Kilometers   * 1.609344
# every 0.621,371,192 miles = 1 kilometer

# every 0.621371192 Miles, we need to count 1 Kilometer
# every 621 thousandths of a mile, we need to count 1 thousandth of a kilometer

# NOTE 1: because duty_cycle must be <= duty_master, we have to scale the ratio
# to stay within those requirements. This introduces a factor of 10 error on
# the ratio, that is corrected using the prescaler.

# NOTE 2: To improve precision, everything is scaled up.
# This means in practice, a hardware acquisition system would have to send
# more frequent distance pulses to the input circuit. This is fine, because
# we wouldn't wait for a whole mile to send a distance pulse, we would probably wait
# for a tiny fraction of a mile (e.g. 1 foot) to send a pulse.

# PARAMETERS
duty_cycle      = 1609344
prescale        = 10000
IN              = "Mile"
duty_master     = 10000000
postscale       = 1000
OUT             = "Kilometer"
in_stop         = 1000000
out_stop        = None

# STATE
in_count     = 0
out_count    = 0
duty_counter = 0

def action(in_reason, in_count, in_value, out_reason, out_count, out_value):
    print("%d (%f) * %s = %d (%f) * %s" % (in_count, in_value, in_reason, out_count, out_value, out_reason))
    if in_stop  is not None and in_count  >= in_stop \
    or out_stop is not None and out_count >= out_stop:
        raise RuntimeError("STOP")

print("Ratio: %d:%d" % (duty_cycle, duty_master))

while True:
    in_count += 1
    duty_counter -= duty_cycle
    if duty_counter < 0:
        out_count += 1
        duty_counter += duty_master
        action(IN, in_count, float(in_count)/prescale, OUT, out_count, float(out_count)/postscale)

# END


# END

# END
