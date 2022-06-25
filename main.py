import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 5, brightness=0.5, pixel_order=neopixel.GRB)

pixels[0] = (200, 0, 0)
time.sleep(0.5)
pixels[0] = (0, 200, 0)
time.sleep(0.5)
pixels[0] = (0, 0, 200)
time.sleep(0.5)
pixels[0] = (200, 200, 0)
time.sleep(0.25)
pixels[0] = (200, 0, 0)
time.sleep(0.25)
pixels[0] = (200, 200, 0)
time.sleep(0.5)
pixels.show()