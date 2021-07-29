#!/usr/bin/env python3

import gscene
import pygame
import sys


class Engine:
    """Class that manages game mechanics and stores useful data"""

    def __init__(self, size):
        '''Class constructor and graphic engine initialization'''
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        self.bar_font = pygame.font.SysFont(None, 32)

        # # # CHARACTER # # #
        # Pair (height, width): size of characher's sprite
        self.ch_size = (int(self.screen.get_size()[0]*0.3),
                        int(self.screen.get_size()[1]*0.6))

        # Pair (x, y): top-left corner of characher's sprite
        self.ch_dest = (int(self.screen.get_size()[0]*0.65),
                        int(self.screen.get_size()[1]*0.1))

        # # # DIALOG BOX # # #
        # Pair (height, width): size of dialog box
        self.db_size = (int(self.screen.get_size()[0]),
                        int(self.screen.get_size()[1]*0.3))

        # Pair (x, y): top-left corner of dialog box
        self.db_dest = (0, int(self.screen.get_size()[1]*0.7))

        self.text_dest = (32, int(self.screen.get_size()[1]*0.75))

    def run(self):
        '''Main game loop'''
        # Scene switch controler
        new_scene = False

        # Test scene #
        self.scene = gscene.GScene("Assets/Dialog/test.csv")

        while True:
            # Texture reload is only done if required to optimize ressources
            # Load background
            self.bg = pygame.transform.smoothscale(self.scene.get_bg(),
                                                   self.screen.get_size())

            # Load characher
            self.ch = pygame.transform.smoothscale(self.scene.get_ch(),
                                                   self.ch_size)

            # Load dialog box
            self.db = pygame.transform.smoothscale(self.scene.get_db(),
                                                   self.db_size)

            # Load text
            self.text = self.bar_font.render(self.scene.get_text(), True,
                                             (0, 0, 0))
            while not(new_scene):
                # Event management
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

                # Draw
                self.screen.blit(self.bg, (0, 0))
                self.screen.blit(self.ch, self.ch_dest)
                self.screen.blit(self.db, self.db_dest)
                self.screen.blit(self.text, self.text_dest)
                pygame.display.flip()
