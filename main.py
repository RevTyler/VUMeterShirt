import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 50, brightness=0.5, pixel_order=neopixel.GRB)

pixels.fill(0, 255, 0)
pixels.show()