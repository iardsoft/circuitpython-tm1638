"""CircuitPython TM1638 example"""
import tm1638
import time
import board
from digitalio import DigitalInOut, Direction

# TM1638 Keyboard & LED setup.
stb = DigitalInOut(board.GP21)
stb.direction = Direction.OUTPUT
clk = DigitalInOut(board.GP20)
clk.direction = Direction.OUTPUT
dio = DigitalInOut(board.GP19)
dio.direction = Direction.OUTPUT

kled = tm1638.TM1638(stb, clk, dio, brightness=2)

# blink all leds
for i in range(8):
    kled.led(i, 1)
    time.sleep(0.5)
    kled.led(i, 0)

# display text
kled.show("PICO2021")

# change brightness
for i in range(5):
    kled.brightness(i)
    time.sleep(0.5)
kled.brightness(2)
time.sleep(0.5)
kled.clear()

# display number
kled.number(-1234567)
time.sleep(1.5)
kled.clear()

# led combinations
kled.leds(170)
time.sleep(0.5)
kled.leds(85)
time.sleep(0.5)
kled.leds(170)
time.sleep(0.5)
kled.leds(85)
time.sleep(0.5)
kled.clear()

# scroll text
kled.scroll("ABC DEF 123 456 789")
kled.clear()

# display temperature and humidity
kled.temperature(25)
kled.humidity(45)
time.sleep(1.5)
kled.clear()

# wait for a key press and activate corresponding led
while True:
    kled.leds(kled.keys())
