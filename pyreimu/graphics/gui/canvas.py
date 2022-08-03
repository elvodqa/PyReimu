import pygame
from pyreimu.graphics.gui.uielement import *


class Canvas(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = pygame.display.get_surface().get_width()
        self.height = pygame.display.get_surface().get_height()
        self.elements = list()
        self.visible = False

    def add(self, element: UIElement):
        element.canvas = self
        self.elements.append(element)

    def send_mouse_press(self):
        if self.visible == True:
            for e in self.elements:
                e.pressed = True

    def draw_and_update(self):
        if self.visible == True:
            for e in self.elements:
                e.draw_and_update()
                e.pressed = False

