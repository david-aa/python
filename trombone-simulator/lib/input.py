from lib.common import *
from lib.resources import Score, Sound, Trombone
import pygame

class StandardGUI:
    MARGIN_TOP = 110
    KEYBD_WIDTH = 615
    WHITE_KEY_HEIGHT = KEYBD_HEIGHT = 240
    BLACK_KEY_HEIGHT = 157
    areas = {  # (x, y, witdh, height)
        (10, MARGIN_TOP, 26, WHITE_KEY_HEIGHT): 40,  # Very low E
        (41, MARGIN_TOP, 26, WHITE_KEY_HEIGHT): 41,
        (72, MARGIN_TOP, 14, BLACK_KEY_HEIGHT): 42,
        (86, MARGIN_TOP, 20, WHITE_KEY_HEIGHT): 43,
        (109, MARGIN_TOP, 14, BLACK_KEY_HEIGHT): 44,
        (124, MARGIN_TOP, 20, WHITE_KEY_HEIGHT): 45,
        (147, MARGIN_TOP, 14, BLACK_KEY_HEIGHT): 46,
        (162, MARGIN_TOP, 28, WHITE_KEY_HEIGHT): 47,
        (194, MARGIN_TOP, 28, WHITE_KEY_HEIGHT): 48,  # Low C
        (223, MARGIN_TOP, 14, BLACK_KEY_HEIGHT): 49,
        (239, MARGIN_TOP, 20, WHITE_KEY_HEIGHT): 50,
        (261, MARGIN_TOP, 14, BLACK_KEY_HEIGHT): 51,
        (277, MARGIN_TOP, 26, WHITE_KEY_HEIGHT): 52,
        (309, MARGIN_TOP, 28, WHITE_KEY_HEIGHT): 53,  # Central F
        (339, MARGIN_TOP, 14, BLACK_KEY_HEIGHT): 54,
        (354, MARGIN_TOP, 20, WHITE_KEY_HEIGHT): 55,
        (378, MARGIN_TOP, 14, BLACK_KEY_HEIGHT): 56,
        (391, MARGIN_TOP, 20, WHITE_KEY_HEIGHT): 57,
        (415, MARGIN_TOP, 14, BLACK_KEY_HEIGHT): 58,
        (430, MARGIN_TOP, 28, WHITE_KEY_HEIGHT): 59,
        (462, MARGIN_TOP, 28, WHITE_KEY_HEIGHT): 60,  # High C
        (492, MARGIN_TOP, 14, BLACK_KEY_HEIGHT): 61,
        (506, MARGIN_TOP, 20, WHITE_KEY_HEIGHT): 62,
        (529, MARGIN_TOP, 14, BLACK_KEY_HEIGHT): 63,
        (545, MARGIN_TOP, 26, WHITE_KEY_HEIGHT): 64,
        (576, MARGIN_TOP, 28, WHITE_KEY_HEIGHT): 65,
        }
    current_audio = None
    current_staff = None
    current_image = None
    def input(self, events): 
        for event in events: 
            if event.type == pygame.QUIT: 
                sys.exit(0) 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for rect, note in self.areas.items():
                    if pygame.Rect(rect).collidepoint(event.pos):
                        self.current_image = pygame.image.load(Trombone(NOTES[note]['position']).path)
                        self.screen.blit(self.current_image, (0, 0))
                        self.current_staff = pygame.image.load(Score(note).path)
                        self.screen.blit(self.current_staff, (self.KEYBD_WIDTH - self.current_staff.get_size()[0], 0))
                        self.current_audio = self.sounds[note]
                        self.current_audio.play(-1)
            elif event.type == pygame.MOUSEBUTTONUP:
#                self.current_image = pygame.image.load(Trombone(0).path)
#                self.screen.blit(self.current_image, (0, 0))
#                self.current_staff = pygame.image.load(Score(0).path)
#                self.screen.blit(self.current_staff, (self.KEYBD_WIDTH - self.current_staff.get_size()[0], 0))
                if self.current_audio:
                    self.current_audio.stop()
            pygame.display.flip()


    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        clock = pygame.time.Clock()
        background = (165, 165, 165)
        self.sounds = {}
        for note in NOTES.keys():
            self.sounds[note] = pygame.mixer.Sound(Sound(note).path)
        self.keyboard = pygame.image.load(os.path.join(DIR_IMG, 'piano.png'))
        self.size = (self.KEYBD_WIDTH, self.KEYBD_HEIGHT + self.MARGIN_TOP)
        self.screen = pygame.display.set_mode(self.size)		
        self.screen.fill(background)
        self.screen.blit(self.keyboard, (0, self.MARGIN_TOP))
        pygame.display.set_caption('Trombone Simulator')
        pygame.display.flip()
        while True:
            self.input(pygame.event.get())
            clock.tick(50)

