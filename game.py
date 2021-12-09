import pygame, sys
import random
# 初始化
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("bgm.mp3")
pygame.mixer.music.play()

bomb_sound = pygame.mixer.Sound("炸弹.wav")
gameover_sound = pygame.mixer.Sound("gameover.wav")
pass_sound = pygame.mixer.Sound("通关.wav")
first_sound = pygame.mixer.Sound("firstblood.wav")
second_sound = pygame.mixer.Sound("doublekill.wav")
scored_sound = pygame.mixer.Sound("得分.wav")

pygame.mixer.music.set_volume(1)

size = width, height = 800, 400
speed = [10, 10]
SCREEN = pygame.display.set_mode(size)
pygame.display.set_caption('PYGAME')
bomb = pygame.image.load('bomb.png')
#bombrect = bomb.get_rect()
random_coin = 0
coin = pygame.image.load('coin.png')
decoin = pygame.image.load('bomb.png')
#coinrect = coin.get_rect()
player = pygame.image.load("校长.png")
#playerrect = player.get_rect()
background = pygame.image.load('startbg.png')

player_location = [336, 272]
coin_location = [[random.randint(0, 750), 0]]
coin_style = [0, 0, 0, 0]
score = 0
pygame.font.init()
myfont = pygame.font.Font(None, 40)
live = True
level = 1
coinrect = [0, 0, 0]
victory = False
sounded = False
fps = 100
fclock = pygame.time.Clock()
frame = True

while frame:
    for event in pygame.event.get():
        # 处理退出事件
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key_list = pygame.key.get_pressed()
            if key_list[pygame.K_SPACE]:
                frame = False
    SCREEN.blit(background, (0,0))
    firstImages = pygame.font.Font(None, 100).render("Gold Game", True, (255,0,0))
    firstImage = myfont.render("Press the key [space] to start game", True, (0, 0, 255))
    SCREEN.blit(firstImage, (180,250))
    SCREEN.blit(firstImages, (220,100))
    pygame.display.update()
    fclock.tick(fps)

while live:
    for event in pygame.event.get():
        # 处理退出事件
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # 键盘按下事件
        elif event.type == pygame.KEYDOWN:
            key_list = pygame.key.get_pressed()
            if key_list[pygame.K_LEFT]:
                player_location[0] -= 30
            elif key_list[pygame.K_RIGHT]:
                player_location[0] += 30
    for i in range(len(coin_location)):
        coinrect[i] = (pygame.Rect(coin_location[i][0], coin_location[i][1], 50, 50))
    if score == 3:
        level += 1
        if(level == 2):
            first_sound.play()
        if(level == 3):
            second_sound.play()
        score = 0
        coinrect = [0, 0, 0, 0]
        coin_location.append([random.randint(0, 750), 0])
        for i in range(len(coin_location)):
            coinrect[i] = pygame.Rect(coin_location[i][0], coin_location[i][1], 50, 50)
    if(level == 4):
            live = False
            victory = True
    for i in range(len(coin_location)):
        coin_location[i][1] += 3
    textImage = myfont.render("score: " + str(score), True, (0, 0, 255))
    textImageL = myfont.render("level: " + str(level), True, (0, 0, 255))
    #textImageM = myfont.render("life: " + str(live), True, (0, 0, 255))
    SCREEN.blit(background, (0,0))
    SCREEN.blit(textImage, (10, 10))
    SCREEN.blit(textImageL, (520, 10))
    #SCREEN.blit(textImageM, (265, 10))
    for i in range(len(coin_location)):
        if coin_style[i] <= 30:
            SCREEN.blit(coin, coin_location[i])
        else:
            SCREEN.blit(decoin, coin_location[i])
    SCREEN.blit(player, player_location)
    for i in range(len(coin_location)):
        playerrect = pygame.Rect(player_location[0], player_location[1], 128, 128)
        if (coinrect[i]).colliderect(playerrect):
            if coin_style[i] <= 30:
                scored_sound.play()
                score += 1
                textImage = myfont.render("score: " + str(score), True, (0, 0, 255))
                textImageL = myfont.render("level: " + str(level), True, (0, 0, 255))
                #textImageM = myfont.render("life: " + str(live), True, (0, 0, 255))
                coin_location[i][1] = 0
                SCREEN.blit(background, (0, 0))
                SCREEN.blit(textImage, (10, 10))
                SCREEN.blit(textImageL, (520, 10))
                #SCREEN.blit(textImageM, (265, 10))
                for i in range(len(coin_location)):
                    coin_location[i] = [random.randint(0, 750), 0]
                    coin_style[i] = random.randint(0, 50)
                    if coin_style[i] <= 30:
                        SCREEN.blit(coin, coin_location[i])
                    else:
                        SCREEN.blit(decoin, coin_location[i])
                SCREEN.blit(player, player_location)
            else:
                live = False
                pygame.mixer.music.stop()
        if coin_location[i][1] >= 300:
            coin_location[i][1] = 0
            SCREEN.blit(background, (0,0))
            SCREEN.blit(textImage, (10, 10))
            SCREEN.blit(textImageL, (520, 10))
            #SCREEN.blit(textImageM, (265, 10))
            for i in range(len(coin_location)):
                coin_location[i] = [random.randint(0, 750), 0]
                coin_style[i] = random.randint(0, 50)
                if coin_style[i] <= 30:
                    SCREEN.blit(coin, coin_location[i])
                else:
                    SCREEN.blit(decoin, coin_location[i])
            SCREEN.blit(player, player_location)
    pygame.display.update()
    fclock.tick(fps)

while not live:
    for event in pygame.event.get():
        # 处理退出事件
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key_list = pygame.key.get_pressed()
            if(not (key_list[pygame.K_LEFT] or key_list[pygame.K_RIGHT])):
                pygame.quit()
                sys.exit()
    SCREEN.blit(background, (0,0))
    textImage_End = myfont.render("Game Over!", True, (0, 0, 255))
    textImage_Endv = myfont.render("Winner!!!", True, (0, 0, 255))
    textImage_End2 = myfont.render("Press any key to end the game", True, (0, 0, 255))
    if not victory:
        SCREEN.blit(textImage_End, (270, 120))
        if not sounded:
            gameover_sound.play()
            sounded = True
    else:
        pygame.mixer.music.set_volume(0.5)
        pass_sound.play()
        #pygame.mixer.music.play()
        SCREEN.blit(textImage_Endv, (270, 120))
    SCREEN.blit(textImage_End2, (100, 180))
    pygame.display.update()
