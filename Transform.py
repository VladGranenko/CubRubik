from copy import copy
import pygame as pg

class Transform:
    def __init__(self,app, cube):
        self.app = app.screen
        self.font = app.font
        self.matrix_list = cube.side
        self.direction = {
            'right/left': 'top back bottom forward'.split(),
            'forward/back': 'top left bottom right'.split(),
            'top/bottom': 'forward right back left'.split(), }

    def rotate_space_reverse(self, key):
        """Вращение плоскости перпендикулярно оси
           против часовой стрелки"""
        #
        value_angle = copy(self.matrix_list[key][0][0])
        value_center = copy(self.matrix_list[key][0][1])
        #
        self.matrix_list[key][0][0] = self.matrix_list[key][0][2]
        self.matrix_list[key][0][2] = self.matrix_list[key][2][2]
        self.matrix_list[key][2][2] = self.matrix_list[key][2][0]
        self.matrix_list[key][2][0] = value_angle
        #
        self.matrix_list[key][0][1] = self.matrix_list[key][1][2]
        self.matrix_list[key][1][2] = self.matrix_list[key][2][1]
        self.matrix_list[key][2][1] = self.matrix_list[key][1][0]
        self.matrix_list[key][1][0] = value_center

    def rotate_space_behind(self, key):
        """Вращение плоскости перпендикулярно оси
           за часовой стрелкой"""
        #
        value_angle = copy(self.matrix_list[key][0][0])
        value_center = copy(self.matrix_list[key][0][1])
        #
        self.matrix_list[key][0][0] = self.matrix_list[key][2][0]
        self.matrix_list[key][2][0] = self.matrix_list[key][2][2]
        self.matrix_list[key][2][2] = self.matrix_list[key][0][2]
        self.matrix_list[key][0][2] = value_angle
        #
        self.matrix_list[key][0][1] = self.matrix_list[key][1][0]
        self.matrix_list[key][1][0] = self.matrix_list[key][2][1]
        self.matrix_list[key][2][1] = self.matrix_list[key][1][2]
        self.matrix_list[key][1][2] = value_center
#
    def rotate_plane(self,direct, course, index):
        """Вращение плоскости паралельно оси"""
        #
        matrix_due = copy(self.matrix_list[self.direction[direct][0]])
        for i in range(3):
            self.matrix_list[self.direction[direct][i * index]][0] = \
                self.matrix_list[self.direction[direct][(i + 1) * index]][0]
        #
        self.matrix_list[self.direction[direct][3 if index == 1 else 1]][0] = matrix_due[0]
        #
        if index == 1:
            self.rotate_space_reverse(key=course)
        elif index == -1:
            self.rotate_space_behind(key=course)

    def control(self,event):
        """Обработка клавиатуры"""

        if event.type == pg.KEYDOWN:
            press = pg.key.get_pressed()
            reverse = press[pg.K_p]
            # top
            if event.key == pg.K_w and not reverse:
                self.rotate_plane('top/bottom', course='top', index=1)
            if event.key == pg.K_w and reverse:
                self.rotate_plane('top/bottom', course='top', index=-1)
            # bottom
            if event.key == pg.K_x and not reverse:
                self.rotate_plane('top/bottom', course='bottom', index=1)
            if event.key == pg.K_x and reverse:
                self.rotate_plane('top/bottom', course='bottom', index=-1)
            # right
            if event.key == pg.K_f and not reverse:
                self.rotate_plane('right/left', course='right', index=1)
            if event.key == pg.K_f and reverse:
                self.rotate_plane('right/left', course='right', index=-1)
            # left
            if event.key == pg.K_a and not reverse:
                self.rotate_plane('right/left', course='left', index=1)
            if event.key == pg.K_a and reverse:
                self.rotate_plane('right/left', course='left', index=-1)
            # back
            if event.key == pg.K_s and not reverse:
                self.rotate_plane('forward/back', course='back', index=1)
            if event.key == pg.K_s and reverse:
                self.rotate_plane('forward/back', course='back', index=-1)
            # forward
            if event.key == pg.K_d and not reverse:
                self.rotate_plane('forward/back', course='forward', index=1)
            if event.key == pg.K_d and reverse:
                self.rotate_plane('forward/back', course='forward', index=-1)
















