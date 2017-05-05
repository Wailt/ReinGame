from pygame import *


decore_width = 20
decore_height = 20

class Decore(sprite.Sprite):
    def __init__(self, x, y, img):
        sprite.Sprite.__init__(self)

        self.x = x
        self.y = y

        self.image = Surface((decore_width, decore_height))

        if img:
            self.image = image.load(img)
        else:
            self.image.fill(color)
        self.rect = Rect(x, y, decore_width, decore_height)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))