from RPLCD.i2c import CharLCD
import time
import os
import RPi.GPIO as GPIO
from time import sleep
from pydub import AudioSegment
from pydub.playback import play
lcd = CharLCD('PCF8574', 0x27)
ledRedPin = 13      #define 3 pins of RGBLED
ledGreenPin = 16
ledBluePin = 37
fileName = os.path.abspath('script/faidubien.wav')
song = AudioSegment.from_wav(fileName)
global p_Red,p_Green,p_Blue
GPIO.setmode(GPIO.BOARD)
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
    0b01111,
    0b01000,
    0b01001,
    0b01000,
    0b01001,
    0b01001,
    0b01010,
    0b01010,
)

middletop = (
    0b11000,
    0b01000,
    0b11111,
    0b00000,
    0b00010,
    0b11110,
    0b00001,
    0b10011,
)

middlebottom = (
    0b00001,
    0b11110,
    0b00000,
    0b00000,
    0b00000,
    0b11111,
    0b00000,
    0b00000,
)

leftbottomcorner = (
    0b11110,
    0b10001,
    0b01000,
    0b01000,
    0b00100,
    0b00011,
    0b00000,
    0b00000,
)
rightbottomcorner = (
    0b11111,
    0b00001,
    0b00010,
    0b00010,
    0b00100,
    0b11000,
    0b00000,
    0b00000,
)
mouthleft = (
    0b00011,
    0b01101,
    0b01001,
    0b01001,
    0b01001,
    0b01011,
    0b11011,
    0b11000,
)



def destroy():
    lcd.clear()
    GPIO.cleanup()

def draw():
    # premire ligne
    lcd.write_string('\x00')
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
    lcd.write_string('\x01')
    lcd.write_string('\x02')
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
    lcd.write_string('\x03')
    lcd.write_string('\x04')
    lcd.write_string('\x05')
    lcd.write_string('\x00')
    lcd.write_string('\x00')
    lcd.write_string('\x06')
    lcd.write_string('\x00')
    lcd.write_string('\x00')
    lcd.write_string('\x03')
    lcd.write_string('\x04')
    lcd.write_string('\x05')
    lcd.write_string('\x00')
    lcd.write_string('\x00')

try:
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
    lcd.create_char(0, empty)
    lcd.create_char(1, lefttopcorner)
    lcd.create_char(2, middletop)
    lcd.create_char(3, leftbottomcorner)
    lcd.create_char(4, middlebottom)
    lcd.create_char(5, rightbottomcorner)
    lcd.create_char(6, mouthleft)
    play(song)
    draw()
    sleep(5)
    destroy()
except KeyboardInterrupt:
    destroy()
