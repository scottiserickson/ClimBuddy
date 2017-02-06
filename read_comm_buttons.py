#!/usr/bin/env python

import time
import serial
import RPi.GPIO as GPIO

# initializes red LED constant values
red_led_1 = 18
red_led_2 = 19
red_led_3 = 20
red_led_4 = 21
red_led_5 = 22
red_led_6 = 23

# global variables for currently lit LEDS
red_led_lit = 18

# constants for RX message comparison
rx_button_1 = '1\n'
rx_button_2 = '2\n'
rx_button_3 = '3\n'
rx_button_4 = '4\n'
rx_button_5 = '5\n'
rx_button_6 = '6\n'

# setmode GPIO
GPIO.setmode(GPIO.BCM)

# serail port initialization
ser = serial.Serial(
	port="/dev/ttyAMA0",
	baudrate = 9600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=1
)

# initializes port port_num as OUTPUT GPIO 
def gpio_setup_output(port_num):
        GPIO.setup(port_num, GPIO.OUT)

# changes output to HIGH on port_num
def gpio_output_high(port_num):
        GPIO.output(port_num, GPIO.HIGH)

# changes output to LOW on port_num
def gpio_output_low(port_num):
        GPIO.output(port_num, GPIO.LOW)

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

                
gpio_setup_output(red_led_1)
gpio_setup_output(red_led_2)
gpio_setup_output(red_led_3)
gpio_setup_output(red_led_4)
gpio_setup_output(red_led_5)
gpio_setup_output(red_led_6)

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

        
                        
                
