import pygame
import pyreimu.graphics.gui.uielement

class Panel(pyreimu.graphics.gui.uielement.UIElement):
    def __init__(self):
        super(Panel, self).__init__()
        self.color = (230, 230, 230, 120)
        self.rect = pygame.Rect(self.position.x, self.position.y, self.width, self.height)

    def draw_and_update(self):
        self.rect = pygame.Rect(self.position.x + self.canvas.x, self.position.y + self.canvas.y, self.width, self.height)
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.surface.fill(self.color)
        pygame.display.get_surface().blit(self.surface, self.rect)
