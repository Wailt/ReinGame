import numpy.random as npr
import pygame
from pygame import *


def process_player(e, player):
    if e.type == QUIT:
        raise (SystemExit, "QUIT")
    if e.type == KEYDOWN:
        if e.key == K_RIGHT:
            player.right = 1
        elif e.key == K_LEFT:
            player.right = -1
        elif e.key == K_UP:
            player.up = -1
        elif e.key == K_DOWN:
            player.up = 1

    if e.type == KEYUP:
        if e.key == K_RIGHT:
            player.right = 0
        elif e.key == K_LEFT:
            player.right = 0
        elif e.key == K_UP:
            player.up = 0
        elif e.key == K_DOWN:
            player.up = 0

    if e.type == pygame.MOUSEBUTTONDOWN:
        if player.rect.collidepoint(pygame.mouse.get_pos()):
            r, g, b = tuple(map(lambda x: int(x), npr.randint(0, 100, 3)))
            player.image.fill(Color(r, g, b))

def process_player_object(e, player, obj_list):
    if e.type == KEYDOWN:
        if e.key == K_e:
            for obj in obj_list:
                if ((player.x - obj.x) ** 2 + (player.y - obj.y) ** 2) ** (0.5) < 100:
                    obj.delete = True
                    break
