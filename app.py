
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
    pygame.display.set_caption("Rein Game")  # Пишем в шапку
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    # будем использовать как фон
    bg.fill(Color(BACKGROUND_COLOR))  # Заливаем поверхность сплошным цветом
    n = 100
    x = 0
    pf = Surface((50, 50))
    pf.fill(Color('#000000'))
    while 1:  # Основной цикл программы
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == QUIT:
                raise (SystemExit, "QUIT")
            elif e.type == KEYDOWN and e.key == K_RIGHT:
                x = 1
            elif e.type == KEYDOWN and e.key == K_LEFT:
                x = -1
            elif e.type == KEYUP and e.key == K_RIGHT:
                x = 0
            elif e.type == KEYUP and e.key == K_LEFT:
                x = 0

            if e.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                print(pf.get_rect())
                pos = pygame.mouse.get_pos()
                print(pos)
                if pf.get_rect().collidepoint(pos):
                    pf.fill(Color('#00FF00'))





        n += x
        screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать
        screen.blit(pf, (n, 100))

        pygame.display.update()  # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    main()