#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import HappyFaceAnimated

# Welcome message
print ("Don't worry Be happy")
try:
    HappyFaceAnimated.HappyFaceAnimated.loop()
    GPIO.cleanup()
except:
    print('error')
