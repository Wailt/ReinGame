
# Импортируем библиотеку pygame
import pygame
from pygame import *

#Объявляем переменные
WIN_WIDTH = 400 #Ширина создаваемого окна
WIN_HEIGHT = 400 # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#FFFFFF"

def main():
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Super Mario Boy")  # Пишем в шапку
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон
    bg.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом

    while 1:  # Основной цикл программы
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == QUIT:
                raise (SystemExit, "QUIT")
        screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать

        pf = Surface((50, 50))
        pf.fill(Color('#000000'))
        screen.blit(pf, (100, 100))

        pygame.display.update()  # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    main()