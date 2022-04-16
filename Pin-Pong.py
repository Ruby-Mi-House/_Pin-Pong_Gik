from pygame import *
from random import randint
from time import sleep
mixer.init()
font.init()
direction = "left"
direction_1 = "up"
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
    def Update(self):
        global direction
        if self.rect.x <= 150 :
            direction = "right"
        if self.rect.x >= 470:
            direction = "left"
        if direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

        if self.rect.y <= 150 :
            direction_1 = "down"
        if self.rect.y >= 470:
            direction_1 = "up"
        if direction_1 == "up":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
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
