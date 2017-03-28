#!/usr/bin/python

import os, sched, signal, subprocess, time

global process
global pid

s = sched.scheduler(time.time, time.sleep)

def runTransceiverCode():
    global process, pid 
    process = subprocess.Popen(["sudo", "python3", "/home/pi/ClimBuddy/cooking/examples/LoRa/loraTransReceive.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    pid = process.pid

def killTransceiverCode():
    global process
    process.kill()

while True:
    time.sleep(1)
    runTransceiverCode()
    s.enter(45, 1, killTransceiverCode)
    s.run()
    
    
