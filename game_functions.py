from curses import KEY_DOWN
import sys
import pygame

def check_events(ship):

    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #move the ship to right
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                #move the ship to left
                ship.moving_left = True    

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False 
            if event.key == pygame.K_LEFT:
                ship.moving_left = False       

def update_screen(ai_settings, screen, ship):
    #redraw the screen 
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #make most recently drawn screen visible
    pygame.display.flip()            