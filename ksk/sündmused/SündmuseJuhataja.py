import pygame
import pygame_gui
import sys
from gui.Gui import GUIEkraan

class SündmuseJuhataja:
    def __init__(self, ekraan, gui):
        self.ekraan = ekraan
        self.gui = gui

    def töötle_sündmustega(self):
        """Töötle pygame'i sündmustega"""
        for sündmus in pygame.event.get():
            if sündmus.type == pygame.QUIT:
                del self.gui
                del self.ekraan
                sys.exit()
            self.gui.manager.process_events(sündmus)

            # Kustutab vana GUI ja ekraani ära ja initsialiseerib uued korraliku suurustega
            if sündmus.type == pygame.VIDEORESIZE:
                vana_ekraan = self.ekraan.ekraan
                vana_gui = self.gui.manager
                self.ekraan.ekraan = pygame.display.set_mode((sündmus.w, sündmus.h), pygame.RESIZABLE)

                self.gui.manager = pygame_gui.UIManager((sündmus.w, sündmus.h))
                self.gui.kinematics_window = GUIEkraan(self.gui.manager, self.ekraan)
                self.ekraan.ekraan.blit(vana_ekraan, (0,0))

                del vana_ekraan
                del vana_gui
                
                for objekt in self.ekraan.objektid:
                    objekt.alguspunkti_seadja((sündmus.w, sündmus.h))