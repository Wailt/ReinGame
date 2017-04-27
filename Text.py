from pygame import *

class Text(sprite.Sprite):
    def __init__(self, x, y, info):
        self.x = x
        self.y = y
        self.info = info
        sprite.Sprite.__init__(self)

    def draw(self, screen):
        myfont = font.SysFont("monospace", 14)
        self.label = myfont.render(self.info, 1, (0, 0, 0))
        screen.blit(self.label, (self.x, self.y))