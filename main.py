import pygame as pg
import sys
from setting import *
from Cube import Cube
from Transform import Transform


class App:
    def __init__(self):
        self.screen = pg.display.set_mode(RES)
        pg.init()
        #
        self.font = pg.font.SysFont('Arial', FONT_SIZE, bold=True)
        self.font_key = pg.font.SysFont('Arial', FONT_SIZE - 4, bold=False)
        self.clock = pg.time.Clock()
        #
        self.cube = Cube(self)
        self.transform = Transform(self,self.cube)

    def Run(self):
        while True:
            self.screen.fill((40,20,60))
            self.cube.draw()

            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                self.transform.control(event)

            self.clock.tick(5)

if __name__ == '__main__':
    app = App()
    app.Run()
