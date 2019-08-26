#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import Dance

# Welcome message
print ("let's dance")

try:
    Dance.Dance.draw()
except:
    print('error')
