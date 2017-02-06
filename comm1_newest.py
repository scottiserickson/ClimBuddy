#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import serial
import uuid

b1_i = 4
b1_o = 10

b2_i = 5
b2_o = 11

b3_i = 6
b3_o = 12

b4_i = 7
b4_o = 13

b5_i = 8
b5_o = 16

b6_i = 9
b6_o = 17

ser = serial.Serial(
    port='/dev/ttyAMA0',
    baudrate = 9600,
    parity = serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
    
def gpio_setup(gpio_input, gpio_output, button_callback):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpio_input, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(gpio_output, GPIO.OUT, initial=GPIO.LOW)
    GPIO.add_event_detect(gpio_input, GPIO.RISING)
    GPIO.add_event_callback(gpio_input, button_callback)

def b1_callback(self):
    GPIO.output(b1_o, GPIO.input(b1_i))
    callback_similar('1')

def b2_callback(self):
    GPIO.output(b2_o, GPIO.input(b2_i))
    callback_similar('2')

def b3_callback(self):
    GPIO.output(b3_o, GPIO.input(b3_i))
    callback_similar('3')

def b4_callback(self):
    GPIO.output(b4_o, GPIO.input(b4_i))
    callback_similar('4')

def b5_callback(self):
    GPIO.output(b5_o, GPIO.input(b5_i))
    callback_similar('5')

def b6_callback(self):
    GPIO.output(b6_o, GPIO.input(b6_i))
    callback_similar('6')
    
def callback_similar(message):
    ser.write(message)
    print('Sent: ' + message +  ' (' + str(uuid.uuid4())[:8] + ')')
    time.sleep(2)

gpio_setup(b1_i, b1_o, b1_callback)
gpio_setup(b2_i, b2_o, b2_callback)
gpio_setup(b3_i, b3_o, b3_callback)
gpio_setup(b4_i, b4_o, b4_callback)
gpio_setup(b5_i, b5_o, b5_callback)
gpio_setup(b6_i, b6_o, b6_callback)



