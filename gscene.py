#!/usr/bin/env python3

import pygame

# Paths
assets_path = "Assets/"
ch_path = assets_path + "Characters/"
bg_path = assets_path + "Backgrounds/"
db_path = assets_path + "Dialog/"


class GScene:
    """"Manages characters, music, backgrounds and dialogs
     belonging to a scene."""

    def __init__(self, filename):
        # File reading
        self.load(filename)
        self.next()

    def load(self, filename):
        self.file = open(filename, "r")

    def get_bg(self):
        return self.background

    def get_ch(self):
        return self.character

    def get_db(self):
        return self.dialog_box

    def get_text(self):
        return self.text

    def next(self):
        '''Reads next line in the script. Returns False if the scene hasn't
        ended. Returns True if it did end.'''
        line = self.file.readline().split(";")

        self.text = line[0]
        self.character = pygame.image.load(ch_path + character_dic[line[1]])
        self.background = pygame.image.load(bg_path + background_dic[line[4]])
        self.dialog_box = pygame.image.load(db_path + "1.png")


character_dic = {"DEF_CH": "1.jpg"}
background_dic = {"DEF_BG": "1.jpg"}
