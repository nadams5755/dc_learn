#motrin dose time calculator, to the nearest hour

import datetime

def todayAt (hr, min=0, sec=0, micros=0):
   now = datetime.datetime.now()
   return now.replace(hour=hr, minute=min, second=sec, microsecond=micros)

print "Motrin time check, ensures its been at least 8 hours since last dose"+"\n"

timeNow = datetime.datetime.now()

s = int(raw_input("type in the hour taken, just the hour in 24 hour format and hit 'enter'."))
# subtract 8 hours from s
diffTime = s - 8

if timeNow > todayAt (s) and s <= 8:
    print "go ahead, its safe to take another dose"
elif timeNow > todayAt (s) and s > 8:
    print "too early, wait until:"

print todayAt(diffTime)
#rough, need to do cleanup, but concept works.   now I gotta figure out how to include down to minute accuracy.
timeNow
#end
