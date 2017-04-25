#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import numpy as np

MOVE_SPEED = 1
WIDTH = 22
HEIGHT = 32
COLOR = Color("#000000")


class Player(sprite.Sprite):
    def __init__(self, x, y, color=COLOR, img=None):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.x = x
        self.y = y

        self.x_prev_collide = self.x
        self.y_prev_collide = self.y

        self.image = Surface((WIDTH, HEIGHT))

        if img:
            self.image = image.load(img)
        else:
            self.image.fill(color)
        self.rect = Rect(x, y, WIDTH, HEIGHT)

        self.right = 0
        self.up = 0

        self.skills = {'athletics': 2.0}

    def update(self, world):
        if self.right:
            self.xvel = self.right * MOVE_SPEED * np.log2(1 + (np.log2(self.skills['athletics']))) / 8
        else:
            self.xvel = 0
        if self.up:
            self.yvel = self.up * MOVE_SPEED * np.log2(1 + (np.log2(self.skills['athletics'])))/ 8
        else:
            self.yvel = 0

        self.collide(world)

        self.x += self.xvel
        self.y += self.yvel
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        self.skills['athletics'] += (self.xvel ** 2 + self.yvel ** 2) ** 0.5

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def collide(self, platforms):
        max_collide = max([sprite.collide_rect(self, p) for p in platforms])
        if max_collide:  # если есть пересечение платформы с игроком\
            print('block_collide')
            print('real', self.x, self.y)
            self.x = self.x_prev_collide
            self.y = self.y_prev_collide
        else:
            print('not_collide')
            print('real', self.x, self.y)
            self.x_prev_collide = self.x
            self.y_prev_collide = self.y
        print('image', self.rect.x, self.rect.y)
        print('prev', self.x_prev_collide, self.y_prev_collide)
        print()