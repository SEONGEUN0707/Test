import pymunk
import pygame
import sys

# 화면 크기 및 색상 설정
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
BACKGROUND_COLOR = (255, 255, 255)
BALL_COLOR = (50, 50, 200)

# 초기화
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pymunk Tutorial")

# Pymunk 공간 생성
space = pymunk.Space()
space.gravity = (0, 1000)  # 중력 설정

# 바닥 생성
ground = pymunk.Segment(space.static_body, (0, SCREEN_HEIGHT), (SCREEN_WIDTH, SCREEN_HEIGHT), 5)
ground.friction = 1.0
space.add(ground)

# 공 생성
radius = 20
ball_mass = 1
ball_moment = pymunk.moment_for_circle(ball_mass, 0, radius)
ball_body = pymunk.Body(ball_mass, ball_moment)
ball_body.position = (SCREEN_WIDTH // 2, 50)
ball_shape = pymunk.Circle(ball_body, radius)
ball_shape.friction = 0.7
space.add(ball_body, ball_shape)

# 시뮬레이션 루프
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 시뮬레이션 업데이트
    dt = 1.0 / 60.0  # 시뮬레이션 스텝 간격
    space.step(dt)

    # 화면 업데이트
    screen.fill(BACKGROUND_COLOR)

    # 공 그리기
    ball_position = int(ball_body.position.x), int(SCREEN_HEIGHT - ball_body.position.y)
    pygame.draw.circle(screen, BALL_COLOR, ball_position, radius)

    # 바닥 그리기
    pygame.draw.line(screen, (0, 0, 0), (0, SCREEN_HEIGHT), (SCREEN_WIDTH, SCREEN_HEIGHT), 5)

    pygame.display.flip()
    clock.tick(60)  # FPS 설정