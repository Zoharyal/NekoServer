#!/usr/bin/env python3
# -*- coding: utf8 -*-

from RPLCD.i2c import CharLCD
import RPi.GPIO as GPIO
import time
import os
from time import sleep
import smbus
from pydub import AudioSegment
from pydub.playback import play

class HappyFaceAnimated:
    def loop():
        ledRedPin = 13      #define 3 pins of RGBLED
        ledGreenPin = 16
        ledBluePin = 37
        fileName = os.path.abspath('script/happy.wav')
        song = AudioSegment.from_wav(fileName)
        global p_Red,p_Green,p_Blue
        GPIO.setmode(GPIO.BOARD)
        def destroy():
            lcd.clear()
        def draw():
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
            lcd.write_string('\x04')
            lcd.write_string('\x03')
            lcd.write_string('\x00')
            lcd.write_string('\x00')
            lcd.write_string('\x00')
            lcd.write_string('\x05')
            lcd.write_string('\x06')
            lcd.write_string('\x00')
            lcd.write_string('\x00')
            lcd.write_string('\x00')
            lcd.write_string('\x04')
            lcd.write_string('\x03')
            lcd.write_string('\x00')
            lcd.write_string('\x00')
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
            0b00000,
            0b00000,
            0b01110,
            0b11111,
            0b11111,
        )

        righttopcorner = (
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b01110,
            0b11111,
            0b111111,
        )

        leftbottomcorner = (
            0b11111,
            0b01111,
            0b00111,
            0b00011,
            0b00001,
            0b00000,
            0b00000,
            0b00000,
        )

        rightbottomcorner = (
            0b11111,
            0b11110,
            0b11100,
            0b11000,
            0b10000,
            0b00000,
            0b00000,
            0b00000,
        )

        mouthleft = (
            0b00000,
            0b00011,
            0b00111,
            0b00111,
            0b00111,
            0b00011,
            0b00000,
            0b00000
        )

        mouthright = (
            0b00000,
            0b11000,
            0b11100,
            0b11100,
            0b11100,
            0b11000,
            0b00000,
            0b00000
        )



        lefttopcornersmall  = (
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00110,
            0b01111,
        )

        righttopcornersmall  = (
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b0000,
            0b01100,
            0b11110,
        )

        leftbottomcornersmall  = (
            0b01111,
            0b00111,
            0b00011,
            0b00001,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
        )

        rightbottomcornersmall = (
            0b11110,
            0b11100,
            0b11000,
            0b10000,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
        )
        looping = 0
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
        p_Red.ChangeDutyCycle(0)  #green
        p_Green.ChangeDutyCycle(100)
        p_Blue.ChangeDutyCycle(100)
        play(song)
        while(looping < 5):
            lcd.create_char(0, empty)
            lcd.create_char(1, lefttopcorner)
            lcd.create_char(2, righttopcorner)

            lcd.create_char(3, rightbottomcorner)
            lcd.create_char(4, leftbottomcorner)

            lcd.create_char(5, mouthleft)
            lcd.create_char(6, mouthright)
            draw()
            sleep(1)
            lcd.create_char(0, empty)
            lcd.create_char(1, lefttopcornersmall)
            lcd.create_char(2, righttopcornersmall)

            lcd.create_char(3, rightbottomcornersmall)
            lcd.create_char(4, leftbottomcornersmall)

            lcd.create_char(5, mouthleft)
            lcd.create_char(6, mouthright)
            draw()
            sleep(1)
            destroy()
            looping += 1
