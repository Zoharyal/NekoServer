#!/usr/bin/env python
# -*- coding: utf8 -*-

from RPLCD.i2c import CharLCD
import RPi.GPIO as GPIO
import time
import os
from time import sleep
from pydub import AudioSegment
from pydub.playback import play

class AngryFace:
    def draw():
        ledRedPin = 13      #define 3 pins of RGBLED
        ledGreenPin = 16
        ledBluePin = 37
        fileName = os.path.abspath('script/ecole.wav')
        song = AudioSegment.from_wav(fileName)
        global p_Red,p_Green,p_Blue
        GPIO.setmode(GPIO.BOARD)
        def destroy():
            lcd.clear()
        lcd = CharLCD('PCF8574', 0x27)
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
            0b10000,
            0b01000,
            0b00100,
            0b00010,
            0b00001,
        )

        righttopcorner = (
            0b00000,
            0b00000,
            0b00000,
            0b00001,
            0b00010,
            0b00100,
            0b01000,
            0b10000,
        )

        mouthleft = (
            0b00001,
            0b00010,
            0b00100,
            0b01000,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
        )

        mouthright = (
            0b10000,
            0b01000,
            0b00100,
            0b00010,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
        )

        angryleft = (
            0b00010,
            0b00001,
            0b01000,
            0b00100,
            0b00010,
            0b00100,
            0b01001,
            0b00010,
        )
        angryright = (
            0b01000,
            0b10000,
            0b00010,
            0b00100,
            0b01000,
            0b00100,
            0b10010,
            0b01000,
        )
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
        p_Red.ChangeDutyCycle(100)  #red
        p_Green.ChangeDutyCycle(0)
        p_Blue.ChangeDutyCycle(100)
        play(song)
        lcd.create_char(0, empty)
        lcd.create_char(1, lefttopcorner)
        lcd.create_char(2, righttopcorner)

        lcd.create_char(3, angryleft)
        lcd.create_char(4, angryright)

        lcd.create_char(5, mouthleft)
        lcd.create_char(6, mouthright)
        # premire ligne
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x01')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x02')
        lcd.write_string('\x00')
        lcd.write_string('\x03')
        lcd.write_string('\x04')
        lcd.write_string('\x00')

        #permet de d'aligner pafaitement la 2nd ligne à la premiere
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')

        # seconde ligne
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x05')
        lcd.write_string('\x06')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')
        lcd.write_string('\x00')

        sleep(4)
        destroy()
