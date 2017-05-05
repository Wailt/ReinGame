from pygame import *

from entities.agents.Text import Text


class Stats(sprite.Sprite):
    def __init__(self, sp):
        sprite.Sprite.__init__(self)

        self.skills = dict()
        self.phisics = dict()

        n = -1
        height = 15
        for skill in sp.skills:
            n += 1
            self.skills[skill] = Text(y=n * height)

        for phisic in sp.phisics:
            n += 1
            self.phisics[phisic] = Text(y=n * height)

        self.update(sp)

    def update(self, sp):
        for key in self.phisics:
            self.phisics[key].info = key + ': ' + str(round(sp.phisics[key](), 3))

        for key in self.skills:
            self.skills[key].info = key + ':' + str(round(sp.skills[key], 1))



    def draw(self, screen):
        for key in self.skills:
            self.skills[key].draw(screen)

        for key in self.phisics:
            self.phisics[key].draw(screen)
