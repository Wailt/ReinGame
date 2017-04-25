#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *


MOVE_SPEED = 1
WIDTH = 22
HEIGHT = 32
COLOR = Color("#000000")


class Player(sprite.Sprite):
    def __init__(self, x, y, color=COLOR, img=None):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.startX = x
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        if img:
            self.image = image.load(img)
        else:
            self.image.fill(color)
        self.rect = Rect(x, y, WIDTH, HEIGHT)

        self.right = 0
        self.up = 0

    def update(self):
        if self.right:
            self.xvel = self.right * MOVE_SPEED
        else:
            self.xvel = 0
        if self.up:
            self.yvel = self.up * MOVE_SPEED
        else:
            self.yvel = 0

        self.rect.x += self.xvel
        self.rect.y += self.yvel

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))