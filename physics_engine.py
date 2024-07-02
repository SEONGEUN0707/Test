import pymunk
import pymunk.pygame_util
import pygame
import math
import sys

fps = 60
dt = 1/fps

pygame.init()

WIDTH, HEIGHT = 1000, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))

#마우스가 그리는 선 길이
def calculate_distance(p1,p2):
    return math.sqrt((p2[1] - p1[1])**2 + (p2[0] - p1[0])**2)

#그 길이 앵글
def calculate_angle(p1,p2):
    return math.atan2(p2[1] - p1[1] , p2[0] - p1[0])

#배경 그리기
def draw(space, window, draw_options,line):
    window.fill("white")

    if line:
        pygame.draw.line(window, "black", line[0], line[1], 3)#3은 두께

    space.debug_draw(draw_options)
    pygame.display.update()

#배경 벽
def create_boundaries(space, width, height):
    rects = [
        [(width / 2, height - 10), (width, 20)],
        [(width / 2, 10), (width, 20)],
        [(10, height / 2), (20, height)],
        [(width - 10, height / 2), (20, height)] 
    ]

    for pos, size in rects:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)

#볼1 만들기
def create_Ball(space, radius, mass, pos):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.elasticity = 0.9
    shape.friction = 0.4
    shape.color = (255, 0 ,0, 100)
    space.add(body, shape)
    return shape

#main
def run(window, width, height):
    run = True
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0,1000)

    create_boundaries(space, width, height)

    draw_options = pymunk.pygame_util.DrawOptions(window)

    pressed_pos = None
    ball = None
    
    while run:
        line = None
        if ball and pressed_pos:
            line = [pressed_pos,pygame.mouse.get_pos()]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not ball:
                    pressed_pos = pygame.mouse.get_pos()
                    ball = create_Ball(space, 30, 100, pressed_pos)
                elif pressed_pos:
                    ball.body.body_type = pymunk.Body.DYNAMIC
                    angle = calculate_angle(*line)
                    force = calculate_distance(*line)*500
                    fx = math.cos(angle)*force
                    fy = math.sin(angle)*force
                    ball.body.apply_impulse_at_local_point((fx, fy), (0,0))
                    pressed_pos = None
                else:
                    space.remove(ball, ball.body)
                    ball = None

        draw(space, window, draw_options, line)

        space.step(dt)
        clock.tick(fps)

#인터프리터에서 직접 실행시 실행
if __name__ == "__main__":
    run(window, WIDTH, HEIGHT)
