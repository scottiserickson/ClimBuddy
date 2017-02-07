#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import serial
import uuid

# CONSTANTS ------------------------------------------------------

# GPIO button input/output pins
b1_i = 4
b2_i = 5
b3_i = 6
b4_i = 7
b5_i = 8
b6_i = 9

# initializes green LED constant values
green_led_1 = 10
green_led_2 = 11
green_led_3 = 12
green_led_4 = 13
green_led_5 = 16
green_led_6 = 17

# initializes red LED constant values
red_led_1 = 18
red_led_2 = 19
red_led_3 = 20
red_led_4 = 21
red_led_5 = 22
red_led_6 = 23

# global variables for currently lit LEDS
red_led_lit = red_led_1
green_led_lit = green_led_1

# constants for RX message comparison
rx_button_1 = '1\n'
rx_button_2 = '2\n'
rx_button_3 = '3\n'
rx_button_4 = '4\n'
rx_button_5 = '5\n'
rx_button_6 = '6\n'

# setmode GPIO
GPIO.setmode(GPIO.BCM)

# Serial communications object
ser = serial.Serial(
    port='/dev/ttyAMA0',
    baudrate = 9600,
    parity = serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
    
def gpio_button_setup(gpio_input, gpio_output, button_callback):
    GPIO.setup(gpio_input, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(gpio_output, GPIO.OUT, initial=GPIO.LOW)
    GPIO.add_event_detect(gpio_input, GPIO.RISING)
    GPIO.add_event_callback(gpio_input, button_callback)

def b1_callback(self):
    green_led_change(green_led_1)
    send_serial_message('1')

def b2_callback(self):
    green_led_change(green_led_2)
    send_serial_message('2')

def b3_callback(self):
    green_led_change(green_led_3)
    send_serial_message('3')

def b4_callback(self):
    green_led_change(green_led_4)
    send_serial_message('4')

def b5_callback(self):
    green_led_change(green_led_5)
    send_serial_message('5')

def b6_callback(self):
    green_led_change(green_led_6)
    send_serial_message('6')
    
def send_serial_message(message):
    ser.write(message)
    print('Sent: ' + message +  ' (' + str(uuid.uuid4())[:8] + ')')

# initializes port port_num as OUTPUT GPIO 
def gpio_setup_output(port_num):
    GPIO.setup(port_num, GPIO.OUT)

# changes output to HIGH on port_num
def gpio_output_high(port_num):
    GPIO.output(port_num, GPIO.HIGH)

# changes output to LOW on port_num
def gpio_output_low(port_num):
    GPIO.output(port_num, GPIO.LOW)

# changes lit green LED to led_num 
def green_led_change(led_num):
    global green_led_lit
    if green_led_lit == led_num:
        time.sleep(1)
        print 'led lit same\n'
    else:
        gpio_output_low(green_led_lit)
        gpio_output_high(led_num)
        green_led_lit = led_num

# changes lit red LED to led_num 
def red_led_change(led_num):
    global red_led_lit
    if red_led_lit == led_num:
        time.sleep(1)
        print 'led lit same\n'
    else:
        gpio_output_low(red_led_lit)
        gpio_output_high(led_num)
        red_led_lit = led_num

# setup GPIO buttons
gpio_button_setup(b1_i, green_led_1, b1_callback)
gpio_button_setup(b2_i, green_led_2, b2_callback)
gpio_button_setup(b3_i, green_led_3, b3_callback)
gpio_button_setup(b4_i, green_led_4, b4_callback)
gpio_button_setup(b5_i, green_led_5, b5_callback)
gpio_button_setup(b6_i, green_led_6, b6_callback)

 # setup GPIO red LEDs               
gpio_setup_output(red_led_1)
gpio_setup_output(red_led_2)
gpio_setup_output(red_led_3)
gpio_setup_output(red_led_4)
gpio_setup_output(red_led_5)
gpio_setup_output(red_led_6)

# listen for communications
while True:
    if ser.inWaiting():
        x = ser.readline()
        if x == rx_button_1:
            red_led_change(red_led_1)
            print '1\n'

        elif x == rx_button_2:
            red_led_change(red_led_2)
            print '2\n'

        elif x == rx_button_3:
            red_led_change(red_led_3)
            print '3\n'

        elif x == rx_button_4:
            red_led_change(red_led_4)
            print '4\n'

        elif x == rx_button_5:
            red_led_change(red_led_5)
            print '5\n'

        elif x == rx_button_6:
            red_led_change(red_led_6)
            print '6\n'

        else:
            print 'unknown\n'
