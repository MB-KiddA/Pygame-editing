import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nuh Uh, My Game Now")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

BORDER = pygame.Rect(0, HEIGHT // 2, WIDTH, 10)

BULLET_HIT_SOUND = pygame.mixer.Sound('Assets/Bonk_Sound_Effect.mp3')
BULLET_FIRE_SOUND = pygame.mixer.Sound('Assets/Boing.mp3')

HEALTH_FONT = pygame.font.SysFont('arial', 40)
WINNER_FONT = pygame.font.SysFont('arial', 100)

FPS = 60
VEL = 5
BULLET_VEL = 7
SUPER_VEL = 3
MAX_BULLETS = 3
MAX_SUPER = 1
PLAYER_WIDTH, PLAYER_HEIGHT = 64, 64

GREEN_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

GREEN_PLAYER_IMAGE = pygame.image.load(
    os.path.join('Assets', 'player_green.png'))
GREEN_PLAYER = pygame.transform.rotate(pygame.transform.scale(
    GREEN_PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT)), 180)

RED_PLAYER_IMAGE = pygame.image.load(
    os.path.join('Assets', 'player_red.png'))
RED_PLAYER = pygame.transform.rotate(pygame.transform.scale(
    RED_PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT)), 0)

BG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Background.png')), (WIDTH, HEIGHT))


def draw_window(red, green, red_bullets, green_bullets, red_health, green_health):
    WIN.blit(BG, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render(
        "Dabloons: " + str(red_health), 1, WHITE)
    green_health_text = HEALTH_FONT.render(
        "Dabloons: " + str(green_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(green_health_text, (10, 10))

    WIN.blit(GREEN_PLAYER, (green.x, green.y))
    WIN.blit(RED_PLAYER, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in green_bullets:
        pygame.draw.rect(WIN, GREEN, bullet)

    pygame.display.update()


def green_handle_movement(keys_pressed, green):
    if keys_pressed[pygame.K_f] and green.x - VEL > 0:  # LEFT
        green.x -= VEL
    if keys_pressed[pygame.K_h] and green.x + VEL < 740:  # RIGHT
        green.x += VEL
    if keys_pressed[pygame.K_t] and green.y - VEL > BORDER.y:  # UP
        green.y -= VEL
    if keys_pressed[pygame.K_g] and green.y + VEL + green.height < HEIGHT - 20:  # DOWN
        green.y += VEL


def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_KP4] and red.x - VEL > 0:  # LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_KP6] and red.x + VEL < HEIGHT - 60:  # RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_KP8] and red.y - VEL > 0:  # UP
        red.y -= VEL
    if keys_pressed[pygame.K_KP5] and red.y + VEL < BORDER.y - 30:  # DOWN
        red.y += VEL


def handle_bullets(green_bullets, red_bullets, green, red):
    for bullet in green_bullets:
        bullet.y -= BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            green_bullets.remove(bullet)
        elif bullet.y < 0:
            green_bullets.remove(bullet)

    for super in green_bullets:
        super.y += SUPER_VEL - 1
        if red.colliderect(super):
            pygame.event.post(pygame.event.Event(RED_HIT))
            green_bullets.remove(super)
        elif super.y < 0:
            green_bullets.remove(super)

    for bullet in red_bullets:
        bullet.y += BULLET_VEL
        if green.colliderect(bullet):
            pygame.event.post(pygame.event.Event(GREEN_HIT))
            red_bullets.remove(bullet)
        elif bullet.y > 800:
            red_bullets.remove(bullet)

    for super in red_bullets:
        super.y += SUPER_VEL - 1
        if green.colliderect(super):
            pygame.event.post(pygame.event.Event(GREEN_HIT))
            red_bullets.remove(super)
        elif super.y > 800:
            red_bullets.remove(super)
        


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))
    
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    red = pygame.Rect(400, 100, PLAYER_WIDTH, PLAYER_HEIGHT)
    green = pygame.Rect(400, 500, PLAYER_WIDTH, PLAYER_HEIGHT)

    red_bullets = []
    green_bullets = []

    red_health = 10
    green_health = 10

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
                if event.key == pygame.K_i and len(green_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        green.x , green.y, 10, 5)
                    green_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_o and len(green_bullets) < MAX_SUPER:
                    super = pygame.Rect(
                        green.x, green.y, 70, 10)
                    green_bullets.append(super)
                
                if event.key == pygame.K_p and len(green_bullets) < MAX_SUPER:
                    super = pygame.Rect(
                        green.x, green.y, 10, 70)
                    green_bullets.append(super)

                if event.key == pygame.K_UP and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RIGHT and len(red_bullets) < MAX_SUPER:
                    super = pygame.Rect(
                        red.x, red.y + red.height//2 - 2, 70, 10)
                    red_bullets.append(super)

                if event.key == pygame.K_DOWN and len(red_bullets) < MAX_SUPER:
                    super = pygame.Rect(
                        red.x, red.y + red.height//2 - 2, 10, 70)
                    red_bullets.append(super)
                    
                    

            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == GREEN_HIT:
                green_health -= 1
                BULLET_HIT_SOUND.play()

        winner_text = ""
        if red_health <= 0:
            winner_text = "Green tha Winner!"

        if green_health <= 0:
            winner_text = " Red Tha Winner!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        
        green_handle_movement(keys_pressed, green)
        red_handle_movement(keys_pressed, red)

        handle_bullets(green_bullets, red_bullets, green, red)

        draw_window(red, green, red_bullets, green_bullets,
                    red_health, green_health)

    main()


if __name__ == "__main__":
    main()
