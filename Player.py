#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from numpy import random as npr
from pygame import *

from Brain import Brain
from Stats import Stats

from copy import deepcopy, copy

MOVE_SPEED = 1
WIDTH = 20
HEIGHT = 20
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
        self.rect = Rect(int(self.x) * WIDTH, int(self.y) * WIDTH, WIDTH, HEIGHT)

        self.right = 0
        self.up = 0

        self.skills = {'athletics': 2.0, 'fight': 0.0}
        self.skills_stack = {key: 0 for key in self.skills.keys()}

        self.phisics = {'speed': lambda: MOVE_SPEED * np.log2(self.skills['athletics']) / 100,
                        'range': lambda: (self.skills['fight']) ** 0.5 + 20,
                        'x': lambda: self.x,
                        'y': lambda: self.y,
                        }

        # stat
        if stat:
            self.stat = Stats(self)
        else:
            self.stat = None

        # notes
        self.delete = False

        # brain
        self.brain = Brain(self)

    def update(self, world, mode='player'):
        self.moove(world, mode=mode)
        self.update_skills()
        if self.stat:
            self.stat.update(self)

    def update_skills(self):
        for key in self.skills_stack:
            self.skills[key] += self.skills_stack[key]
            self.skills_stack[key] = 0

    def stack(self, s, val):
        self.skills_stack[s] += val

    def moove(self, world, mode='player'):
        old_world_stat = self.brain.stat(self, world)
        # mooving

        #making decision
        if mode != 'player':
            dicision = self.brain.decide(self, world)
            #TODO: make a dict of actions
            action = dicision['moove'][0]
            self.right = dicision['moove'][1][0]  # npr.randint(0, 3) - 1
            self.up = dicision['moove'][1][1]#npr.randint(0, 3) - 1

        if self.right != 0:
            self.xvel = self.right * self.phisics['speed']()
        else:
            self.xvel = 0
        if self.up != 0:
            self.yvel = self.up * self.phisics['speed']()
        else:
            self.yvel = 0

        self.collide(world)

        if 0 <= self.x + self.xvel < 400 / 20 and 0 <= self.y + self.yvel < 400 / 20:
            self.x += self.xvel
            self.y += self.yvel
            self.rect.x = int(self.x) * WIDTH
            self.rect.y = int(self.y) * HEIGHT

            self.stack('athletics', (self.xvel ** 2 + self.yvel ** 2) ** 0.5)

        #count regret
        if mode != 'player':
            new_world_stat = self.brain.stat(self, world)
            regrets = self.brain.count_regret('here npc', old_world_stat, new_world_stat)
            self.brain.learn(action, regrets)

    def attack(self, obj):
        if ((self.rect.x - obj.rect.x) ** 2 + (self.rect.y - obj.rect.y) ** 2) ** (0.5) <= self.phisics['range']():
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
        if platforms:
            max_collide = max([sprite.collide_rect(self, p) for p in platforms])
        else:
            max_collide = False
        if max_collide:
            self.x = self.x_prev_collide
            self.y = self.y_prev_collide
        else:
            self.x_prev_collide = self.x
            self.y_prev_collide = self.y
