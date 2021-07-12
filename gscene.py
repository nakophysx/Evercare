import pygame

# Paths
assets_path = "Assets/"
ch_path = assets_path + "Characters/"
bg_path = assets_path + "Backgrounds/"


class GScene:
    """"Manages characters, music, backgrounds and dialogues
     belonging to a scene."""
    # (surface, rect)
    characters = []
    current_ch = 0

    # surface
    backgrounds = []
    current_bg = 0

    sound = []
    current_sound = 0
    music = []
    current_m = 0

    # (string, ch_id, bg_id, sound_id, music_id)
    script = []
    current = 0

    def __init__(self, filename):
        # file reading that fills in this automatically
        img = pygame.image.load(bg_path+filename)
        self.backgrounds.append(img)

    def get_bg(self):
        return self.backgrounds[self.current_bg]

# enum Characters
# enum Backgrounds
# enum ...
