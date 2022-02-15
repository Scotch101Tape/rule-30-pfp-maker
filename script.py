import random
import math
from PIL import Image

PFP_SIZE = 1024
SQUARE_SIZE = 64
CELLS_SIZE = PFP_SIZE // SQUARE_SIZE
RULES = [(True, False, False), (False, True, False), (False, False, True), (False, True, True)]

def write_square(picture, m, n):
  for x in range(SQUARE_SIZE):
    for y in range(SQUARE_SIZE):
      px = x + m * SQUARE_SIZE
      py = y + n * SQUARE_SIZE
      picture.putpixel(
        (x + m * SQUARE_SIZE, y + n * SQUARE_SIZE), 
        (round(px * (220 / PFP_SIZE)) + 35, 0, round(py * (220 / PFP_SIZE)) + 35)
      )

def on_or_off(above_cells_array, i):
  if i == 0:
    above = (False, above_cells_array[i], above_cells_array[i + 1])
  elif i == CELLS_SIZE - 1:
    above = (above_cells_array[i - 1], above_cells_array[i], False)
  else:
    above = (above_cells_array[i - 1], above_cells_array[i], above_cells_array[i + 1])

  return above in RULES

cells = [[False for _ in range(CELLS_SIZE)] for _ in range(CELLS_SIZE)]

pfp = Image.new('RGB', (PFP_SIZE, PFP_SIZE))

for i in range(CELLS_SIZE):
  if bool(random.getrandbits(1)):
    cells[0][i] = True
    write_square(pfp, i, 0)

for x in range(1, CELLS_SIZE):
  for y in range(CELLS_SIZE):
    if on_or_off(cells[x - 1], y):
      write_square(pfp, y, x)
      cells[x][y] = True

pfp.save("pfp.png")
