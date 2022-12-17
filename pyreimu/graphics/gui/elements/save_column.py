import os

import pygame
import pyreimu.graphics.gui.uielement
import pyreimu.engine.save_file

class SaveColumn(pyreimu.graphics.gui.uielement.UIElement):
    def __init__(self, id):
        super(SaveColumn, self).__init__()
        self.save_file_id = id
        self.color = (230, 230, 255)
        self.rect = pygame.Rect(self.position.x, self.position.y, self.width, self.height)
        if os.path.exists('resources/saves/' + str(self.save_file_id) + '.rei'):
            self.save_file = pyreimu.engine.save_file.Save('resources/saves/' + str(self.save_file_id) + '.rei')
            self.save_file.load()
            self.string = r"Click to load save " + str(self.save_file_id) + "\n" + r"(last saved at " + self.save_file.get_time() + r")"
        else:
            self.string = "No save found"
        self.fontColour = (0, 0, 0)
        self.BGColour = (255, 255, 255)
        self.justification = 0
        self.font: pygame.font.Font = pygame.font.SysFont("arial", 30)
        self.font_height = self.font.get_height()


    def draw_and_update(self):
        self.rect = pygame.Rect(self.position.x + self.canvas.x, self.position.y + self.canvas.y, self.width,
                                self.height)
        self.bg_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.bg_surface.fill(self.color)
        pygame.display.get_surface().blit(self.bg_surface, self.rect)

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
        pygame.display.get_surface().blit(surface, (self.canvas.x + self.position.x + 5, self.canvas.y + self.position.y + 5))

        # if hover change color 
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.color = (200, 200, 255)
        else:
            self.color = (230, 230, 255)

    def is_clicked(self):
        # if save file exists
        if os.path.exists('resources/saves/' + str(self.save_file_id) + '.rei'):
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                return True
            else:
                return False