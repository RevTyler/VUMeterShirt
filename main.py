import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 5, brightness=0.5, pixel_order=neopixel.GRB)

pixels[0] = (255, 0, 0)
pixels[1] = (0, 255, 0)
pixels[2] = (0, 0, 255)
pixels.show()