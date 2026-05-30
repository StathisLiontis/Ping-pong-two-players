# create a game
from pygame import *

# class
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (90, 140))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player_Role(GameSprite):
    def update(self):
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= 5
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += 5
    def updates(self):
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= 5
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += 5

class Ball_Role(GameSprite):
    def update(self):
        pass

#create game window
window = display.set_mode((700, 500))
display.set_caption('Ping-Pong_two_players')

#background and items
backgroynd_game = transform.scale(image.load("table_ping_pong_champion_vs_pong_star.png"),(700, 500))
player_1 = Player_Role("racketbulep.png", 600, 250, 5)
player_2 = Player_Role("racketredss.png", 30, 250, 5)
ball = Ball_Role("ball_champions.png", 250, 250, 5)

#ball directions
speed_x = 3
speed_y = 3

#music for background

#mixer.init()
#mixer.music.load("")
#mixer.music.play()

#clock for FPS
clock = time.Clock()
FPS = 60

# game worked but now the name is run
run = True
finish = False
while run:
    window.blit(backgroynd_game,(0,0))
    keys_pressed = key.get_pressed()
    player_1.reset()
    player_2.reset()
    ball.reset()

    for e in event.get():
        if e.type == QUIT:
            run = False
    
    player_1.update()
    player_2.updates()
    #ball.update()
    
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    
    if ball.rect.y < 0:
        speed_y *= -1
    
    if sprite.collide_rect(player_1, ball) or sprite.collide_rect(player_2, ball):
        speed_x *= -1

    clock.tick(FPS)
    display.update() 
