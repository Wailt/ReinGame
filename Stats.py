from pygame import *

from Text import Text


class Stats(sprite.Sprite):
    def __init__(self, sp):
        sprite.Sprite.__init__(self)

        self.phisics = {'pos': Text(),
                        'speed': Text(),
                        'range': Text()
                        }

        self.skills = {'athletics': Text(),
                       'fight': Text()
                       }

        self.update(sp)

    def update(self, sp):
        self.phisics['pos'].info = 'x:' + str(int(sp.x)) + ', y:' + str(int(sp.y))
        self.phisics['speed'].info = 'speed: ' + str(round(sp.speed, 3))
        self.phisics['tange'].info = 'range:' + str(round(sp.range, 2))

        for key in self.skills:
            self.skills['key'].info = key + ':' + str(round(sp.skills[key], 1))

        self.skills['athletics'].info = 'athletics:' + str(round(sp.skills['athletics'], 1))
        self.fight.info = 'fight:' + str(round(sp.skills['fight'], 1))



    def draw(self, screen):
        for key in self.skills:
            self.skills[key].draw(screen)

        for key in self.phisics:
            self.phisics[key].draw(screen)
