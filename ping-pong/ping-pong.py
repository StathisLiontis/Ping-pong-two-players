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
style = font.SysFont("Arial", 34)
styles = font.SysFont("Arial", 25)
#ball directions and perfect score
speed_x = 5
speed_y = 5
global score
score = 0
score_player_1 = 0
score_player_2 = 0
#music for background
mixer.init()
mixer.music.load("alisiabeats-titanium-170190.mp3")
mixer.music.set_volume(0.5)
mixer.music.play()
sound_of_winner = mixer.Sound('kevincsupo-marble-it-up-ultra-soccer-win-sound.mp3')
restart_sound = mixer.Sound('restart_button.mp3')
pause_sound = mixer.Sound('pause_sound_effect.mp3')
#clock for FPS
clock = time.Clock()
FPS = 60 
# game worked but now the name is run
run = True
finish = False
sound_played = False
sound_played_restart = False
sound_pause = False
pause = False
How_play = False
music_muted = False
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
        # restart the game
        if finish == True and e.type == KEYDOWN:
            if e.key == K_r:
                if not sound_played_restart:
                    restart_sound.play()
                    sound_played_restart = True
                # επαναφορα μεταβλητων
                finish = False
                sound_played = False
                sound_played_restart = False
                score = 0 
                score_player_1 = 0
                score_player_2 = 0
                speed_x = 5
                speed_y = 5
                #επαναφορα θεσεων
                ball.rect.x = 325
                ball.rect.y = 225
                player_1.rect.y = 250
                player_2.rect.y = 250
                #επαναφορα τις μουσικης
                mixer.music.play(-1)
        #mute the music
        if e.type == KEYDOWN:
            if e.key == K_m:
                if music_muted:
                    mixer.music.unpause()
                    music_muted = False
                else:
                    mixer_music.pause()
                    music_muted = True
        # h for learn how to play the game.
        if e.type == KEYDOWN:
            if e.key == K_h:
                How_play = not How_play
                sound_pause = False
        # space for use pause
        if e.type == KEYDOWN:
            if e.key == K_SPACE and not finish:
                pause = not pause
                sound_pause = False
    # how the players play the game.
    if How_play:
        How_play_text_1 = style.render('Player1 (red racket) use W and S', True, (225, 219, 61))
        window.blit(How_play_text_1, (35, 100))
        How_play_text_1_1 = style.render('in the keyboard to move', True, (225, 219, 61))
        window.blit(How_play_text_1_1, (35, 140))
        How_play_text_2 = style.render('Player2 (blue racket) use UP and DOWN Arrows', True, (225, 219, 61))
        window.blit(How_play_text_2, (35, 170))
        How_play_text_2_2 = style.render('in the keyboard to move', True, (225, 219, 61))
        window.blit(How_play_text_2_2, (35, 200))
        How_play_text_2_3 = style.render("Press 'H' to play", True, (225, 219, 61))
        window.blit(How_play_text_2_3, (50, 250))
        if not sound_pause:
            pause_sound.play()
            sound_pause = True
        display.update()
        clock.tick(FPS)
        continue
    # pause and unpause
    if pause:
        pause_text = style.render("Press 'SPACE' to UNpause the game", True,(255, 219, 61))
        window.blit(pause_text,(125, 100))
        if not sound_pause:
            pause_sound.play()
            sound_pause = True
        display.update()
        clock.tick(FPS)
        continue
    #text for match
    text_match_score = style.render(f'P1: {score_player_1} | P2: {score_player_2}', 1, (255,255,255))
    window.blit(text_match_score,(3, 455))
    # score perfect saves of ball
    text_score = style.render("Perfect saves of Ball:" + str(score), 1, (225, 255, 255))
    window.blit(text_score,(10, 2))
    # informaition for space
    informaition_text = style.render("Press 'SPACE' to pause", True,(255, 219, 61))
    window.blit(informaition_text,(360, 2))
    # information for mute the music
    mute_music_text = styles.render("Press 'M' mute/unmute music", True,(255, 219, 61))
    window.blit(mute_music_text, (410, 460))
    #information for how to play by button edition
    informaition_play_text = styles.render("Press 'H' how to play", True, (255, 219, 61))
    window.blit(informaition_play_text, (160, 470))
    # lose for player 2 and winner player 1 
    if ball.rect.x > 650:
        if score_player_1 <= 2:
            score_player_1 += 1 # take poit player 1
        else:
            score_player_1 += 0
        if score_player_1 < 3:
            score = 0
            ball.rect.x = 250
            ball.rect.y = 250
            speed_x = -3
        else:
            # stop the background music
            mixer.music.stop()
            # winner sound
            if not sound_played:
                sound_of_winner.play()
                sound_played = True
            # lose text
            lose = style.render("You lost the ball player 2", True, (0, 230, 255))
            window.blit(lose, (200, 90))
            # winner text
            winner = style.render("The player 1 is the winner", True, (255, 0, 0))
            window.blit(winner, (190, 130))
            # restart text
            restart_text = style.render("Press 'R' to Restart the game", True,(255, 219, 61))
            window.blit(restart_text,(205, 200))
            finish = True
    
    # lose for player 1 and winner player 2
    if ball.rect.x < -4:
        if score_player_2 <= 2:
            score_player_2 += 1 # take poit player 2
        else:
            score_player_2 += 0
        if score_player_2 < 3:
            score = 0
            ball.rect.x = 250
            ball.rect.y = 250
            speed_x = -3
        else:
            # stop the background music
            mixer.music.stop()
            # winner sound
            if not sound_played:
                sound_of_winner.play()
                sound_played = True
            # lose text
            lose = style.render("You lost the ball player 1", True, (255, 0, 0))
            window.blit(lose, (200, 90))
            # winner text
            winners = style.render("The player 2 is the winner", True, (0, 230, 255))
            window.blit(winners, (190, 130))
            # restart text
            restart_text = style.render("Press 'R' to Restart the game", True,(255, 219, 61))
            window.blit(restart_text,(205, 200))
            finish = True
    
    # finish and rules
    if finish != True:
        player_1.update()
        player_2.updates()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        # ball bouns
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        # collide player_1 ball
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
        # collide player_2 ball
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
