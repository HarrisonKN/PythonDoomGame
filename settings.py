import math

RES = WIDTH, HEIGHT = 1920, 1040
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2 
FPS = 500

PLAYER_POS = 1.5,5
PLAYER_ANGLE = 0
PLAYER_PITCH = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002
PLAYER_SIZE_SCALE = 60

MOUSE_SENSITIVITY = 0.0002
MOUSE_MAX_REL = 40
MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT 
MOUSE_BORDER_TOP = 100
MOUSE_BORDER_BOTTOM = HEIGHT - MOUSE_BORDER_TOP

FLOOR_COLOR = (30,30,30)

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2