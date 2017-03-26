#!/usr/bin/python 

import os
import time
import RPi.GPIO as GPIO
from subprocess import check_output, Popen, PIPE

global out, err, proc

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def my_callback(self):
    print "button 26 pressed"
    os.system("sudo kill %s" % (rx_pid, ))
    runTransmitCode("bigmoney")
    runReceiveCode()

def gpio_button_setup(gpio_input, gpio_output, button_callback):
    GPIO.setup(gpio_input, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(gpio_output, GPIO.OUT, initial=GPIO.LOW)
    GPIO.add_event_detect(gpio_input, GPIO.RISING)
    GPIO.add_event_callback(gpio_input, button_callback)

def b1_callback(self):
    "button 26 pressed"
    green_led_change(green_led_1)
    send_serial_message(rx_button_1)

# runs receiver code in a subprocess
def runReceiveCode():
    proc = Popen(["sudo", "./receiveExample.cpp_exe"], stdout=PIPE)
    global rx_pid
    rx_pid = proc.pid
    global out
    out, err = proc.communicate()

# run transmit code in a subprocess
def runTransmitCode(message):
    proc = Popen(["sudo", "./transmitMessage.cpp_exe", message], stdout=PIPE)
    proc.wait()
    
GPIO.add_event_detect(26, GPIO.FALLING, callback=my_callback, bouncetime=300)

GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)
    

#if "1" in out:
#    print "1"
#    GPIO.output(20, GPIO.HIGH)
#elif "2" in out:
#    print "2"
#    GPIO.output(21, GPIO.HIGH)
#else:
#    print "Did not turn on the lights"

runReceiveCode()

while True:
    if "1" in out:
        print "received 1"
