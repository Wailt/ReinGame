from pygame import *

from Text import Text


class Stats(sprite.Sprite):
    def __init__(self, sp):
        sprite.Sprite.__init__(self)

        self.pos = Text(0, 0, '1')
        self.skills = Text(0, 15, '2')
        self.speed = Text(0, 30, '3')
        self.update(sp)

    def update(self, sp):
        self.pos.info = 'x:' + str(int(sp.x)) + ', y:' + str(int(sp.y))
        self.skills.info = 'athletics:' + str(round(sp.skills['athletics'], 1))
        self.speed.info = 'speed: ' + str(round(sp.speed, 3))

    def draw(self, screen):
        self.pos.draw(screen)
        self.skills.draw(screen)
        self.speed.draw(screen)