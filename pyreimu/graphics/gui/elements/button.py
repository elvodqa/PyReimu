import pygame
from pyreimu.graphics.gui.elements.text import Text
from pyreimu.graphics.gui.uielement import UIElement


class Button(UIElement):
    def __init__(self):
        super(Button, self).__init__()


        self.string = ""
        self.fontColour = (0, 0, 0)
        self.BGColour = (255, 255, 255)
        self.justification = 0
        self.font = pygame.font.SysFont("arial", 30)
        self.font_height = self.font.get_height()
        self.justification = 1

        self.color = (140, 70, 120)
        self.hover_color = (70, 30, 30)
        self.current_color = self.color
        self.rect = pygame.Rect(self.position.x, self.position.y, self.width, self.height)
        self.pressed = False
        self.on_press = None

    def draw_and_update(self):
        self.rect = pygame.Rect(self.position.x + self.canvas.x, self.position.y + self.canvas.y, self.width, self.height)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_rect = pygame.Rect(mouse_x, mouse_y, 1, 1)

        if self.rect.colliderect(mouse_rect):
            self.current_color = self.hover_color
            if self.pressed:
                try:
                    self.on_press()
                except TypeError:
                    print("On press is not set to a function.")
        else:
            self.current_color = self.color

        pygame.draw.rect(
            pygame.display.get_surface(),
            self.current_color,
            self.rect
        )

        finalLines = []
        requestedLines = self.string.splitlines()
        # Create a series of lines that will fit on the provided
        # rectangle.
        for requestedLine in requestedLines:
            if self.font.size(requestedLine)[0] > self.rect.width:
                words = requestedLine.split(' ')
                # if any of our words are too long to fit, return.
                for word in words:
                    if self.font.size(word)[0] >= self.rect.width:
                        raise Exception("The word " + word + " is too long to fit in the rect passed.")
                # Start a new line
                accumulatedLine = ""
                for word in words:
                    testLine = accumulatedLine + word + " "
                    # Build the line while the words fit.
                    if self.font.size(testLine)[0] < self.rect.width:
                        accumulatedLine = testLine
                    else:
                        finalLines.append(accumulatedLine)
                        accumulatedLine = word + " "
                finalLines.append(accumulatedLine)
            else:
                finalLines.append(requestedLine)

        # Let's try to write the text out on the surface.
        surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        # surface.fill(self.BGColour)
        accumulatedHeight = 0
        for line in finalLines:
            if accumulatedHeight + self.font.size(line)[1] >= self.rect.height:
                raise Exception("Once word-wrapped, the text string was too tall to fit in the rect.")
            if line != "":
                tempSurface = self.font.render(line, 1, self.fontColour)
            if self.justification == 0:
                surface.blit(tempSurface, (0, accumulatedHeight))
            elif self.justification == 1:
                surface.blit(tempSurface, ((self.rect.width - tempSurface.get_width()) / 2, accumulatedHeight))
            elif self.justification == 2:
                surface.blit(tempSurface, (self.rect.width - tempSurface.get_width(), accumulatedHeight))
            else:
                raise Exception("Invalid justification argument: " + str(self.justification))
            accumulatedHeight += self.font.size(line)[1]
        pygame.display.get_surface().blit(surface, (self.position.x, self.position.y))

