#!/usr/bin/python 

import os
import RPi.GPIO as GPIO
from subprocess import check_output, Popen, PIPE

global rx_pid

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def my_callback(channel):
    print "button 26 pressed"
    os.system("sudo kill %s" % (proc.pid, ))

GPIO.add_event_detect(26, GPIO.FALLING, callback=my_callback, bouncetime=300)

#output = check_output(["sudo", "./receiveExample.cpp_exe"], shell=False)
proc = Popen(["sudo", "./receiveExample.cpp_exe"], stdout=PIPE)
rx_pid = proc.pid
out, err = proc.communicate()

print "The output is: ", out, type(out)

GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)
    
if "1" in out:
    print "1"
    GPIO.output(20, GPIO.HIGH)
elif "2" in out:
    print "2"
    GPIO.output(21, GPIO.HIGH)
else:
    print "Did not turn on the lights"
