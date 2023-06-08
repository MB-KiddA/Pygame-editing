import pygame
import os
from Sprites import *

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Medieval Mayham")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

BORDER = pygame.Rect(WIDTH // 2 - 5, 264, 10, WIDTH)

ATTACK_HIT_SOUND = pygame.mixer.Sound('Assets/Bonk_Sound_Effect.mp3')
BULLET_FIRE_SOUND = pygame.mixer.Sound('Assets/Laser.mp3')
ATTACK_FIRE_SOUND = pygame.mixer.Sound('Assets/Woosh.mp3')
HEALTH_FONT = pygame.font.SysFont('arial', 40)
WINNER_FONT = pygame.font.SysFont('arial', 100)

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_ATTACKS = 1
MAX_SUPER = 3
PLAYER_WIDTH, PLAYER_HEIGHT = 64, 64

#P1 = RED P2 = GREEN
P2_HIT = pygame.USEREVENT + 1
P1_HIT = pygame.USEREVENT + 2


P1_IMAGE = pygame.image.load(
    os.path.join('Assets', 'player_green.png'))
P1 = pygame.transform.rotate(pygame.transform.scale(
    P1_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT)), 90)

P2_IMAGE = pygame.image.load(
    os.path.join('Assets', 'player_red.png'))
P2 = pygame.transform.rotate(pygame.transform.scale(
    P2_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT)), 270)


def draw_window(p2, p1, p2_attacks, p1_attacks, p2_health, p1_health):
    WIN.blit(BGG, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    p2_health_text = HEALTH_FONT.render(
        "Dabloons: " + str(p2_health), 1, WHITE)
    p1_health_text = HEALTH_FONT.render(
        "Dabloons: " + str(p1_health), 1, WHITE)
    WIN.blit(p2_health_text, (WIDTH - p2_health_text.get_width() - 10, 10))
    WIN.blit(p1_health_text, (10, 10))

    WIN.blit(P1, (p1.x, p1.y))
    WIN.blit(P2, (p2.x, p2.y))

    for attack in p2_attacks:
        pygame.draw.rect(WIN, RED, attack)

    for attack in p1_attacks:
        pygame.draw.rect(WIN, GREEN, attack)

    pygame.display.update()


def p1_handle_movement(keys_pressed, p1):
    if keys_pressed[pygame.K_a] and p1.x - VEL > 0 - 5:  # LEFT
        p1.x -= VEL
    if keys_pressed[pygame.K_d] and p1.x + VEL < BORDER.x - 60:  # RIGHT
        p1.x += VEL
    if keys_pressed[pygame.K_w] and p1.y - VEL > 259:  # UP
        p1.y -= VEL
    if keys_pressed[pygame.K_s] and p1.y + VEL < 600 - 60:  # DOWN
        p1.y += VEL

def p2_handle_movement(keys_pressed, p2):
    if keys_pressed[pygame.K_KP4] and p2.x - VEL > BORDER.x + 5:  # LEFT
        p2.x -= VEL
    if keys_pressed[pygame.K_KP6] and p2.x + VEL < 800 - 60:  # RIGHT
        p2.x += VEL
    if keys_pressed[pygame.K_KP8] and p2.y - VEL > 259:  # UP
        p2.y -= VEL
    if keys_pressed[pygame.K_KP5] and p2.y + VEL < 600 - 60:  # DOWN
        p2.y += VEL



def handle_attacks(p1_attacks, p2_attacks, p1, p2):
    for swing in p1_attacks:

        swing.x = p1.x + 64
        swing.y = p1.y
        if p2.colliderect(swing):
            pygame.event.post(pygame.event.Event(P1_HIT))
            p1_attacks.remove(swing)
            

    for super in p1_attacks:
        super.x += BULLET_VEL
        if p2.colliderect(super):
            pygame.event.post(pygame.event.Event(P1_HIT))
            p1_attacks.remove(super)
        elif super.x < 0:
            p1_attacks.remove(super)

    for swing in p2_attacks:
 
        swing.x = p2.x - 60
        if p1.colliderect(swing):
            pygame.event.post(pygame.event.Event(P2_HIT))
            p2_attacks.remove(swing)


    for super in p2_attacks:
        super.x -= BULLET_VEL
        if p1.colliderect(super):
            pygame.event.post(pygame.event.Event(P2_HIT))
            p2_attacks.remove(super)
        elif super.x > 800:
            p2_attacks.remove(super)
        


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))
    
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    p1 = pygame.Rect(200, 300, PLAYER_WIDTH, PLAYER_HEIGHT)
    p2 = pygame.Rect(600, 300, PLAYER_WIDTH, PLAYER_HEIGHT)
    gone = 0
    here = 0
    p2_attacks = []
    p1_attacks = []

    p2_health = 2
    p1_health = 2
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            keys_pressed = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    gone += 1
                    print(gone)
                    if gone == 1:
                        swing = pygame.Rect(
                            p1.x , p1.y, 70, 70)
                        
                        p1_attacks.append(swing)

                        ATTACK_FIRE_SOUND.play()
                    if gone == 2: 
                        p1_attacks.remove(swing)
                        gone = 0



                if event.key == pygame.K_y and len(p1_attacks) < MAX_SUPER:
                    super = pygame.Rect(
                        p1.x, p1.y + 30, 70, 10)
                    p1_attacks.append(super)
                
                if event.key == pygame.K_u and len(p1_attacks) < MAX_SUPER:
                    super = pygame.Rect(
                        p1.x, p1.y + 30, 10, 70)
                    p1_attacks.append(super)

                if event.key == pygame.K_UP:
                    here += 1
                    if here == 1:
                        attack = pygame.Rect(
                            p2.x, p2.y, 70, 70)
                        p2_attacks.append(swing)
                        ATTACK_FIRE_SOUND.play()
                    if here == 2:
                        p2_attacks.remove(swing)
                        here = 0

                if event.key == pygame.K_RIGHT and len(p2_attacks) < MAX_SUPER:
                    super = pygame.Rect(
                        p2.x, p2.y + p2.height//2 - 2, 70, 10)
                    p2_attacks.append(super)

                if event.key == pygame.K_DOWN and len(p2_attacks) < MAX_SUPER:
                    super = pygame.Rect(
                        p2.x, p2.y + p2.height//2 - 2, 10, 70)
                    p2_attacks.append(super)
                    
                    

            if event.type == P1_HIT:
                p2_health -= 1
                p1_health += 1
                ATTACK_HIT_SOUND.play()

            if event.type == P2_HIT:
                p1_health -= 1
                p2_health += 1
                ATTACK_HIT_SOUND.play()

        winner_text = ""
        if p2_health <= 0:
            winner_text = "Green tha Winner!"

        if p1_health <= 0:
            winner_text = " Red Tha Winner!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        
        p1_handle_movement(keys_pressed, p1)
        p2_handle_movement(keys_pressed, p2)

        handle_attacks(p1_attacks, p2_attacks, p1, p2)

        draw_window(p2, p1, p2_attacks, p1_attacks,
                    p2_health, p1_health)

    main()

main()
