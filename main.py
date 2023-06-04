import random

import pygame


def obstacleMove(oList):
    if oList:
        for i in oList:
            i.x -= 5
            if i.bottom == 150:
                root.blit(fly[int(score/15)%2], i)
            else:
                root.blit(snl[int(score/7)%4], i)
        oList = [it for it in oList if it.x > -100]
        return oList
    else:
        return []
def checkCollition(oList, pRect):
    for i in oList:
        if i.colliderect(pRect):
            return True
    else:
        return False

pygame.init()
root = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Perro Escapar')
icon = pygame.image.load("graphics/icon.ico")
pygame.display.set_icon(icon)
clk = pygame.time.Clock()
score = 0

# background
sky = pygame.image.load('graphics/Sky.png').convert()
sky = pygame.transform.scale(sky, (800, 600))
ground = pygame.image.load('graphics/ground.png').convert()
ground = pygame.transform.scale(ground, (850, 200))
ff = pygame.font.Font(None, 24)

# obstacles
obList = []

s1 = pygame.image.load('graphics/s1.png').convert_alpha()
s2 = pygame.image.load('graphics/s2.png').convert_alpha()
s3 = pygame.image.load('graphics/s3.png').convert_alpha()
s4 = pygame.image.load('graphics/s4.png').convert_alpha()
snl = [s1, s2, s3, s4]
for i in range(4): snl[i] = pygame.transform.scale(snl[i], (60, 60))

f1 = pygame.image.load('graphics/fly1.png').convert_alpha()
f2 = pygame.image.load('graphics/fly2.png').convert_alpha()
fly = [f1,f2]
for i in range(2): fly[i] = pygame.transform.scale(fly[i], (100, 60))

# player
p1 = pygame.image.load('graphics/d1.png').convert_alpha()
p2 = pygame.image.load('graphics/d2.png').convert_alpha()
p3 = pygame.image.load('graphics/d3.png').convert_alpha()
p4 = pygame.image.load('graphics/d4.png').convert_alpha()
p5 = pygame.image.load('graphics/d5.png').convert_alpha()
p6 = pygame.image.load('graphics/d6.png').convert_alpha()
p7 = pygame.image.load('graphics/d7.png').convert_alpha()
p8 = pygame.image.load('graphics/d8.png').convert_alpha()
p9 = pygame.image.load('graphics/d9.png').convert_alpha()
p10 = pygame.image.load('graphics/d10.png').convert_alpha()
player = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
for i in range(10): player[i] = pygame.transform.scale(player[i], (100,90))
playerPos = player[9].get_rect(midbottom=(80, 300))
playerGravity = 0

game = False

# timer
gameTimer = pygame.USEREVENT + 1;
pygame.time.set_timer(gameTimer, 1400)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and playerPos.bottom == 300:
                playerGravity = -14
            if event.type == pygame.MOUSEBUTTONDOWN and playerPos.collidepoint(event.pos) and playerPos.bottom == 300:
                playerGravity = -14
            if event.type == gameTimer:
                print('engages')
                print(len(obList))
                if random.randint(0, 2):
                    obList.append(snl[int(score/7)%4].get_rect(midbottom=(random.randint(900, 1200), 300)))
                else:
                    obList.append(fly[int(score/15)%2].get_rect(midbottom=(random.randint(900, 1200), 150)))

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game = True
                score = 0
                obList.clear()

    if game:
        score += 1
        playerGravity += 0.5
        scr = ff.render(str(score), True, 'Black')
        playerPos.y += playerGravity
        if playerPos.bottom >= 300:
            playerPos.bottom = 300

        root.blit(sky, (0, 0))
        root.blit(ground, (0, 280))
        root.blit(scr, (700, 50))
        #pygame.draw.rect(p10, 'BLACK', playerPos, 5)
        #root.blit(p10, playerPos)
        if playerPos.bottom == 300:
            root.blit(player[int(score/4)%10], playerPos)
        else:
            root.blit(player[9], playerPos)
        obList = obstacleMove(obList)

        if checkCollition(obList, playerPos):
            game = False
            print('collition')

    else:
        root.fill('#ffebbb')
        ff = pygame.font.Font(None, 40)
        if score == 0:
            scrTemp = ff.render('Perro Escapar', True, 'black')
        else:
            scrTemp = ff.render('Your total score : ' + str(score), True, 'black')
        scrRect = scrTemp.get_rect(center=(550, 260))

        btm = pygame.font.Font(None, 40)
        btmTemp = btm.render('Press SPACE to play', True, 'black')
        btmrect = btmTemp.get_rect(center=(550, 330))

        pic = pygame.image.load('graphics/player_stand.png').convert_alpha()
        pic = pygame.transform.scale(pic, (480,360))
        picRect = pic.get_rect(topleft=(-60, 0))

        root.blit(scrTemp, scrRect)
        root.blit(btmTemp, btmrect)
        root.blit(pic, picRect)
    pygame.display.update()
    clk.tick(60 + (score / 100))
