from machine import Pin, PWM
from pixels import Neopixel
import time
import random

##################################################### Defining All Variables and constants that are used #####################################################

PIXELPIN = 6

#Setup the neopixel object 
WIDTH = 8
HEIGHT = 16
NUMPIXELS = WIDTH * HEIGHT

pixels = Neopixel(NUMPIXELS, 0, PIXELPIN)

#Defining the colors

NR_COLORS = 6

g_colors = [    [0, 0, 0], # color 0 is black (blank)
    [255, 255, 255], # color 1 is white
    [0, 0, 60], # rest of the NR_COLORS are used for the blocks
    [0, 50, 0],
    [50, 0, 0], 
    [0, 30, 60],
    [30, 50, 0],
    [30, 0, 30]
]

NR_SHAPES = 7


# there are 7 different shapes, we put them in a constant array in four orientations 
# [shape_id][orientation][y][x]
g_shapes = [
    [
        [
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        [
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0]
        ],
        [
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        [
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0]
        ]
    ],
    [
        [
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        [
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        [
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        [
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
    ],
    [
        [
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        [
            [0, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0]
        ],
        [
            [0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        [
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0]
        ]
    ],
    [
        [
            [1, 1, 1, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        [
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0]
        ],
        [
            [0, 0, 1, 0],
            [1, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],  
        [
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]
        ]
    ],
    [
        [
            [1, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        [
            [0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]
        ],
        [
            [1, 0, 0, 0],
            [1, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        [
            [0, 1, 1, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0]
        ]
    ], 
    [
        [
            [1, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        [
            [0, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0]
        ],
        [
            [1, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        [
            [0, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0]
        ]
    ],
    [
        [
            [0, 1, 1, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        [
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0]
        ],
        [
            [0, 1, 1, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        [
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0]
        ]
    ]
]
# position, color, orientation and shape_id of the block that is falling downs


# Define constants
NR_COLORS = 5

Button_LEFT = Pin(7)
Button_RIGHT = Pin(8)
Button_UP = Pin(10)
Button_DOWN = Pin(9)

# Define variables
block_x = 0
block_y = 0
block_color = NR_COLORS - 1
block_orientation = 0
block_shape = 0

# Define grid the grid contains the pixels of the blocks that are already on the screen the falling block is not part of the grid 
grid = [[0] * WIDTH for i in range(HEIGHT)]



previousMoveTime = 0
previousFullLineTime = 0

state = {"left": 0, "right": 0, "up": 0, "down": 0}

level = 800  # start off with 300ms drops

falling_down = False

##################################################### Defining all Functions that are used #####################################################

# Define function to set pixel color
def setPixelRGB(y, x, r, g, b):
  global pixels
  global index
  if (y >= 0) and (y < HEIGHT):
      index = (HEIGHT * WIDTH) - 1 - (y * WIDTH) - x
      pixels[index] = (r, g, b)

# Define function to set pixel color using a color table
def setPixel(y, x, color):
  r = g_colors[color][0]
  g = g_colors[color][1]
  b = g_colors[color][2]
  setPixelRGB(y, x, r, g, b)

# Define function to perform a flashclean effect
def flashclean():
  global pixels
  # Define constant
  tail = 5

  # Loop through rows and columns of grid
  for y in range(HEIGHT + 2):
    for x in range(WIDTH):
       # Loop through tail of flashclean effect
       for t in range(tail):
          # Calculate color value
          c = 255 >> t
          if t == (tail - 1):
            c = 0
          # Set pixel color
          setPixelRGB(y - t, x, c, c, c)

    # Show pixels on screen
    pixels.show()

    # Delay for 10 ms
    time.sleep_ms(10)


# Define function to clear grid
def clearGrid():
  global grid
  # Loop through columns and rows of grid
  for x in range(WIDTH):
    for y in range(HEIGHT):
      # Set grid cell to black
      grid[y][x] = 0

# Define function to initialize a block
def initBlock():
    global block_x
    global block_y
    global block_color
    global block_shape
    # Set block position
    block_x = WIDTH // 2 - 2
    block_y = 0

  # Set block color
    block_color = ((block_color - 1) % NR_COLORS) + 2 # The first two colors defined in g_color are skipped because those are black and white!

  # Set block shape
    block_shape = random.randint(0,NR_SHAPES)

def canMoveTo(x, y, orientation):
  global grid
  # Loop through rows and columns of block shape
  for dx in range(4):
    for dy in range(4):
      # Check if block shape cell is occupied
      if g_shapes[block_shape-1][orientation][dy][dx]:
        # Calculate block position
        xx = x + dx
        yy = y + dy

        # Check if block is outside grid
        if (xx < 0) or (xx >= WIDTH) or (yy < 0) or (yy >= HEIGHT):
          return False

        # Check if grid cell is occupied
        if grid[yy][xx] != 0:
          return False

  # Return true if all checks pass
  return True


# Define function to check if block can move down
def canMoveDown():
  global block_x
  global block_y
  global block_orientation
  return canMoveTo(block_x, block_y + 1, block_orientation)

# Define function to check if block can move left
def canMoveLeft():
  global block_x
  global block_y
  global block_orientation
  return canMoveTo(block_x - 1, block_y, block_orientation)

# Define function to check if block can move right
def canMoveRight():
  global block_x
  global block_y
  global block_orientation
  return canMoveTo(block_x + 1, block_y, block_orientation)

# Define function to check if block can rotate
def canRotate():
  global block_x
  global block_y
  global block_orientation
  return canMoveTo(block_x, block_y, (block_orientation + 1) % 4)


# Define function to check if block can rotate after shifting
def canRotateShift(i):
  global block_x
  global block_y
  global block_orientation
  return canMoveTo(block_x + i, block_y, (block_orientation + 1) % 4)

# Define function to drop block on grid
def dropOnGrid():
  global grid
  # Loop through rows and columns of block shape
  for dx in range(4):
    for dy in range(4):
      # Check if block shape cell is occupied
      if g_shapes[block_shape-1][block_orientation][dy][dx]:
        # Calculate block position
        xx = block_x + dx
        yy = block_y + dy

        # Set grid cell to block color
        grid[yy][xx] = block_color

  # Return false (for compatibility with Arduino code)
  return False

  # Define function to check if line is full
def isFullLine(y):
  # Loop through columns of grid
  for x in range(WIDTH):
    # Check if grid cell is empty
    if grid[y][x] < 2:
      # Return false if empty cell is found
      return False

  # Return true if all cells are occupied
  return True

# Define function to check if line is highlighted
def isHighlightedLine(y):
  # Loop through columns of grid
  for x in range(WIDTH):
    # Check if grid cell is not highlighted
    if grid[y][x] != 1:
      # Return false if unhighlighted cell is found
      return False

  # Return true if all cells are highlighted
  return True

# Define function to delete line from grid
def deleteLineFromGrid(d):
  global grid
  # Loop through rows of grid
  for y in range(d, 1, -1):
    # Loop through columns of grid
    for x in range(WIDTH):
      # Shift rows down
      grid[y][x] = grid[y - 1][x]

# Define function to draw grid
def drawGrid():
  # Loop through columns and rows of grid
  for x in range(WIDTH):
    for y in range(HEIGHT):
      # Set pixel color from grid
      setPixel(y, x, grid[y][x])


# Define function to draw block in a given color
def drawBlockInColor(color):
  # Loop through rows and columns of block shape
  for dx in range(4):
    for dy in range(4):
      # Check if block shape cell is occupied
    
      if g_shapes[block_shape-1][block_orientation][dy][dx]:
        # Calculate block position
        xx = block_x + dx
        yy = block_y + dy

        # Set pixel color
        setPixel(yy, xx, color)

# Define function to draw block
def drawBlock():
  global block_color
  # Draw block in block color
  drawBlockInColor(block_color)

# Define function to erase block
def eraseBlock():
  # Draw block in black
  drawBlockInColor(0)

# Define function to highlight block
def highlightBlock():
  # Draw block in bright white
  drawBlockInColor(1)

# Define function to highlight line
def highlightLine(y):
  global grid
  # Loop through columns of grid
  for x in range(WIDTH):
    # Set grid cell to bright white
    grid[y][x] = 1


def moveDown():
  global block_y
  block_y += 1

def moveLeft(i=1):
  global block_x
  block_x -= i

def moveRight(i=1):
  global block_x
  block_x += i

def rotate():
  global block_orientation
  block_orientation = (block_orientation + 1) % 4

def setup():
  pixels.clear()
  initBlock()

  Button_LEFT.init(mode=Pin.IN, pull=Pin.PULL_UP) # button left
  Button_RIGHT.init(mode=Pin.IN, pull=Pin.PULL_UP) # button right
  Button_UP.init(mode=Pin.IN, pull=Pin.PULL_UP) # button up
  Button_DOWN.init(mode=Pin.IN, pull=Pin.PULL_UP) # button down

# this is some lazy way to debounce.    Since there is a lot of stuff in the loop, it kind of works. 
def buttonPressed(pin, btn):
  global state
  treshold = 4
  if pin.value() == 1:  # button is up
      state[btn] = 0
      return False
  else: # button down
      state[btn] += 1
      return state[btn] == treshold  # we only return the Pressed result once


def buttonLeftPressed():
  return buttonPressed(Button_LEFT, "left")

def buttonRightPressed():
  return buttonPressed(Button_RIGHT, "right")

def buttonUpPressed():
  return buttonPressed(Button_UP, "up")

def buttonDownPressed():
  return buttonPressed(Button_DOWN, "down")


def loop():
  global previousMoveTime
  global previousMoveTime
  global previousFullLineTime
  global previousLeft
  global previousRight
  global previousUp
  global previousDown
  global level
  global falling_down
  eraseBlock()
  if buttonLeftPressed() and canMoveLeft():
    moveLeft()
  if buttonRightPressed() and canMoveRight():
    moveRight()
  if buttonUpPressed():
    # first try to just rotate
    if canRotate():
      rotate()
      
    else:
      #  
      for i in range(1, -3, -1):
        if canRotateShift(i):
          moveRight(i)
          rotate()
          break
  if buttonDownPressed():
    falling_down = True
  
  if (time.ticks_ms() - previousMoveTime >= level) or falling_down:
    if canMoveDown(): 
      moveDown()
    else:
      falling_down = False
      dropOnGrid()
      drawGrid()
      if block_y<4:
        flashclean()   
        # game over  
        clearGrid()
        drawGrid()
        # reset the interval back to 300ms 
        level = 800
      initBlock()  
    previousMoveTime = time.ticks_ms()

  if time.ticks_ms() - previousFullLineTime >= 50:
    for y in range(HEIGHT):
      if isHighlightedLine(y):
        deleteLineFromGrid(y) 
        drawGrid()

  for y in range(HEIGHT):
    if isFullLine(y):
      highlightLine(y)
      drawGrid()
      previousFullLineTime = time.ticks_ms()
      # make blocks drop a little (2ms) faster 
      level = level - 2

  drawBlock() 
  pixels.show()



##################################################### Running The Code #####################################################
setup()
while True:
    loop()





