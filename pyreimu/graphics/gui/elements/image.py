import pygame
import pyreimu.graphics.gui.uielement

class Image(pyreimu.graphics.gui.uielement.UIElement):
    def __init__(self, image_name):
        super(Image, self).__init__()

        self.destination_folder = "resources/images"
        self.image_source = image_name

        self.image = pygame.image.load(self.destination_folder + "/" + self.image_source).convert_alpha()

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect(
            self.position.x,
            self.position.y,
            self.width,
            self.height
        )


    def draw_and_update(self):

        self.rect = pygame.Rect(
            self.position.x + self.canvas.x,
            self.position.y + self.canvas.y,
            self.width,
            self.height
        )

        pygame.display.get_surface().blit(self.image, (0, 0))
