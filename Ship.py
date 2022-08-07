import pygame

class Ship:
    def __init__(self,screen,settings):
        self.screen = screen
        self.screenrect = self.screen.get_rect()
        self.image = pygame.image.load("images/spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screenrect.midbottom
        self.settings = settings
        self._x = float(self.rect.x)
        self._y = float(self.rect.y)
        self.right = False
        self.left = False
        self.up = False
        self.down = False
    def Update(self):
        if self.right == True and self.rect.right < self.screenrect.right:
            self._x += self.settings.ShipSpeed
        if self.left == True and self.rect.left > self.screenrect.left:
            self._x -= self.settings.ShipSpeed
        if self.up == True and self.rect.top > self.screenrect.top:
            self._y -= self.settings.ShipSpeed
        if self.down == True and self.rect.bottom < self.screenrect.bottom:
            self._y += self.settings.ShipSpeed

        self.rect.x = self._x
        self.rect.y = self._y
    def Blitme(self):
        self.screen.blit(self.image,self.rect)