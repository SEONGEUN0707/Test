import pymunk
import pymunk.pygame_util
import pygame
import sys

fps = 60
dt = 1/fps

pygame.init()

WIDTH, HEIGHT = 1000, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))

def create_Ball(space, r, m):
    ball = pymunk.

def run(window, width, height):
    run = True
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0,100)

    ball = create_Ball(space,30,10)
    create_boundaries(space, width, height)

    draw_options = pymunk.pygame_util.DrawOptions(window)
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
                sys.exit()
        
        draw(space, window, draw_options)
        space.step(dt)
        clock.tick(fps)

if __name__ == "__main__":
    run(window, WIDTH, HEIGHT)