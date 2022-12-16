import sys
from time import time
import pygame

import pyreimu.graphics.gui.canvas
import pyreimu.graphics.gui.elements

class Dialogue:
    def __init__(self, text, speaker_name, options = []):
        self.text = text
        self.speaker_name = speaker_name
        self.options = options

class Pyreimu:
    def __init__(self, title):
        self.state = "main_menu"

        self.current_speaker = None
        self.dialogue = []
        self.dialogue_index = 0

        pygame.init()
        self.title = title
        pygame.display.set_caption(self.title)
        self.screen = pygame.display.set_mode([800, 600], pygame.RESIZABLE | pygame.SCALED, vsync=1, depth=32)
        self.clear_color = pygame.color.Color(88, 85, 83, 255)
        self.running = True
        self.open_options = False
        self.open_load = False
        #------------------- MAIN MENU ------------------------
        self.menu_canvas = pyreimu.graphics.gui.canvas.Canvas()

        self.main_title = pyreimu.graphics.gui.elements.text.Text()
        self.main_title.font = pygame.font.SysFont("arial", 39)
        self.main_title.justification = 1
        self.main_title.rect.width = 240
        self.main_title.rect.height = 400
        self.main_title.position.x = -10
        self.main_title.position.y = 110
        self.main_title.fontColour = (255, 255, 255)
        self.main_title.string = self.title

        self.menu_bg = pyreimu.graphics.gui.elements.panel.Panel()
        self.menu_bg.width = 200
        self.menu_bg.height = 800

        self.start_button = pyreimu.graphics.gui.elements.button.Button()
        self.start_button.fontColour = (255, 255, 255)
        self.start_button.width = 120
        self.start_button.height = 40
        self.start_button.position = pygame.math.Vector2(40, 240)
        self.start_button.string = "Start"


        self.load_button = pyreimu.graphics.gui.elements.button.Button()
        self.load_button.fontColour = (255, 255, 255)
        self.load_button.width = 120
        self.load_button.height = 40
        self.load_button.position = pygame.math.Vector2(40, 300)
        self.load_button.string = "Load"

        self.options_button = pyreimu.graphics.gui.elements.button.Button()
        self.options_button.fontColour = (255, 255, 255)
        self.options_button.width = 120
        self.options_button.height = 40
        self.options_button.position = pygame.math.Vector2(40, 360)
        self.options_button.string = "Options"

        self.quit_button = pyreimu.graphics.gui.elements.button.Button()
        self.quit_button.fontColour = (255, 255, 255)
        self.quit_button.width = 120
        self.quit_button.height = 40
        self.quit_button.position = pygame.math.Vector2(40, 420)
        self.quit_button.string = "Quit"

        self.bg_image = pyreimu.graphics.gui.elements.image.Image("shrek.jpeg")
        ratio = self.bg_image.image.get_width() / self.bg_image.image.get_width()
        self.bg_image.image = pygame.transform.scale(self.bg_image.image, (800 * ratio, 600 * ratio))


        self.menu_canvas.add(self.bg_image)
        self.menu_canvas.add(self.menu_bg)
        self.menu_canvas.add(self.main_title)
        self.menu_canvas.add(self.start_button)
        self.menu_canvas.add(self.load_button)
        self.menu_canvas.add(self.options_button)
        self.menu_canvas.add(self.quit_button)
        self.menu_canvas.visible = True
        # ------------------- MAIN MENU (END)------------------------

        # ------------------- LOAD MENU ------------------------
        self.load_canvas = pyreimu.graphics.gui.canvas.Canvas()
        self.load_canvas.x = 200
        self.load_canvas.width = 600

        self.load_panel = pyreimu.graphics.gui.elements.panel.Panel()
        self.load_panel.width = self.load_canvas.width
        self.load_panel.height = self.load_canvas.height
        self.load_panel.color = (140, 70, 120, 200)

        self.load_save_column_1 = pyreimu.graphics.gui.elements.save_column.SaveColumn(1)
        self.load_save_column_1.position = pygame.math.Vector2(40, 100)
        self.load_save_column_1.width = 500
        self.load_save_column_1.height = 100

        self.load_save_column_2 = pyreimu.graphics.gui.elements.save_column.SaveColumn(2)
        self.load_save_column_2.position = pygame.math.Vector2(40, 250)
        self.load_save_column_2.width = 500
        self.load_save_column_2.height = 100

        self.load_save_column_3 = pyreimu.graphics.gui.elements.save_column.SaveColumn(3)
        self.load_save_column_3.position = pygame.math.Vector2(40, 400)
        self.load_save_column_3.width = 500
        self.load_save_column_3.height = 100

        self.load_text = pyreimu.graphics.gui.elements.text.Text()
        self.load_text.string = "Load Save"
        self.load_text.justification = 1
        self.load_text.rect = pygame.Rect(
            self.load_canvas.x,
            self.load_canvas.y,
            self.load_canvas.width,
            self.load_canvas.height
        )
        self.load_text.position.y += 20
        self.load_text.fontColour = (255, 255, 255)

        self.load_canvas.add(self.load_panel)
        self.load_canvas.add(self.load_text)
        self.load_canvas.add(self.load_save_column_1)
        self.load_canvas.add(self.load_save_column_2)
        self.load_canvas.add(self.load_save_column_3)

        self.load_canvas.visible = False

        # ------------------- LOAD MENU (END)------------------------

        # ------------------- OPTIONS MENU ------------------------
        self.options_canvas = pyreimu.graphics.gui.canvas.Canvas()
        self.options_canvas.x = 200
        self.options_canvas.width = 600

        self.options_panel = pyreimu.graphics.gui.elements.panel.Panel()
        self.options_panel.width = self.options_canvas.width
        self.options_panel.height = self.options_canvas.height
        self.options_panel.color = (140, 70, 120, 200)

        self.options_text = pyreimu.graphics.gui.elements.text.Text()
        self.options_text.string = "Options"
        self.options_text.justification = 1
        self.options_text.rect = pygame.Rect(
            self.options_canvas.x,
            self.options_canvas.y,
            self.options_canvas.width,
            self.options_canvas.height
        )
        self.options_text.position.y += 20
        self.options_text.fontColour = (255, 255, 255)

        self.options_canvas.add(self.options_panel)
        self.options_canvas.add(self.options_text)

        self.options_canvas.visible = False

        # ------------------- OPTIONS MENU (END)------------------------


        # ------------------- GAME ------------------------
        self.dialogue_canvas = pyreimu.graphics.gui.canvas.Canvas()
        self.dialogue_canvas.x = 75
        self.dialogue_canvas.width = pygame.display.get_surface().get_width() - 150
        self.dialogue_canvas.y = pygame.display.get_surface().get_height() - 115
        self.dialogue_canvas.height = 100
        self.dialogue_canvas.visible = True
        self.dialogue_text = pyreimu.graphics.gui.elements.text.Text()
        self.dialogue_text.string = "...press space to start/continue..."
        self.dialogue_text.justification = 0
        #self.dialogue_text.set_font(pygame.font.SysFont("arial", 20))
        self.dialogue_text.font = pygame.font.SysFont("arial", 20)

        self.speaker_text = pyreimu.graphics.gui.elements.text.Text()
        self.speaker_text.string = "speaker_text"
        self.speaker_text.justification = 0
        self.speaker_text.font = pygame.font.SysFont("arial", 20)
        #self.speaker_text.position.y = self.dialogue_canvas.y - 20
        #self.speaker_text.position.x = self.dialogue_canvas.x

        self.dialogue_bg = pyreimu.graphics.gui.elements.panel.Panel()
        self.dialogue_bg.width = self.dialogue_canvas.width
        self.dialogue_bg.height = self.dialogue_canvas.height
        self.dialogue_bg.color = (140, 70, 120, 200)
        self.dialogue_canvas.add(self.dialogue_bg)

        self.dialogue_text.rect = pygame.Rect(
            self.dialogue_canvas.x,
            self.dialogue_canvas.y,
            self.dialogue_canvas.width,
            self.dialogue_canvas.height
        )

        self.speaker_text.rect = pygame.Rect(  
            self.speaker_text.position.x,
            self.speaker_text.position.y,
            self.speaker_text.width,
            self.speaker_text.height
        )

        self.dialogue_text.position.y += 20
        self.dialogue_text.fontColour = (255, 255, 255)
        self.dialogue_canvas.add(self.dialogue_text)
        self.dialogue_canvas.add(self.speaker_text)



        # ------------------- BUTTON SETUPS ----------------------------

        def start_pressed():
            self.state = "game"
        self.start_button.on_press = start_pressed

        def load_pressed():
            if self.open_load == False:
                if self.open_options == True:
                    self.options_canvas.visible = False
                    self.open_options = False
                self.load_canvas.visible = True
                self.open_load = True
            else:
                self.load_canvas.visible = False
                self.open_load = False
        self.load_button.on_press = load_pressed

        def options_pressed():
            if self.open_options == False:
                if self.open_load == True:
                    self.load_canvas.visible = False
                    self.open_load = False
                self.options_canvas.visible = True
                self.open_options = True
            else:
                self.options_canvas.visible = False
                self.open_options = False
        self.options_button.on_press = options_pressed

        def quit_pressed():
            self.running = False
        self.quit_button.on_press = quit_pressed

        # ------------------- BUTTON SETUPS (END) ----------------------------

        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:
            time_delta = self.clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.menu_canvas.send_mouse_press()
                    self.options_canvas.send_mouse_press()
                    self.load_canvas.send_mouse_press()
                # space down
                if event.type == pygame.KEYDOWN and event.key == 32:
                    match(self.state):
                        case "main_menu":
                            pass
                        case "game":
                            if self.dialogue_index < len(self.dialogue):
                                self.dialogue_text.string = self.dialogue[self.dialogue_index].text
                                self.speaker_text.string = self.dialogue[self.dialogue_index].speaker_name
                                self.dialogue_index += 1
                # esc dowmn
                if event.type == pygame.KEYDOWN and event.key == 27:
                    match(self.state):
                        case "main_menu":
                            pass
                        case "game":
                            self.state = "main_menu"
                            self.dialogue_index = 0
                            self.dialogue_text.string = "...press space to start/continue..."
                            self.speaker_text.string = "speaker_text"
                            
                                

            self.screen.fill(self.clear_color)
            match(self.state):
                case "main_menu":
                    self.menu_canvas.draw_and_update()
                    self.options_canvas.draw_and_update()
                    self.load_canvas.draw_and_update()
                case "game":
                    self.dialogue_canvas.draw_and_update()
                    

            pygame.display.flip()

        pygame.quit()
        sys.exit(0)
    
    def load_save(self, save_number):
        pass

    def speaker(self, speaker):
        self.speaker_name = speaker

    def talk(self, text):
        self.dialogue.append(Dialogue(text, self.speaker_name))
