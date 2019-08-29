#!/usr/bin/env python
# -*- coding: utf8 -*-

from RPLCD.i2c import CharLCD
import RPi.GPIO as GPIO
import time
from time import sleep
import smbus
import os
from pydub import AudioSegment
from pydub.playback import play

class Dance:
    def draw():
        OFFSE_DUTY = 0.5        #define pulse offset of servo
        SERVO_MIN_DUTY = 2.5+OFFSE_DUTY     #define pulse duty cycle for minimum angle of servo
        SERVO_MAX_DUTY = 12.5+OFFSE_DUTY    #define pulse duty cycle for maximum angle of servo
        servoPin = 12
        ledRedPin = 13      #define 3 pins of RGBLED
        ledGreenPin = 16
        ledBluePin = 22
        loop = 0
        fileName = os.path.abspath('script/danser.wav')
        song = AudioSegment.from_wav(fileName)
        global p_Red,p_Green,p_Blue,p
        GPIO.setmode(GPIO.BOARD)
        def destroy():
            lcd.clear()
            GPIO.cleanup()
        lcd = CharLCD('PCF8574', 0x27)
        def map( value, fromLow, fromHigh, toLow, toHigh):
            return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow
        def servoWrite(angle):      # make the servo rotate to specific angle (0-180 degrees)
            if(angle<0):
                angle = 0
            elif(angle > 180):
                angle = 180
            p.ChangeDutyCycle(map(angle,0,180,SERVO_MIN_DUTY,SERVO_MAX_DUTY))#map the angle to duty cycle and output it
        empty = (
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
        )
        lefttopcorner = (
            0b00000,
            0b00000,
            0b00000,
            0b00001,
            0b00010,
            0b00011,
            0b00010,
            0b00010,
        )

        righttopcorner = (
            0b00000,
            0b00111,
            0b11001,
            0b00111,
            0b11001,
            0b00001,
            0b00001,
            0b00001,
        )

        mouthleft = (
            0b00000,
            0b00000,
            0b00001,
            0b00011,
            0b00011,
            0b00011,
            0b00001,
            0b00000,
        )

        mouthright = (
            0b00000,
            0b00000,
            0b10000,
            0b11000,
            0b11000,
            0b11000,
            0b10000,
            0b00000,
        )

        leftbottomcorner = (
            0b00010,
            0b00010,
            0b01110,
            0b11110,
            0b11110,
            0b01100,
            0b00000,
            0b00000,
        )
        rightbottomcorner = (
            0b00001,
            0b00111,
            0b01111,
            0b01111,
            0b00110,
            0b00000,
            0b00000,
            0b00000,
        )

        GPIO.setup(servoPin, GPIO.OUT)   # Set servoPin's mode is output
        GPIO.setup(ledRedPin,GPIO.OUT)      #set 3 pins of RGBLED to output mode
        GPIO.setup(ledGreenPin,GPIO.OUT)
        GPIO.setup(ledBluePin,GPIO.OUT)

        p_Red = GPIO.PWM(ledRedPin,1000)    #configure PMW to 3 pins of RGBLED
        p_Red.start(0)
        p_Green = GPIO.PWM(ledGreenPin,1000)
        p_Green.start(0)
        p_Blue = GPIO.PWM(ledBluePin,1000)
        p_Blue.start(0)
        p = GPIO.PWM(servoPin, 50)     # set Frequece to 50Hz
        p.start(0)                     # Duty Cycle = 0
        p_Red.ChangeDutyCycle(0)  #green
        p_Green.ChangeDutyCycle(100)
        p_Blue.ChangeDutyCycle(100)


        lcd.create_char(0, empty)
        lcd.create_char(1, lefttopcorner)
        lcd.create_char(2, righttopcorner)

        lcd.create_char(3, leftbottomcorner)
        lcd.create_char(4, rightbottomcorner)

        lcd.create_char(5, mouthleft)
        lcd.create_char(6, mouthright)
        # premire ligne
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x01')
        lcd.write_string('\x02')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x01')
        lcd.write_string('\x02')
        lcd.write_string('\x00')
        lcd.write_string('\x00')

        #permet de d'aligner pafaitement la 2nd ligne à la premiere
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')

        # seconde ligne
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x03')
        lcd.write_string('\x04')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x05')
        lcd.write_string('\x06')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x03')
        lcd.write_string('\x04')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        play(song)
        while (loop<6):
            for dc in range(90, 181, 1):   #make servo rotate from 0 to 180 deg
                servoWrite(dc)     # Write to servo
                time.sleep(0.001)
            time.sleep(0.5)
            for dc in range(180, 89, -1): #make servo rotate from 180 to 0 deg
                servoWrite(dc)
                time.sleep(0.001)
            time.sleep(0.5)
            loop += 1
        destroy()
        p.stop()
