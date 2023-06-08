import pygame, os
from Sprites import *
from main import WIN, FPS, main, P1


def draw_win(WIN):
    WIN.blit(BG, (0,0))

    pygame.display.update()

def player_sel(s1, pick):
    if pick == 0:
        p1_controls(s1, pick)
    elif pick == 1:
        p2_controls(s1, pick)
    elif pick == 2:
        main()


def p1_controls(control, s1):
    if control[pygame.K_a]:
        s1.remove(1)
    if control[pygame.K_d]:
        s1.append(1)

def p2_controls(control, s1):
    if control[pygame.K_KP4]:
        s1.remove(1)
    if control[pygame.K_KP6]:
        s1.append(1)

def char_sel(s2, pick):
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
    s1 = []
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
    
            if s1.index() > 3:
                s1.clear()
            if s1.index() < 0:
                s1.append(1) and s1.append(1) and s1.append(1) and s1.append(1)

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_t or pygame.K_y or pygame.K_u:
                    s2 = len(s1)
                    pick += 1

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_UP or pygame.K_RIGHT or pygame.K_DOWN:
                    s2 = len(s2)
                    pick += 1
                
    player_sel(s1, pick)
    draw_win()


    menu()

menu()