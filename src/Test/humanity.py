# This file has been written to your home directory for convenience. It is
# saved as "/home/pi/humidity-2021-04-10-23-06-55.py"

from sense_emu import SenseHat

sense = SenseHat()

green = (0, 255, 0)
red = (255,0,0)
blue = (0,0,255)
white = (255, 255, 255)
grey = (128,128,128)

while True:
    humidity = sense.humidity
    temp = sense.temperature
    pressure=sense.pressure

    # convert to num no more than 16
    humidity_value = 16 * humidity / 100
    temp_value = 16 * (temp+30) / 135
    pressure_value = 16 * (pressure-260) / (1260-260)

    pixels1 = [red if i < temp_value else white for i in range(16)]
    pixels2 = [blue if i < pressure_value else white for i in range(16)]
    pixels3 = [green if i < humidity_value else white for i in range(16)]
    pixels4 = [grey for i in range(16)]
    pixels=pixels1+pixels2+pixels3+pixels4
    sense.set_pixels(pixels)
    