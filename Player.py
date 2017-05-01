#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import numpy as np

from Stats import Stats

MOVE_SPEED = 2
WIDTH = 22
HEIGHT = 32
COLOR = Color("#000000")


class Player(sprite.Sprite):
    def __init__(self, x, y, color=COLOR, img=None, stat=False):
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

        self.skills = {'athletics': 2.0, 'fight': 2.0}
        self.skills_stack = {key: 0 for key in self.skills.keys()}

        self.speed = 1
        self.range = 100

        #stat
        if stat:
            self.stat = Stats(self)
        else:
            self.stat = None

        #notes
        self.delete = False

    def update(self, world):
        self.speed = MOVE_SPEED * np.log2(self.skills['athletics']) / 100
        if self.right:
            self.xvel = self.right * self.speed
        else:
            self.xvel = 0
        if self.up:
            self.yvel = self.up * self.speed
        else:
            self.yvel = 0

        self.collide(world)

        self.x += self.xvel
        self.y += self.yvel
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        if self.stat:
            self.stat.update(self)

        self.stack('athletics', (self.xvel ** 2 + self.yvel ** 2) ** 0.5)

    def update_skills(self):
        for key in self.skills_stack:
            self.skills[key] += self.skills_stack[key]
            self.skills_stack[key] = 0

    def stack(self, s, val):
        self.skills_stack[s] += val

    def attack(self, obj):
        self.range = 100 + (self.skills['fight']) ** 0.5
        if ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** (0.5) < self.range:
            self.stack('fight', 1)
            obj.delete = True
            return True
        else:
            return False


    def draw(self, screen):
        if self.stat:
            self.stat.draw(screen)
        screen.blit(self.image, (self.rect.x, self.rect.y))


    def collide(self, platforms):
        max_collide = max([sprite.collide_rect(self, p) for p in platforms])
        if max_collide:
            self.x = self.x_prev_collide
            self.y = self.y_prev_collide
        else:
            self.x_prev_collide = self.x
            self.y_prev_collide = self.y