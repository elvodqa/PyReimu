import pygame
import pyreimu.graphics.gui.uielement

class Text(pyreimu.graphics.gui.uielement.UIElement):
    def __init__(self):
        super(Text, self).__init__()

        self.string = ""
        self.fontColour = (0, 0, 0)
        self.BGColour = (255, 255, 255)
        self.justification = 0
        self.font: pygame.font.Font = pygame.font.SysFont("arial", 30)
        self.font_height = self.font.get_height()
        self.width = 220
        self.height = 300
        self.rect: pygame.rect.Rect = pygame.rect.Rect(self.position.x, self.position.y, self.width, self.height)

    def draw_and_update(self):
        """Returns a surface containing the passed text string, reformatted
        to fit within the given rect, word-wrapping as necessary. The text
        will be anti-aliased.

        Parameters
        ----------
        string - the text you wish to render. \n begins a new line.
        font - a Font object
        rect - a rect style giving the size of the surface requested.
        fontColour - a three-byte tuple of the rgb value of the
                 text color. ex (0, 0, 0) = BLACK
        BGColour - a three-byte tuple of the rgb value of the surface.
        justification - 0 (default) left-justified
                    1 horizontally centered
                    2 right-justified

        Returns
        -------
        Success - a surface object with the text rendered onto it.
        Failure - raises a TextRectException if the text won't fit onto the surface.
        """



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
        #surface.fill(self.BGColour)
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
        pygame.display.get_surface().blit(surface, (self.canvas.x + self.position.x, self.canvas.y + self.position.y))
        #return surface

    def set_text(self, text: str):
        self.string = text
        self.height = self.font_height * len(self.string.splitlines())
        self.rect = pygame.rect.Rect(self.position.x, self.position.y, self.width, self.height)
    
    def set_font(self, font: pygame.font.Font):
        self.font = font
        self.height = self.font_height * len(self.string.splitlines())
        self.rect = pygame.rect.Rect(self.position.x, self.position.y, self.width, self.height)