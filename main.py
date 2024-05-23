import pygame
import random
import time
pygame.init()
pygame.font.init()
pygame_icon = pygame.image.load('vorobey.png')
pygame.display.set_icon(pygame_icon)
my_font = pygame.font.SysFont('font.ttf', 999)
clock = pygame.time.Clock()
screen_info = pygame.display.Info() 
SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 710
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("VOROBEY")
background_image = pygame.image.load('bg.jpg')
background_image1 = pygame.image.load('bg1.jpg')
playe = pygame.image.load('obj.png')
vetka = pygame.image.load('vetka.png')
vetka1 = pygame.image.load('vetka1.png')
tex=my_font.render('Press space to start ', True, (255, 0, 0))
tex1=my_font.render('Press ESC to leave ', True, (255, 0, 0))
nfi = pygame.image.load('Infiniti.png')
f = pygame.image.load('finityd.png')
bo = pygame.image.load('boo.png')
zern = pygame.image.load('zerno.png')
winn = pygame.image.load('win.png')
winner = pygame.transform.scale(winn, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
bg1 = pygame.transform.scale(background_image1, (SCREEN_WIDTH, SCREEN_HEIGHT))
player_image = pygame.transform.scale(playe, (SCREEN_WIDTH//8, SCREEN_HEIGHT//7))
v = pygame.transform.scale(vetka, (SCREEN_WIDTH//14, SCREEN_HEIGHT//2))
player_width, player_height = player_image.get_size()
v1 = pygame.transform.scale(vetka1, (SCREEN_WIDTH//14, SCREEN_HEIGHT//2))
text = pygame.transform.scale(tex, (SCREEN_WIDTH-100, SCREEN_HEIGHT//4))
text1 = pygame.transform.scale(tex1, (SCREEN_WIDTH-100, SCREEN_HEIGHT//4))
infi = pygame.transform.scale(nfi, (SCREEN_WIDTH//5, SCREEN_HEIGHT//6))
fi = pygame.transform.scale(f, (SCREEN_WIDTH//5, SCREEN_HEIGHT//6))
boo = pygame.transform.scale(bo, (SCREEN_WIDTH, SCREEN_HEIGHT))
zerno = pygame.transform.scale(zern, (SCREEN_WIDTH//10, SCREEN_HEIGHT//5))
player_x = 100
player_y = SCREEN_HEIGHT // 2 - player_height
player_speed = 0
bgx=0
bgs=0 
bgx1=SCREEN_WIDTH
running = True
ticks = 0
vx=SCREEN_WIDTH+50
seconds = random.randint(3, 10)
vet = False
vx0 = True
vxs=0
fly=False
fs = 0
points=0
mode=5.8
FPS = 60
gamestart=False
wing = False
flag = False
modee = 0
ticks1=0
zx = random.randint(int(vx+50), int(SCREEN_WIDTH*1.75-50))
zwi, zhei = zerno.get_size()
zy = random.randint(5, SCREEN_HEIGHT-zhei)
pygame.mixer.init()
pygame.mixer.music.load('forest.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=-1)
sound = pygame.mixer.Sound('wings.mp3')
scream = pygame.mixer.Sound('scream.mp3')
bite = pygame.mixer.Sound('bite.mp3')
YOULOOSE = my_font.render('YOU LOSE! YOUR POINTS: '+str(points), True, (0, 0, 0), (255, 255, 255))
YOUWIN = my_font.render('YOU WIN! YOUR POINTS: '+str(points), True, (0, 0, 0), (255, 255, 255))
tpoi = my_font.render(str(points), True, (255, 0, 0), (255, 255, 255))
loose = False
win = False
zer = False
fas=10
fall=False
poi=points
die = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP:
                sound.play()
                fall=True
                fas=10
                wing = False
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]) and gamestart!=True:
        bgs=5
        fs=5
        vxs=5
        fall=True
        fly=True
        fas=10
        gamestart=True
    if keys[pygame.K_0]:
        die = False
    if keys[pygame.K_1]:
        die = True
    if (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]) and fly:
        player_y -= player_speed
        player_speed = 30
        wing = True
    if keys[pygame.K_ESCAPE]:
        loose = True
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button==1:
                sound.play()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1 and gamestart!=True:
            fly=False
            pos = pygame.mouse.get_pos()  # Получаем координаты места нажатия
            flag = True
    if flag == True: # Начинаем обработку. Проверяем координаты нажатия
        if (150 <= pos[0] <= 150 + SCREEN_WIDTH//5 and SCREEN_HEIGHT//3 <= pos[1] <= SCREEN_HEIGHT//3 + SCREEN_HEIGHT//6):
            modee = 0
            f = pygame.image.load('finityd.png')
            nfi = pygame.image.load('infiniti.png')
    if flag == True:
        if (SCREEN_WIDTH-(SCREEN_WIDTH//5)-150 <= pos[0] <= SCREEN_WIDTH-(SCREEN_WIDTH//5)-150 + SCREEN_WIDTH//5 and SCREEN_HEIGHT//3 <= pos[1] <= SCREEN_HEIGHT//3 + SCREEN_HEIGHT//6):
            modee = 1
            f = pygame.image.load('finity.png')
            nfi = pygame.image.load('infinitid.png')
    if bgx<(-1*SCREEN_WIDTH):
        bgx=SCREEN_WIDTH
    if bgx1<(-1*SCREEN_WIDTH):
        bgx1=SCREEN_WIDTH
    if player_y <-15 and die:
        fly=False
        player_speed=0
        scream.play()
    if player_y > SCREEN_HEIGHT-15 and die:
        fly=False
        player_speed=0
        loose = True
    tpoi = my_font.render(str(points), True, (0, 0, 0), (255, 255, 255))
    if modee == 1:
        if mode<=3:
            fly=False
            player_speed=0
            scream.play()
            win = True
    if wing:
        playe = pygame.image.load('obj1.png')
        player_image = pygame.transform.scale(playe, (SCREEN_WIDTH//8, SCREEN_HEIGHT//7))
    else:
        playe = pygame.image.load('obj.png')
        player_image = pygame.transform.scale(playe, (SCREEN_WIDTH//8, SCREEN_HEIGHT//7))
    bgx-=bgs
    bgx1-=bgs
    player_y += fs
    vwi, vhei = v.get_size()
    ticks+=1
    ticks1+=1
    if ticks==FPS*10 and mode>=1:
        tiscks = 0
        mode -= 0.5
    if ticks1==FPS*10 and gamestart:
        bgs+=1
        vxs+=1
        ticks1=0
    if vx<0-vwi:
        vx = SCREEN_WIDTH+50
        points+=10
    if zx<=0-zwi and points%20==0 and points>0:
        zx = random.randint(int(vx+50), int(SCREEN_WIDTH*1.75-50))
        zy = random.randint(5, SCREEN_HEIGHT-zhei)
        zer = False
    if vx>SCREEN_WIDTH:
            vy = random.randint(100, SCREEN_HEIGHT//4)
            vy1 = SCREEN_HEIGHT - vy - mode*75
            v = pygame.transform.scale(vetka, (SCREEN_WIDTH//14, vy))
            v1 = pygame.transform.scale(vetka1, (SCREEN_WIDTH//14, int(vy1)))
            vet = True
            zer = True
    if vet:
        vx-=vxs
    if zer:
        zx-=vxs
    if ((zx - player_width <= player_x <= zx + zwi) and (zy - player_height <= player_y <= zy + zhei)):
        poi=int(points)
        poi+=5
        points=int(poi)
        zer = False
        zx = random.randint(int(vx+50), int(SCREEN_WIDTH*1.75-50))
        bite.play()
    vwi, vhei = v.get_size()
    zwi, zhei = zerno.get_size()
    vwi1, vhei1 = v1.get_size()
    if ((vx - player_width <= player_x <= vx + vwi) and (0 - player_height <= player_y <= 0 + vhei)) and die:
        fly=False
        player_speed=0
        scream.play()
    if ((vx - player_width <= player_x <= vx + vwi1) and (SCREEN_HEIGHT-vy1 - player_height <= player_y <= SCREEN_HEIGHT-vy1 + vhei1)) and die:
        fly=False
        player_speed=0
        scream.play()
    if fall:
        player_y+=fas
        fas+=0.1
    infi = pygame.transform.scale(nfi, (SCREEN_WIDTH//5, SCREEN_HEIGHT//6))
    fi = pygame.transform.scale(f, (SCREEN_WIDTH//5, SCREEN_HEIGHT//6))
    tpoin = pygame.transform.scale(tpoi, (SCREEN_WIDTH//20, SCREEN_HEIGHT//10))
    screen.blit(bg, (bgx, 0))
    screen.blit(bg1, (bgx1, 0))
    screen.blit(v, (vx, 0))
    vwi, vhei = v.get_size()
    screen.blit(v1, (vx, SCREEN_HEIGHT-vy1))
    screen.blit(zerno, (zx, zy))
    screen.blit(player_image, (player_x, player_y))
    screen.blit(tpoin, (5, 5))
    if gamestart!=True:
        screen.blit(text, (0, 0))
        screen.blit(text1, (0, SCREEN_HEIGHT-(SCREEN_HEIGHT//4)-150))
        screen.blit(infi, (150, SCREEN_HEIGHT//3))
        screen.blit(fi, (SCREEN_WIDTH-(SCREEN_WIDTH//5)-150, SCREEN_HEIGHT//3))
    if (fly!=True and gamestart and points<100) or loose:
        YOULOOS = my_font.render('YOU LOSE! YOUR POINTS: '+str(points), True, (0, 0, 0), (255, 255, 255))
        YOULOOSE = pygame.transform.scale(YOULOOS, (SCREEN_WIDTH-100, SCREEN_HEIGHT//4))
        YOUWIN = my_font.render('YOU WIN! YOUR POINTS: '+str(points), True, (0, 0, 0), (255, 255, 255))
        screen.blit(boo, (0, 0))
        screen.blit(YOULOOSE, (0, 150))
        pygame.display.flip()
        time.sleep(5)
        running = False
    if ((fly!=True and gamestart and points>=100) or win):
        YOULOOSE = my_font.render('YOU LOSE! YOUR POINTS: '+str(points), True, (0, 0, 0), (255, 255, 255))
        YOUWI = my_font.render('YOU WIN! YOUR POINTS: '+str(points), True, (0, 0, 0), (255, 255, 255))
        YOUWIN = pygame.transform.scale(YOUWI, (SCREEN_WIDTH-100, SCREEN_HEIGHT//4))
        screen.blit(winner, (0, 0))
        screen.blit(YOUWIN, (0, 150))
        pygame.display.flip()
        time.sleep(5)
        running = False
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()