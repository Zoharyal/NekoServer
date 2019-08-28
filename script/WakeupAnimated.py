#!/usr/bin/env python
# -*- coding: utf8 -*-

from RPLCD.i2c import CharLCD
import os
from time import sleep
from pydub import AudioSegment
from pydub.playback import play

class WakeupAnimated:

    def loop():
        fileName = os.path.abspath('script/biendormi.wav')
        song = AudioSegment.from_wav(fileName)
        loop = 0
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
        lefttopcorneropen = (
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00011,
            0b00100,
            0b01000,
            0b01000,
        )
        middletopopen = (
            0b00000,
            0b00000,
            0b00000,
            0b11111,
            0b00000,
            0b00000,
            0b11111,
            0b11111
        )
        righttopcorneropen = (
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b11000,
            0b00100,
            0b00010,
            0b00010,
        )
        middlebottomopen = (
            0b11111,
            0b11111,
            0b00000,
            0b00000,
            0b11111,
            0b00000,
            0b00000,
            0b00000
        )
        leftbottomcorneropen = (
            0b01000,
            0b01000,
            0b00100,
            0b00011,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
        )

        rightbottomcorneropen = (
            0b00010,
            0b00010,
            0b00100,
            0b11000,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
        )

        lefttopcornerclose = (
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00001,
        )
        middletopclose = (
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b11111
        )
        righttopcornerclose = (
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b10000,
        )
        middlebottomclose = (
            0b11111,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00000,
            0b00000
        )
        def destroy():
            lcd.clear()

        def drawopen():
            # premire ligne
            lcd.write_string('\x00')
            lcd.write_string('\x00')
            lcd.write_string('\x01')
            lcd.write_string('\x05')
            lcd.write_string('\x02')
            lcd.write_string('\x00')
            lcd.write_string('\x00')
            lcd.write_string('\x00')
            lcd.write_string('\x00')
            lcd.write_string('\x00')
            lcd.write_string('\x00')
            lcd.write_string('\x01')
            lcd.write_string('\x05')
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
            lcd.write_string('\x06')
            lcd.write_string('\x03')
            lcd.write_string('\x00')
            lcd.write_string('\x00')
            lcd.write_string('\x04')
            lcd.write_string('\x03')
            lcd.write_string('\x00')
            lcd.write_string('\x00')
            lcd.write_string('\x04')
            lcd.write_string('\x06')
            lcd.write_string('\x03')
            lcd.write_string('\x00')
            lcd.write_string('\x00')

        def drawclose():
            # premire ligne
            lcd.write_string('\x00')
            lcd.write_string('\x00')
            lcd.write_string('\x01')
            lcd.write_string('\x05')
            lcd.write_string('\x02')
            lcd.write_string('\x00')
            lcd.write_string('\x00')
            lcd.write_string('\x00')
            lcd.write_string('\x00')
            lcd.write_string('\x00')
            lcd.write_string('\x00')
            lcd.write_string('\x01')
            lcd.write_string('\x05')
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
            lcd.write_string('\x00')
            lcd.write_string('\x06')
            lcd.write_string('\x00')
            lcd.write_string('\x00')
            lcd.write_string('\x00')
            lcd.write_string('\x04')
            lcd.write_string('\x03')
            lcd.write_string('\x00')
            lcd.write_string('\x00')
            lcd.write_string('\x00')
            lcd.write_string('\x06')
            lcd.write_string('\x00')
            lcd.write_string('\x00')
            lcd.write_string('\x00')

        lcd.create_char(0, empty)
        lcd.create_char(1, lefttopcornerclose)
        lcd.create_char(2, righttopcornerclose)

        lcd.create_char(3, rightbottomcorneropen)
        lcd.create_char(4, leftbottomcorneropen)

        lcd.create_char(5, middletopclose)
        lcd.create_char(6, middlebottomclose)
        drawclose()
        play(song)
        destroy()
        lcd.create_char(0, empty)
        lcd.create_char(1, lefttopcorneropen)
        lcd.create_char(2, righttopcorneropen)

        lcd.create_char(3, rightbottomcorneropen)
        lcd.create_char(4, leftbottomcorneropen)

        lcd.create_char(5, middletopopen)
        lcd.create_char(6, middlebottomopen)
        drawopen()
        sleep(4)
        destroy()
        GPIO.cleanup()
