from pygame import *

from Text import Text


class Stats(sprite.Sprite):
    def __init__(self, sp):
        sprite.Sprite.__init__(self)

        self.pos = Text(0, 0, '1')
        self.athletics = Text(0, 15, '2')
        self.fight = Text(0, 30, '3')
        self.speed = Text(0, 45, '4')
        self.range = Text(0, 60, '5')
        self.update(sp)

    def update(self, sp):
        self.pos.info = 'x:' + str(int(sp.x)) + ', y:' + str(int(sp.y))
        self.athletics.info = 'athletics:' + str(round(sp.skills['athletics'], 1))
        self.fight.info = 'fight:' + str(round(sp.skills['fight'], 1))
        self.speed.info = 'speed: ' + str(round(sp.speed, 3))
        self.range.info = 'range:' + str(round(sp.range, 2))


    def draw(self, screen):
        self.pos.draw(screen)
        self.athletics.draw(screen)
        self.fight.draw(screen)
        self.speed.draw(screen)
        self.range.draw(screen)