#!/usr/bin/env python3
#############################################################################
# Filename    : Softlight.py
# Description : Potentiometer control LED
# Author      : freenove
# modification: 2018/08/02
########################################################################
import RPi.GPIO as GPIO

import time


ledRedPin = 13      #define 3 pins of RGBLED
ledGreenPin = 16
ledBluePin = 37

def setup():
    global p_Red,p_Green,p_Blue
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledRedPin,GPIO.OUT)      #set 3 pins of RGBLED to output mode
    GPIO.setup(ledGreenPin,GPIO.OUT)
    GPIO.setup(ledBluePin,GPIO.OUT)

    p_Red = GPIO.PWM(ledRedPin,1000)    #configure PMW to 3 pins of RGBLED
    p_Red.start(0)
    p_Green = GPIO.PWM(ledGreenPin,1000)
    p_Green.start(0)
    p_Blue = GPIO.PWM(ledBluePin,1000)
    p_Blue.start(0)

def loop():
    while True:
        print ('open blue')
        p_Red.ChangeDutyCycle(0)  #blue
        p_Green.ChangeDutyCycle(100)
        p_Blue.ChangeDutyCycle(100)
        time.sleep(5)

        print ('open green')
        p_Red.ChangeDutyCycle(100)  #green
        p_Green.ChangeDutyCycle(100)
        p_Blue.ChangeDutyCycle(0)
        time.sleep(5)
        print ('open red')
        p_Red.ChangeDutyCycle(100)  #red
        p_Green.ChangeDutyCycle(0)
        p_Blue.ChangeDutyCycle(100)
        time.sleep(5)
def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    print ('Program is starting ... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
