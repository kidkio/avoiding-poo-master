import pygame

#초기화
pygame.init()

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#배경 설정
background = pygame.image.load("background.png")

#제목 설정
pygame.display.set_caption("test pygame")

clock = pygame.time.Clock()

#캐릭터 속도 설정
character_speed = 0.5

poo = pygame.image.load("poo.png")
poo_size = poo.get_rect().size
poo_width = poo_size[0]
poo_height = poo_size[1]
poo_xpos = screen_width/2 - poo_width/2
poo_ypos = screen_height/2 - poo_height/2

#캐릭터 생성
character = pygame.image.load("character.png")
character_size = character.get_rect().size #이미지 사이즈 구하기
character_width = character_size[0] #캐릭터 가로 
character_height = character_size[1] #캐릭터 세로
character_xpos = screen_width/2-character_width/2
character_ypos = screen_height - character_height

game_font = pygame.font.Font(None,40)

total_time = 10
start_ticks = pygame.time.get_ticks()


to_x = 0
to_y = 0
#종료 버튼 눌렀을 때 꺼지기
running = True
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
            if event.key == pygame.K_UP:
                to_y -= character_speed
            if event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    character_xpos += to_x * dt
    character_ypos += to_y * dt
    if character_xpos < 0:
        character_xpos = 0
    elif character_xpos > screen_width - character_width:
        character_xpos = screen_width - character_width
    if character_ypos < 0:
        character_ypos = 0
    elif character_ypos > screen_height - character_height:
        character_ypos = screen_height - character_height
    
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

#pygame 종료
pygame.quit()



