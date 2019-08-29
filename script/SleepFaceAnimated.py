from RPLCD.i2c import CharLCD
import time
from time import sleep
import os
from pydub import AudioSegment
from pydub.playback import play
fileName = os.path.abspath('script/snooze.wav')
song = AudioSegment.from_wav(fileName)
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
    0b00000,
    0b00000,
    0b11111,
)

righttopcorner = (
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b11111,
)

leftbottomcorner = (
    0b00111,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
)

rightbottomcorner = (
    0b11100,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
)

mouthleftopen = (
    0b00000,
    0b00011,
    0b00111,
    0b00111,
    0b00111,
    0b00111,
    0b00011,
    0b00000,
)

mouthrightopen = (
    0b00000,
    0b11000,
    0b11100,
    0b11100,
    0b11100,
    0b11100,
    0b11000,
    0b00000,
)
mouthleftclose = (
    0b00000,
    0b00000,
    0b00000,
    0b00111,
    0b00111,
    0b00000,
    0b00000,
    0b00000,
)

mouthrightclose = (
    0b00000,
    0b00000,
    0b00000,
    0b11100,
    0b11100,
    0b0000,
    0b00000,
    0b00000,
)
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

def sleeping():
    play(song)
    lcd.create_char(0, empty)
    lcd.create_char(1, lefttopcorner)
    lcd.create_char(2, righttopcorner)

    lcd.create_char(3, rightbottomcorner)
    lcd.create_char(4, leftbottomcorner)

    lcd.create_char(5, mouthleftopen)
    lcd.create_char(6, mouthrightopen)

    draw()
    sleep(2)
    play(song)
    lcd.create_char(0, empty)
    lcd.create_char(1, lefttopcorner)
    lcd.create_char(2, righttopcorner)

    lcd.create_char(3, rightbottomcorner)
    lcd.create_char(4, leftbottomcorner)

    lcd.create_char(5, mouthleftclose)
    lcd.create_char(6, mouthrightclose)

    draw()
    sleep(2)
try:
    sleeping()
except KeyboardInterrupt:
    destroy()
