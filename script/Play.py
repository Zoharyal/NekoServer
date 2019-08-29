from RPLCD.i2c import CharLCD
import time
from time import sleep
import os
from pydub import AudioSegment
from pydub.playback import play
fileName = os.path.abspath('script/envoieleballon.wav')
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
    0b00011,
    0b00100,
    0b01000,
    0b01000,
    0b10111,
    0b11000,
    0b10000,
)

middletop = (
    0b11111,
    0b00100,
    0b00010,
    0b00001,
    0b00000,
    0b10000,
    0b01100,
    0b00010,
)

righttopcorner = (
    0b00000,
    0b11000,
    0b00100,
    0b10010,
    0b01010,
    0b00101,
    0b00011,
    0b00001,
)


leftbottomcorner = (
    0b10000,
    0b10000,
    0b01000,
    0b01000,
    0b00100,
    0b00011,
    0b00000,
    0b00000,
)
middlebottom = (
    0b00001,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b11111,
    0b00000,
)

rightbottomcorner = (
    0b00001,
    0b10001,
    0b10011,
    0b01010,
    0b01100,
    0b11000,
    0b00000,
    0b00000,
)

def destroy():
    lcd.clear()

def draw():
    # premire ligne
    lcd.write_string('\x00')
    lcd.write_string('\x00')
    lcd.write_string('\x00')
    lcd.write_string('\x01')
    lcd.write_string('\x02')
    lcd.write_string('\x03')
    lcd.write_string('\x00')
    lcd.write_string('\x00')
    lcd.write_string('\x00')
    lcd.write_string('\x00')
    lcd.write_string('\x01')
    lcd.write_string('\x02')
    lcd.write_string('\x03')
    lcd.write_string('\x00')
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
    lcd.write_string('\x04')
    lcd.write_string('\x05')
    lcd.write_string('\x06')
    lcd.write_string('\x00')
    lcd.write_string('\x00')
    lcd.write_string('\x00')
    lcd.write_string('\x00')
    lcd.write_string('\x04')
    lcd.write_string('\x05')
    lcd.write_string('\x06')
    lcd.write_string('\x00')
    lcd.write_string('\x00')
    lcd.write_string('\x00')

try:
    lcd.create_char(0, empty)
    lcd.create_char(1, lefttopcorner)
    lcd.create_char(2, middletop)
    lcd.create_char(3, righttopcorner)
    lcd.create_char(4, leftbottomcorner)
    lcd.create_char(5, middlebottom)
    lcd.create_char(6, rightbottomcorner)
    draw()
    play(song)
    sleep(5)
    destroy()
except KeyboardInterrupt:
    destroy()
