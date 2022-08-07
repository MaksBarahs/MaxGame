from random import choice
import pygame
from pygame.sprite import Sprite
class Animy(Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.images = ["testallian.png"]
        #self.images = ["testallian.png", "BigMeteorTexture.png","MidMeteorTexture.png","smallmeteor.png"]
        self.image = pygame.image.load(f"images/{choice(self.images)}")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self._x = float(self.rect.x)

    def ChekEdges(self):
        screenRect = self.screen.get_rect()
        if self.rect.right >= screenRect.right or self.rect.left <= 0:
            return True
    def update(self):
        self._x += self.settings.animyspeed * self.settings.fleetderection
        self.rect.x = self._x

