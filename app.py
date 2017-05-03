# Импортируем библиотеку pygame
import pygame
from pygame import *

from Decore import *
from Player import Player
from Stats import Stats
from Text import Text
from event_processing import *

from time import time

import numpy.random as npr

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

    pf = Player(0, 0, img="img/main_player.png", stat=True)
    blocks = [Player(npr.randint(WIN_WIDTH / decore_width),
                     npr.randint(WIN_HEIGHT / decore_height),
                     color=Color(100, 0, 0), stat=False, img='img/enemy.png') for i in range(10)]

    cells = [Decore(i, j, "img/cell.png") for i in range(0, WIN_WIDTH, decore_width)
             for j in range(0, WIN_HEIGHT, decore_height)]

    timer = pygame.time.Clock()

    step = 0
    begin_time = time()
    try:
        while 1:
            step += 1
            timer.tick(100)
            for e in pygame.event.get():
                process_player(e, pf)
                process_player_object(e, pf, blocks)

            pf.update(blocks)

            for i in range(len(blocks)):
                #TODO: hard place how to do the same without creation new list?
                blocks[i].update(blocks[:i] + blocks[i + 1:], 'npc')

            screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать
            [i.draw(screen) for i in cells]
            [i.draw(screen) for i in blocks]
            blocks = [i for i in blocks if not i.delete]

            pf.draw(screen)
            pygame.display.update()  # обновление и вывод всех изменений на экран
    except Exception as e:
        print('step:', step)
        print('time:', time() - begin_time)
        raise e


if __name__ == "__main__":
    main()
