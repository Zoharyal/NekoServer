#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import Eatting
loop = 0

Eatting.Eating.loop()

GPIO.cleanup()
