import pygame

# - 기본 framework

pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Game")

# FPS
clock = pygame.time.Clock()
# -

# - 사용자 정의









# 이벤트 루프
running = True

while running:
    dt = clock.tick(30)

    # 이벤트 처리 (키보드, 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #  게임 캐릭터 위치 정의


    # 충돌 처리



    # 화면 출력


    pygame.display.update()

pygame.quit()