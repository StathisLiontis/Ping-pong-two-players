# create a game
from pygame import *

# class
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_scale_1, player_scale_2):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_scale_1, player_scale_2))
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
speed_of_ball = 5
player_1 = Player_Role("racketbulep.png", 600, 250, 5, 90, 140)
player_2 = Player_Role("racketredss.png", 30, 250, 5, 90, 140)
ball = Ball_Role("ball_champions.png", 250, 250, speed_of_ball, 50, 50)
win_height = 500
# text font 
font.init()
style = font.SysFont("Arial", 40)
#ball directions and perfect score
speed_x = 5
speed_y = 5
global score
score = 0
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
    # reset for items
    player_1.reset()
    player_2.reset()
    ball.reset()
    # guit for game
    for e in event.get():
        if e.type == QUIT:
            run = False
    # score perfect saves of ball
    text_score = style.render("perfect saves of ball:" + str(score), 1, (225, 255, 255))
    window.blit(text_score,(10, 2))
    # lose for player 2
    if ball.rect.x > 650:
        #mixer.music.stop()
        lose = style.render("You lost the ball player 2", True, (0, 230, 255))
        window.blit(lose, (175, 90))
        finish = True
    # lose for player 1
    if ball.rect.x < -4:
        #mixer.music.stop()
        lose = style.render("You lost the ball player 1", True, (255, 0, 0))
        window.blit(lose, (175, 90))
        finish = True

    # finish and rules
    if finish != True:
        player_1.update()
        player_2.updates()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
    
        if sprite.collide_rect(player_1, ball) and speed_x > 0:
            speed_x *= -1
            score = score +1
            speed_of_ball = +100
            speed_x -= 0.2
            if keys_pressed[K_UP]:
                speed_y -= 0.8
            if keys_pressed[K_DOWN]:
                speed_y += 0.8
            ball.rect.x += speed_x * 2

        if sprite.collide_rect(player_2, ball) and speed_x < 0:
            speed_x *= -1
            score = score +1
            speed_of_ball = +100
            speed_x += 0.2
            if keys_pressed[K_w]:
                speed_y -= 0.8
            if keys_pressed[K_s]:
                speed_y += 0.8
            ball.rect.x += speed_x * 2

    clock.tick(FPS)
    display.update() 
