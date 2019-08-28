#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import WakeupAnimated

# Welcome message
print ("Wake up")

try:
    WakeupAnimated.WakeupAnimated.loop()
    GPIO.cleanup()
except:
    print('error')
