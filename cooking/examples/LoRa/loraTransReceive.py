#!/usr/bin/python 

import os
import time
import signal
import RPi.GPIO as GPIO
from subprocess import check_output, Popen, PIPE, TimeoutExpired

# GLOBALS --------------------------------------------------------

global out, err
global rx_proc, rx_pid 
global tx_proc, tx_pid
global isRunningTransmit
isRunningTransmit = False

# CONSTANTS ------------------------------------------------------

# GPIO button input pins (connected to ArduPi sheild).
b1_i = 22 
b2_i = 27 
b3_i = 18
b4_i = 4
b5_i = 25
b6_i = 24

# initializes green LED constant values
green_led_1 = 6 # testing
green_led_2 = 11
green_led_3 = 12
green_led_4 = 13
green_led_5 = 16
green_led_6 = 17

# initializes red LED constant values
red_led_1 = 7 # testing
red_led_2 = 19
red_led_3 = 20
red_led_4 = 21
red_led_5 = 22
red_led_6 = 23

# global variables for currently lit LEDS
red_led_lit = red_led_1
green_led_lit = green_led_1

# FUNCTION DEFINITIONS -------------------------------------------

# turn off warnings and set gpio pin mode to use BCM numbering
def gpio_general_setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

# general button setup for input/output and callback
def gpio_button_setup(gpio_input, gpio_output, button_callback):
    GPIO.setup(gpio_input, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(gpio_output, GPIO.OUT, initial=GPIO.LOW)
    GPIO.add_event_detect(gpio_input, GPIO.RISING, callback=button_callback, bouncetime=1000)

# changes output to HIGH on port_num
def gpio_output_high(port_num):
    GPIO.output(port_num, GPIO.HIGH)

# changes output to LOW on port_num
def gpio_output_low(port_num):
    GPIO.output(port_num, GPIO.LOW)

# changes lit green LED to led_num 
def green_led_change(led_num):
    print("change green led")
    #global green_led_lit
    #if green_led_lit == led_num:
    #    print 'led lit same\n'
    #else:
    #    gpio_output_low(green_led_lit)
    #    gpio_output_high(led_num)
    #    green_led_lit = led_num
        
# button 1 pressed
def b1_callback(self):
    print("button 1")
    global isRunningTransmit
    if isRunningTransmit == False:
        isRunningTransmit = True
        green_led_change(green_led_1)
        os.system("sudo kill -STOP %s" % (rx_pid))
        runTransmitCode("1")
        os.system("sudo kill -CONT %s" % (rx_pid))
        isRunningTransmit = False
    else:
        print("RUNNING CODE")

# button 2 pressed
def b2_callback(self):
    print("button 2")
    global isRunningTransmit
    if isRunningTransmit == False:
        isRunningTransmit = True
        green_led_change(green_led_2)
        os.system("sudo kill -STOP %s" % (rx_pid))
        runTransmitCode("2")
        os.system("sudo kill -CONT %s" % (rx_pid))
        isRunningTransmit = False
    else:
        print("RUNNING CODE")

# button 3 pressed
def b3_callback(self):
    print("button 3")
    global isRunningTransmit
    if isRunningTransmit == False:
        isRunningTransmit = True
        green_led_change(green_led_3)
        os.system("sudo kill -STOP %s" % (rx_pid))
        runTransmitCode("3")
        os.system("sudo kill -CONT %s" % (rx_pid))
        isRunningTransmit = False
    else:
        print("RUNNING CODE")

# button 4 pressed
def b4_callback(self):
    print("button 4")
    global isRunningTransmit
    if isRunningTransmit == False:
        isRunningTransmit = True
        green_led_change(green_led_4)
        os.system("sudo kill -STOP %s" % (rx_pid))
        runTransmitCode("4")
        os.system("sudo kill -CONT %s" % (rx_pid))
        isRunningTransmit = False
    else:
        print("RUNNING CODE")

# button 5 pressed
def b5_callback(self):
    print("button 5")
    global isRunningTransmit
    if isRunningTransmit == False:
        isRunningTransmit = True
        green_led_change(green_led_5)
        os.system("sudo kill -STOP %s" % (rx_pid))
        runTransmitCode("5")
        os.system("sudo kill -CONT %s" % (rx_pid))
        isRunningTransmit = False
    else:
        print("RUNNING CODE")

# button 6 pressed
def b6_callback(self):
    print("button 6")
    global isRunningTransmit
    if isRunningTransmit == False:
        isRunningTransmit = True
        green_led_change(green_led_6)
        os.system("sudo kill -STOP %s" % (rx_pid))
        runTransmitCode("6")
        os.system("sudo kill -CONT %s" % (rx_pid))
        isRunningTransmit = False
    else:
        print("RUNNING CODE")

# runs receiver code in a subprocess
def runReceiveCode():
    global rx_proc
    rx_proc = Popen(["sudo", "./receiveExample.cpp_exe"], stdout=PIPE)
    global rx_pid
    rx_pid = rx_proc.pid

# run transmit code in a subprocess
def runTransmitCode(message):
    global tx_proc
    try:
        tx_proc = Popen(["sudo", "./transmitMessage.cpp_exe", message], stdout=PIPE)
        a, b = tx_proc.communicate(timeout=8)
        global tx_pid
        tx_pid = tx_proc.pid
        #Wait for execution of transmit to complete.
        tx_proc.wait()
    except TimeoutExpired:
        global isRunningCode
        isRunningCode = False

# setup GPIO button type and warnings
gpio_general_setup()

# setup GPIO buttons
gpio_button_setup(b1_i, green_led_1, b1_callback)
gpio_button_setup(b2_i, green_led_2, b2_callback)
gpio_button_setup(b3_i, green_led_3, b3_callback)
gpio_button_setup(b4_i, green_led_4, b4_callback)
gpio_button_setup(b5_i, green_led_5, b5_callback)
gpio_button_setup(b6_i, green_led_6, b6_callback)

runReceiveCode()

while True:
    out, err = rx_proc.communicate()    
    
    #if "1" in out:
    #    print "1!"
        
    runReceiveCode()


















































