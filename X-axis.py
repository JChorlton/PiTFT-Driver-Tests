import os
import pygame
import time

# Initialize environment variables 
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV' , '/dev/fb1')
os.putenv('SDL_MOUSEDRV' , 'TSLIB')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

# Initialize pygame and screen
pygame.init()
pygame.mouse.set_visible(False)
(width, height) = pygame.display.list_modes(0)[0]
screen = pygame.display.set_mode((width, height))

font_big = pygame.font.Font(None, 100)

count = 0
last_x = 0

def DrawNumber(nr):
    screen.fill((255, 255, 255))
    text_surface = font_big.render("{0}".format(count), True, (0,0,0))
    rect = text_surface.get_rect(center=(width/2,height/2))
    screen.blit(text_surface, rect)
    pygame.display.update()

DrawNumber(0)
while True:
    for event in pygame.event.get():
        cur_x = pygame.mouse.get_pos()[0]

        if event.type is pygame.MOUSEBUTTONDOWN:
            last_x = cur_x
            print "Touched at x: {0}".format(cur_x)
        elif event.type is pygame.MOUSEBUTTONUP:
            last_x = 0
            print "Released at x: {0}".format(cur_x)
        elif event.type is pygame.MOUSEMOTION:
            print "Movement to x: {0}".format(cur_x)

            delta_x = cur_x - last_x
            if delta_x > 0:
              count = count + 1
              print "count + 1"
            elif delta_x < 0:
              count = count - 1
              print "count - 1"

            DrawNumber(count)

            last_x = cur_x
