from pygame import *

from Text import Text


class Stats(sprite.Sprite):
    def __init__(self, sp):
        sprite.Sprite.__init__(self)

        self.skills = dict()

        n = -1
        height = 15
        for skill in sp.skills:
            n += 1
            self.skills[skill] = Text(x=0, y=n * height)

        self.phisics = {'pos': Text(y=(n + 1) * height),
                        'speed': Text(y=(n + 2) * height),
                        'range': Text(y=(n + 3) * height)
                        }

        self.update(sp)

    def update(self, sp):
        self.phisics['pos'].info = 'x:' + str(int(sp.x)) + ', y:' + str(int(sp.y))
        self.phisics['speed'].info = 'speed: ' + str(round(sp.speed, 3))
        self.phisics['range'].info = 'range:' + str(round(sp.range, 2))

        for key in self.skills:
            self.skills[key].info = key + ':' + str(round(sp.skills[key], 1))



    def draw(self, screen):
        for key in self.skills:
            self.skills[key].draw(screen)

        for key in self.phisics:
            self.phisics[key].draw(screen)
