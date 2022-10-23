import pygame


class Player:
    def __init__(self, x, y, width, height, dx=0, dy=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dx = dx
        self.dy = dy

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_max_y(self):
        return self.y + self.height

    def get_max_x(self):
        return self.x + self.width

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def stop(self):
        self.x = self.y = 0

    def set_dy(self, dy):
        self.dy = dy

    def set_dx(self, dx):
        self.dx = dx

    def get_dy(self):
        return self.dy
