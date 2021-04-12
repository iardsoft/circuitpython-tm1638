# circuitpython-tm1638

CircuitPython driver for TM1638 Led &amp; Key modules. Adapted to work on CircuitPython from MicroPython TM1638 LED Driver by mcauser https://github.com/mcauser/micropython-tm1638

Tested on Raspberry Pi Pico with CircuitPython 6.2

## Usage

Copy the tm1638.py file to the board. Also copy the code below to code.py, using your favorite editor and file manager, or using [Mu editor](https://codewith.mu). The example assumes a TM1638 Led&Key module connected to a Raspberry Pi Pico (see next section)

```python
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
```

## Connections

Raspberry Pi Pico   | LED&KEY TM1638 Module
-----------------   | ---------------------
3V3(OUT) - pin 36   | VCC
GND - pin 28        | GND
GP21 - pin 27       | STB
GP20 - pin 26       | CLK
GP19 - pin 25       | DIO

## Links

* [MicroPython TM1638 LED Driver](https://github.com/mcauser/micropython-tm1638)
* [circuitpython.org](https://circuitpython.org)
* [Mu editor](https://codewith.mu)
* [Adafruit CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython)

## License

Licensed under the [MIT License](http://opensource.org/licenses/MIT).
