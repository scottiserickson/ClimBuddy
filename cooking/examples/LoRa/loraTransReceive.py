#!/usr/bin/python 

import os
import time
import signal
import RPi.GPIO as GPIO
from subprocess import check_output, Popen, PIPE, TimeoutExpired

# GLOBALS --------------------------------------------------------

global rx_proc, rx_pid 
global tx_proc, tx_pid
global isRunningTransmit
isRunningTransmit = False

# CONSTANTS ------------------------------------------------------

# GPIO button input pins (connected to ArduPi sheild).
b1_i = 18           # Set properly
b2_i = 24           # Set properly
b3_i = 25           # Set properly
b4_i = 4            # Set properly
b5_i = 27           # Set properly
b6_i = 22           # Set properly

# initializes green LED constant values
green_led_1 = 14    # Set properly (LED is fucked).
green_led_2 = 17    # Set properly
green_led_3 = 15    # Set properly
green_led_4 = 5     # Set properly
green_led_5 = 6     # Set properly
green_led_6 = 12    # Set properly

# initializes red LED constant values
red_led_1 = 13
red_led_2 = 19
red_led_3 = 26
red_led_4 = 16
red_led_5 = 20
red_led_6 = 21

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
    GPIO.add_event_detect(gpio_input, GPIO.RISING, callback=button_callback, bouncetime=400)

def red_led_setup():
    GPIO.setup(red_led_1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(red_led_2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(red_led_3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(red_led_4, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(red_led_5, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(red_led_6, GPIO.OUT, initial=GPIO.LOW)
    
# changes output to HIGH on port_num
def gpio_output_high(port_num):
    GPIO.output(port_num, GPIO.HIGH)

# changes output to LOW on port_num
def gpio_output_low(port_num):
    GPIO.output(port_num, GPIO.LOW)

# changes lit green LED to led_num 
def turn_on_green_led(green_led):
    global green_led_lit
    if green_led_lit == green_led:  
        print('led lit same\n')
    else:
        gpio_output_low(green_led_lit)
        gpio_output_high(green_led)
        green_led_lit = green_led

def turn_on_red_led(red_led):
    global red_led_lit
    if red_led_lit == red_led:
        print('led lit same\n')
    else:
        gpio_output_low(red_led_lit)
        gpio_output_high(red_led)
        red_led_lit = red_led

def pauseReceiveTransmitMessageAndContinueReceive(message):
    global rx_pid
    os.system("sudo kill -STOP %s" % (rx_pid))
    runTransmitCode(message)
    os.system("sudo kill -CONT %s" % (rx_pid))
        
# button 1 pressed
def b1_callback(self):
    print("Sent 1!") 
    turn_on_green_led(green_led_1)
    global isRunningTransmit
    if isRunningTransmit == False:
        isRunningTransmit = True
        pauseReceiveTransmitMessageAndContinueReceive("1")
        isRunningTransmit = False
    else:
        print("RUNNING CODE")

# button 2 pressed
def b2_callback(self):
    print("Sent 2!")
    turn_on_green_led(green_led_2)
    global isRunningTransmit
    if isRunningTransmit == False:
        isRunningTransmit = True
        pauseReceiveTransmitMessageAndContinueReceive("2")
        isRunningTransmit = False
    else:
        print("RUNNING CODE")

# button 3 pressed
def b3_callback(self):
    print("Sent 3!")
    turn_on_green_led(green_led_3)
    global isRunningTransmit
    if isRunningTransmit == False:
        isRunningTransmit = True
        pauseReceiveTransmitMessageAndContinueReceive("3")
        isRunningTransmit = False
    else:
        print("RUNNING CODE")

# button 4 pressed
def b4_callback(self):
    print("Sent 4!")
    turn_on_green_led(green_led_4)
    global isRunningTransmit
    if isRunningTransmit == False:
        isRunningTransmit = True
        pauseReceiveTransmitMessageAndContinueReceive("4")
        isRunningTransmit = False
    else:
        print("RUNNING CODE")

# button 5 pressed
def b5_callback(self):
    print("Sent 5!")
    turn_on_green_led(green_led_5)
    global isRunningTransmit
    if isRunningTransmit == False:
        isRunningTransmit = True
        pauseReceiveTransmitMessageAndContinueReceive("5")
        isRunningTransmit = False
    else:
        print("RUNNING CODE")

# button 6 pressed
def b6_callback(self):
    print("Sent 6!")
    turn_on_green_led(green_led_6)
    global isRunningTransmit
    if isRunningTransmit == False:
        isRunningTransmit = True
        pauseReceiveTransmitMessageAndContinueReceive("6")
        isRunningTransmit = False
    else:
        print("RUNNING CODE")

# runs receiver code in a subprocess
def runReceiveCode():
    global rx_proc
    rx_proc = Popen(["sudo", "/home/pi/ClimBuddy/cooking/examples/LoRa/receiveExample.cpp_exe"], stdin=PIPE, stdout=PIPE)
    global rx_pid
    rx_pid = rx_proc.pid

# run transmit code in a subprocess
def runTransmitCode(message): 
    try:
        global tx_proc
        tx_proc = Popen(["sudo", "/home/pi/ClimBuddy/cooking/examples/LoRa/transmitMessage.cpp_exe", message], stdin=PIPE, stdout=PIPE)
        out, err = tx_proc.communicate(timeout=8)
        global tx_pid
        tx_pid = tx_proc.pid
        tx_proc.wait() #Wait for execution of transmit to complete.
    except TimeoutExpired:
        global isRunningCode
        isRunningCode = False

# Light up LEDs depending on message received
def handleMessage(outStr):
    if "1" in outStr:
        print ("Received 1!")
        turn_on_red_led(red_led_1)
    elif "2" in outStr:
        print ("Received 2!")
        turn_on_red_led(red_led_2)
    elif "3" in outStr:
        print ("Received 3!")
        turn_on_red_led(red_led_3)
    elif "4" in outStr:
        print ("Received 4!")
        turn_on_red_led(red_led_4)
    elif "5" in outStr:
        print ("Received 5!")
        turn_on_red_led(red_led_5)
    elif "6" in outStr:
        print ("Received 6!")
        turn_on_red_led(red_led_6)
    else:
        print("ErrorReceiving")
        
# setup GPIO button type and warnings
gpio_general_setup()

# setup GPIO buttons
gpio_button_setup(b1_i, green_led_1, b1_callback)
gpio_button_setup(b2_i, green_led_2, b2_callback)
gpio_button_setup(b3_i, green_led_3, b3_callback)
gpio_button_setup(b4_i, green_led_4, b4_callback)
gpio_button_setup(b5_i, green_led_5, b5_callback)
gpio_button_setup(b6_i, green_led_6, b6_callback)
red_led_setup()

runReceiveCode()

while True:
    global rx_proc
    time.sleep(0.3)
    out, err = rx_proc.communicate()
    try:
        outStr = out.decode("utf-8")
        handleMessage(outStr)
    except UnicodeDecodeError:
        print("UnicodeDecodeError")

    runReceiveCode()
















