import pygame, os

PH, PW = 64, 64

IH, IW = 112, 98

druid_sprite = pygame.image.load(
    os.path.join('Assets','Druid.png'))

Druid = pygame.transform.scale(
    druid_sprite, (PH, PW))

Druid_Icon_Sprite = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Druid_Icon.png')), (IH, IW))

rouge_sprite = pygame.image.load(
    os.path.join('Assets', 'Rouge.png'))

Rouge = pygame.transform.scale(
    rouge_sprite, (PH, PW))

Rouge_Icon_sprite = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets','Rouge_Icon.png')), (IH, IW))

warrior_sprite = pygame.image.load(
    os.path.join('Assets', 'Warrior.png'))

Warrior = pygame.transform.scale(
    warrior_sprite, (PH, PW))

Warrior_Icon_Sprite = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets','Warrior_Icon.png')), (IH, IW))

frog_sprite = pygame.image.load(
    os.path.join('Assets', 'Frog.png'))

Frog = pygame.transform.scale(
    frog_sprite, (PH, PW))

Frog_Icon_Sprite = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets','Frog_Icon.png')), (IW, IH))

BG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Background.png')), (800, 600))

BGG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Background_Game.png')), (800, 600))

Druid_Icon_Select = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Druid_Icon_Select.png')), (IW, IH))

Rouge_Icon_Select = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Rouge_Icon_Select.png')), (IW, IH))

Warrior_Icon_Select = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Warrior_Icon_Select.png')), (IW, IH))

Frog_Icon_Select = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Frog_Icon_Select.png')), (IW, IH))