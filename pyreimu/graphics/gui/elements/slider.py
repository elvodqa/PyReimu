import pygame
from pyreimu.graphics.gui.uielement import UIElement

class Slider(UIElement):
    def __init__(self, x, y, min, max):
        super(Slider, self).__init__()

        self.min = min
        self.max = max
        self.value = 0
        self.width = 100
        self.height = 20
        self.position = pygame.math.Vector2(x, y)
        self.rect = pygame.Rect(self.position.x, self.position.y, self.width, self.height)
        self.color = (140, 70, 120)
        self.hover_color = (70, 30, 30)
        self.current_color = self.color
        self.pressed = False
        self.on_press = None

    def draw_and_update(self):
        self.rect = pygame.Rect(self.position.x + self.canvas.x, self.position.y + self.canvas.y, self.width, self.height)

        pygame.draw.rect(pygame.display.get_surface(), self.current_color, self.rect)

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.current_color = self.hover_color
        else:
            self.current_color = self.color
        
        if self.pressed:
            if self.on_press is not None:
                self.on_press()
            
            self.value = pygame.mouse.get_pos()[0] - self.rect.x

        if pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.pressed = True
        else:
            self.pressed = False

    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value

        
     
    