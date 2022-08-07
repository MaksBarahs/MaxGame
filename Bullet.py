import pygame
from pygame import Rect
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,screen,settings,ship, _type="center"):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.ship = ship
        self._type = _type

        if self._type == "center":
            self.rect = Rect(0,0,self.settings.bulletwidth,self.settings.bulletheight)
        else:
            self.rect = Rect(0, 0,6, self.settings.bulletheight + 3)

        self.rect.midbottom = self.ship.rect.midtop
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        self.y -= self.settings.bulletspeed
        self.rect.y = self.y

        if self._type == "right":
            self.x += self.settings.bulletspeed
            self.rect.x = self.x
        elif self._type == "left":
            self.x -= self.settings.bulletspeed
            self.rect.x = self.x
    def Blitme(self):
        pygame.draw.rect(self.screen,self.settings.bulletcolor,self.rect)
