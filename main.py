#import modules
import math
import pygame as pg
import sys


def main():
    running = True
    t = 0
    dt = 0.01
    g = 9.8
    l = 300
    a = 0.05
    av = 1
    screen = pg.display.set_mode([500, 500])
    while running:
        x = (l * math.sin(a)) + 250
        y = (l * math.cos(a)) + 30
        screen.fill((255, 255, 255))
        pg.draw.line(
            start_pos=(30, 30), end_pos=(470, 30), color=(0, 0, 0), surface=screen
        )
        pg.draw.line(
            start_pos=(250, 30), end_pos=(x, y), surface=screen, color=(0, 0, 0)
        )
        pg.draw.circle(
            center=(x, y), radius=30, color=(0, 0, 0), surface=screen
        )
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        aa = -g * (math.sin(a))
        av = av + (aa * dt)
        a = a + (av * dt)
        t = t + dt
        pg.time.wait(30)
        pg.display.update()



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

