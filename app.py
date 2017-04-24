# Импортируем библиотеку pygame
import pygame
from pygame import *

from Player import Player

WIN_WIDTH = 400  # Ширина создаваемого окна
WIN_HEIGHT = 400  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#FFFFFF"


def main():
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Rein Game")  # Пишем в шапку
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон
    bg.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом
    up = right = 0
    pf = Player(50, 50)
    timer = pygame.time.Clock()

    while 1:
        timer.tick(200)
        for e in pygame.event.get():
            if e.type == QUIT:
                raise (SystemExit, "QUIT")
            if e.type == KEYDOWN:
                if e.key == K_RIGHT:
                    right = 1
                elif e.key == K_LEFT:
                    right = -1
                elif e.key == K_UP:
                    up = -1
                elif e.key == K_DOWN:
                    up = 1
            if e.type == KEYUP:
                if e.key == K_RIGHT:
                    right = 0
                elif e.key == K_LEFT:
                    right = 0
                elif e.key == K_UP:
                    up = 0
                elif e.key == K_DOWN:
                    up = 0


            if e.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pf.rect.collidepoint(pos):
                    pf.image.fill(Color(0, 100, 0))

        pf.update(right, up)

        screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать
        pf.draw(screen)
        pygame.display.update()  # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    main()
