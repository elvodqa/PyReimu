import pygame.math


class UIElement:
    def __init__(self):
        self.width: int = 0
        self.height: int = 0
        self.position: pygame.math.Vector2 = pygame.math.Vector2(0, 0)
        self.canvas = None
        self.pressed = False

    def draw_and_update(self):
        pass

