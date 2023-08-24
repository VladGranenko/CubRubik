import pygame as pg
from setting import *

class Cube:

    def __init__(self, app):
        self.app = app.screen
        self.font = app.font
        self.font_k = app.font_key
        #
        self.side = {'forward': [['red', 'red', 'red'],
                                 ['red', 'red', 'red'],
                                 ['red', 'red', 'red'],],

                     'back':[['orange','orange','orange'],
                             ['orange','orange','orange'],
                             ['orange','orange','orange'],],

                     'right':[['green','green','green'],
                              ['green','green','green'],
                              ['green','green','green'],],

                     'left':[['blue','blue','blue'],
                             ['blue','blue','blue'],
                             ['blue','blue','blue'],],

                     'bottom':[['yellow','yellow','yellow'],
                             ['yellow','yellow','yellow'],
                             ['yellow','yellow','yellow'],],

                     'top':[['white','white','white'],
                           ['white','white','white'],
                           ['white','white','white'],],}

    def get_rect(self,x,y,deltaX,deltaY):
        return x * (TILE + 4) + deltaX + dist_at_border, y * (TILE + 4) + (CENTER[1] - TILE * 1.5 + deltaY),\
                                                                                            TILE - 3, TILE - 3
    def pos_side(self,key):
        """Формирование плоскостей для построения сторон куба"""
        if key == 'forward':
            return [[pg.Rect(self.get_rect(x,y,deltaX=delta_beet_plane * 0,deltaY= 0)) for x in range(3)] for y in range(3)]
        if key == 'top':
            return [[pg.Rect(self.get_rect(x,y,deltaX= TILE * delta_beet_plane * 1,deltaY= 0)) for x in range(3)] for y in range(3)]
        if key == 'back':
            return [[pg.Rect(self.get_rect(x,y,deltaX= TILE * delta_beet_plane * 2 ,deltaY= 0)) for x in range(3)] for y in range(3)]
        if key == 'bottom':
            return [[pg.Rect(self.get_rect(x,y,deltaX= TILE * delta_beet_plane * 3,deltaY= 0)) for x in range(3)] for y in range(3)]
        if key == 'right':
            return [[pg.Rect(self.get_rect(x,y,deltaX= TILE * delta_beet_plane,deltaY= TILE * delta_beet_plane)) for x in range(3)] for y in range(3)]
        if key == 'left':
            return [[pg.Rect(self.get_rect(x,y,deltaX= TILE * delta_beet_plane,deltaY= (-TILE) * delta_beet_plane)) for x in range(3)] for y in range(3)]

    def draw(self):
        """Полная отрисовка """

        for side in SIDES:
            [pg.draw.rect(self.app,self.side[side][j][i],self.pos_side(side)[j][i]) for j in range(3) for i in range(3)]
            self.draw_border(side)
            self.render_plane(side)

    def draw_border(self,side):
        """Отрисовка границ"""

        center = self.pos_side(side)[1][1].center
        pg.draw.rect(self.app,'cyan',(center[0] - height_border,
                                      center[1] - height_border,height_border * 2, height_border * 2),width=TILE // 5)

    def render_plane(self,local, height= height_border + TILE):
        """Отрисовка надписей"""

        center = self.pos_side(local)[1][1].center
        LOCAL = local.upper()[0] + local[1:]
        self.render_side_title = self.font.render(f'{LOCAL}', False, self.side[local][1][1])
        w_render_s = self.render_side_title.get_width()
        self.app.blit(self.render_side_title, (center[0] - w_render_s // 2, center[1] - height))
        #
        self.rend_main_title = self.font.render('RUBIK\'S CUBE', True, 'purple')
        self.rend_int_key = self.font_k.render('REVERSE PRESS: P', True, 'cyan')
        self.rend_keylist = [self.font_k.render(f'{SIDES[i][0].upper() + SIDES[i][1:]}: press {KEY_LIST[i]}', True, 'orange')
                             for i in range(6)]
        #
        [self.app.blit(self.rend_keylist[j],(WIDTH - DIST_INSC, 200 + j * 50)) for j in range(6)]
        self.app.blit(self.rend_int_key, (WIDTH - DIST_INSC, 150))
        self.app.blit(self.rend_main_title, (WIDTH - DIST_INSC, 50))






