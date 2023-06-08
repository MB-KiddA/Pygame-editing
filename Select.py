import pygame, os
from Sprites import *
from main import WIN, FPS, main, P1, P2


def draw_win(WIN):
    WIN.blit(Rouge_Icon_sprite, (100, 600))
    WIN.blit(BG, (0,0))


    pygame.display.update()

def player_sel(control, s1, pick):
    if pick == 0:
        p1_controls(control, s1)
    elif pick == 1:
        p2_controls(control, s1)
    elif pick == 2:
        main()


def p1_controls(control, s1):
    if control[pygame.K_a]:
        s1.remove("car")
        print(len(s1))
    if control[pygame.K_d]:
        s1.append("car")
        print(len(s1))

def p2_controls(control, s1):
    if control[pygame.K_KP4]:
        s1.remove(1)
    if control[pygame.K_KP6]:
        s1.append(1)

def char_sel(s1, s2, pick):
    while pick == 0:
        if s2 == 1:
            P1 = Druid
        elif s2 == 2:
            P1 = Frog
        elif s2 == 3:
            P1 = Rouge
        elif s2 == 4:
            P1 = Frog
    while pick == 1:
        if s2 == 1:
            P2 = Druid
        elif s2 == 2:
            P2 = Frog
        elif s2 == 3:
            P2 = Rouge
        elif s2 == 4:
            P2 = Frog   


def menu():
    s1 = ["car", "car"]
    s2 = 0
    pick = 0
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            control = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit
                
    
            if len(s1) > 3:
                s1.clear()
            if len(s1) < 0:
                s1.append("car") and s1.append("car") and s1.append("car") and s1.append("car")

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_t or pygame.K_y or pygame.K_u:
                    s2 = len(s1)
                    pick += 1

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_UP or pygame.K_RIGHT or pygame.K_DOWN:
                    s2 = len(s1)
                    pick += 1
                
    player_sel(s1, pick, control)
    draw_win(WIN)


    menu()

menu()