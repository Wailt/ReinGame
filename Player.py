#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *

MOVE_SPEED = 1
WIDTH = 22
HEIGHT = 32
COLOR = "#000000"


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.startX = x
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)

    def update(self, right, up):
        if right:
            self.xvel = right * MOVE_SPEED
        else:
            self.xvel = 0
        if up:
            self.yvel = up * MOVE_SPEED
        else:
            self.yvel = 0

        self.rect.x += self.xvel
        self.rect.y += self.yvel

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))