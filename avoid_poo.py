import pygame
import random

#초기화
pygame.init()

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#배경 설정
background = pygame.image.load("background.png")

#제목 설정
pygame.display.set_caption("Avoiding poo")

clock = pygame.time.Clock()


#종료 버튼 눌렀을 때 꺼지기
running = True
_running = True
while _running:
    #캐릭터 속도 설정
    character_speed = 0.5
    
    poo_speed = 1
    #캐릭터 생성
    character = pygame.image.load("character.png")
    character_size = character.get_rect().size #이미지 사이즈 구하기
    character_width = character_size[0] #캐릭터 가로 
    character_height = character_size[1] #캐릭터 세로
    character_xpos = screen_width/2-character_width/2
    character_ypos = screen_height - character_height

    #똥 생성
    poo = pygame.image.load("poo.jpg")
    poo_size = poo.get_rect().size
    poo_width = poo_size[0]
    poo_height = poo_size[1]
    poo_xpos = 0
    poo_ypos = poo_height



    game_font = pygame.font.Font(None,40)

    start_ticks = pygame.time.get_ticks()


    to_x = 0
    while running:
        dt = clock.tick(60)
        print("fps:",str(clock.get_fps()))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_x -= character_speed
                if event.key == pygame.K_RIGHT:
                    to_x += character_speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x = 0
                    to_y = 0
        character_xpos += to_x * dt
        if character_xpos < 0:
            character_xpos = 0
        elif character_xpos > screen_width - character_width:
            character_xpos = screen_width - character_width
        if character_ypos < 0:
            character_ypos = 0
        elif character_ypos > screen_height - character_height:
            character_ypos = screen_height - character_height
        if poo_ypos >= screen_height + 70 or poo_ypos == 70:
            poo_ypos =  poo_height
            poo_xpos = random.uniform(0,screen_width - character_width)
        
        poo_ypos += poo_speed
        poo_speed += 0.01
        character_rect = character.get_rect()
        character_rect.left = character_xpos
        character_rect.top = character_ypos

        poo_rect = character.get_rect()
        poo_rect.left = poo_xpos
        poo_rect.top = poo_ypos

        if character_rect.colliderect(poo_rect):
            print("You die")
            running = False
        
        elapsed_time = (pygame.time.get_ticks() - start_ticks)/1000 #경과시간 밀리세컨드 이므로 100으로 나눠 표시
        timer = game_font.render(str(int(elapsed_time)),True,(255,255,255))

        
        screen.blit(background,(0,0)) #
        screen.blit(character,(character_xpos,character_ypos))
        screen.blit(poo,(poo_xpos,poo_ypos))
        screen.blit(timer,(10,10))
        pygame.display.update() #화면 새로고침
    score_font = pygame.font.Font(None,50)
    text = score_font.render("Your score",True,(255,255,255))
    info = score_font.render("Press r key to restart.",True, (255,255,255))
    text_rect = text.get_rect()
    info_rect = info.get_rect()
    timer_rect = timer.get_rect()
    screen.fill((0,0,0))
    screen.blit(timer,(10,50))
    screen.blit(info,(10,80))
    screen.blit(text,(10,10))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            _running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                running = True


#pygame 종료
pygame.quit()