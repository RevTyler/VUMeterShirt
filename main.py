import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 5)

pixels.fill((0, 128, 0))
pixels.show()