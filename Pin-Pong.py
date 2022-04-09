from pygame import *
from random import randint
from time import sleep
mixer.init()
font.init()
window = display.set_mode ((700, 500))
display.set_caption ("_Pin-Pong_")
background = transform.scale(image.load("Fon.jpg"), (700,500))
game = True
clock = time.Clock()
FPS = 100
clock.tick(FPS)
speed = 2
mixer.music.load("Fonam (1).mp3")
mixer.music.play()
#kick = mixer.Sound("Stolknovenie.mp3")
font.init()
#font = font.SysFont("Times New Roman",70)
finish = False
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player_2(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def Update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and a.rect.y>5:
            a.rect.y -= speed
        if keys_pressed[K_DOWN] and a.rect.y<625:
            a.rect.y += speed
class Player_1(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def Update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y>5:
            self.rect.y -= speed
        if keys_pressed[K_s] and self.rect.y<625:
            self.rect.y += speed
class Boll(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed,):
        super().__init__(player_image, player_x, player_y, player_speed)
    def update(self):
        if self.rect.y < 400:
            self.rect.y += self.speed
        if self.rect.x < 400:
            self.rect.x += self.speed
        if self.rect.y > 600:
            self.rect.y -= self.speed
        if self.rect.x > 600:
            self.rect.x -= self.speed
a_1 = Player_1('P_1.png', 30, 430, speed)
a_2 = Player_2('P_1.png', 600, 430, speed)
boll = Boll("Boll.png", randint(35,620), randint(35,620),1)
while game:
    #sprites_list = sprite.spritecollide(a_1, boll, True)
    #sprites_list = sprite.spritecollide(a_2, boll, True)
    window.blit(background, (0,0))
    window.blit(a_1.image,(a_1.rect.x,a_1.rect.y))
    window.blit(a_2.image,(a_2.rect.x,a_2.rect.y))
    window.blit(boll.image,(boll.rect.x,boll.rect.y))
    a_1.Update()
    a_2.update()
    boll.update()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()









'''class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed,x,y):
        super().__init__(player_image, player_x, player_y, player_speed,x,y)
    def update(self):
        global propusk
        if self.rect.y < 500:
            self.rect.y += self.speed
        else:
            self.rect.x = randint(25,650)
            self.speed = randint(1,2)
            self.rect.y = 10
            propusk += 1
            self.rect.y += self.speed
class bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed,x,y):
        super().__init__(player_image, player_x, player_y, player_speed,x,y)
        self.x = x
        self.y = y
    def update(self):
        if self.rect.y > 0:
            self.rect.y -= self.speed
        else:
            self.kill()
a = Player('rocket.png', 10, 430, speed,70,80)
b_1 = Enemy("ufo.png", randint(35,620), 10, randint(1,2),70,50)
b_2 = Enemy("ufo.png", randint(35,620), 10, randint(1,2),70,50)
b_3 = Enemy("ufo.png", randint(35,620), 10, randint(1,2),70,50)
b_4 = Enemy("ufo.png", randint(35,620), 10, randint(1,2),70,50)
b_5 = Enemy("ufo.png", randint(35,620), 10, randint(1,2),70,50)
monsters = sprite.Group()
monsters.add(b_1,b_2,b_3,b_4,b_5)
b_1_1 = Ast("asteroid.png", randint(35,620), 10, randint(1,2),70,50)
b_2_1= Ast("asteroid.png", randint(35,620), 10, randint(1,2),70,50)
b_3_1 = Ast("asteroid.png", randint(35,620), 10, randint(1,2),70,50)
asteroids = sprite.Group()
asteroids.add(b_1_1,b_2_1,b_3_1)
while game:
    text_win_ = font_1.render("You win",1,(255,255,255))
    text_lose_ = font_1.render("You lose",1,(255,255,255))  
    if balli >= 30:
        window.blit(text_win_,(100,100))
        sleep(5)
        game = False
    if propusk >= 20:
        window.blit(text_lose_,(100,100)) 
        sleep(5) 
        game = False
    sprites_list_1 = sprite.spritecollide(a, monsters, False)
    sprites_list_2 = sprite.groupcollide(Bullet, monsters, True, True)
    sprites_list_3 = sprite.spritecollide(a, asteroids, True)
    for i in sprites_list_3:
        soul-=1
    if soul <=0:
        window.blit(text_lose_,(50,50)) 
        sleep(5) 
        finish = True   
        game = False
    for i in sprites_list_2:
        balli += 1
        monsters_ =  Enemy("ufo.png", randint(35,620), 10, randint(1,2),70,50)
        monsters.add(monsters_)
    text_soul = font_1.render("Жизни: "+ str(soul),1,(255,255,255))
    text_lose = font_1.render("Пропущено: "+ str(propusk),1,(255,255,255))
    text_win = font_1.render("Подбито: "+ str(balli),1,(255,255,255))'''