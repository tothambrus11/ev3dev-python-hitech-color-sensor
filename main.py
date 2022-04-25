#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, Sensor
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds

from htcolor import *

from ev3dev2 import *

#cl = Sensor("ev3-ports:in1:i2c1", driver='ht-nxt-color-v2')


sensor = HTColor(1)

while True:
    sensor.read()
    print(sensor.sees_red(), sensor.hue, sensor.saturation)

