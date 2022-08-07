import pygame
import sys
import animy
import Bullet
from Settings import Settings
from Ship import Ship

class SpaseAdventure():
    def __init__(self):
        # Инициализация движка
        pygame.init()
        # Создание объекта настроек
        self.settings = Settings()
        # Сохранение экрана с разрешением из настроек
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.width = self.screen.get_width()
        self.settings.height = self.screen.get_height()
        # Создание объекта корабля
        self.Ship = Ship(self.screen,self.settings)
        pygame.display.set_caption("SpaseAdventure")
        # контейнер спрайтов
        self.bullets = pygame.sprite.Group()
        self.animys = pygame.sprite.Group()
        self.CreateAnimy()
        self.CreateFleet()

    def CreateAnimy(self):
        # Создаем объект пришельца
        animy1 = animy.Animy(self)
        # Добавляем объект пришельца в контейнер
        self.animys.add(animy1)

    def CreateFleet(self):
        # Создаем объект пришельца для того, чтобы узнать его ширину
        _animy = animy.Animy(self)
        # Вытаскиваем ширину пришельца (необходимо для формулы)
        animywidth = _animy.rect.width
        # Пустое пространство, в котором будут спавниться пришельцы в пикселях (справа и слева пустые места размером с пришельца)
        space = self.screen.get_width() - 2 * animywidth
        # Кол-во пришельцев = пустое пространство / (2 * ширина пришельца) - т.к. каждый пришелец будет занимать в два раза больше места, чтобы они не были  в притык
        n = space//(2 * animywidth)
        for i in range(0,n + 1):
            # Создаем объект пришельца
            animy_ = animy.Animy(self)
            # Смещаем пришельца на i * ширину * 2
            # i - сколько пришельцев сзади
            # ширина * 2 - сколько пикселей занимает один пришелец
            # итого каждого следующего пришельца необходимо сдвигать на i * width * 2
            animy_.rect.x += i * animywidth * 2
            # Пересохраняем x
            animy_._x = animy_.rect.x
            # Добавляем врага в контейнер
            self.animys.add(animy_)
    def Fire(self):
        bullet = Bullet.Bullet(self.screen,self.settings,self.Ship)
        self.bullets.add(bullet)
    def FireThreeble(self):
        bullet = Bullet.Bullet(self.screen, self.settings, self.Ship)
        bulletright = Bullet.Bullet(self.screen, self.settings, self.Ship, "another")
        bulletright.rect.x += 32
        bulletleft = Bullet.Bullet(self.screen, self.settings, self.Ship, "another")
        bulletleft.rect.x -= 32
        self.bullets.add(bullet)
        self.bullets.add(bulletright)
        self.bullets.add(bulletleft)
    def FireALotOf(self,n):
        a = 10
        right = 0
        left = a
        for i in range(0,n):
            bullet = Bullet.Bullet(self.screen,self.settings,self.Ship,"another")
            if i % 2 == 0:
                bullet.rect.x += right
                right += a
            else:
                bullet.rect.x -= left
                left += a
            self.bullets.add(bullet)

    def FireSpred(self):
        bullet = Bullet.Bullet(self.screen,self.settings,self.Ship)
        bullet.rect.width = 10
        bullet.rect.height = 10
        bulletright = Bullet.Bullet(self.screen,self.settings,self.Ship,"right")
        bulletright.rect.width = 10
        bulletright.rect.height = 10
        bulletleft = Bullet.Bullet(self.screen,self.settings,self.Ship,"left")
        bulletleft.rect.width = 10
        bulletleft.rect.height = 10
        self.bullets.add(bullet)
        self.bullets.add(bulletright)
        self.bullets.add(bulletleft)

    def AnimyUpdate(self):
        # Если контейнер спрайтов (врагов) пуст
        if not self.animys:
            # Очищаем контйнер пуль
            self.bullets.empty()
            # Создаем новый флот
            self.CreateFleet()

        # Проходим всех врагов
        for animy in self.animys.sprites():
            # Если враг находится на краю
            if animy.ChekEdges() == True:
                # Меняем направление флота
                self.settings.fleetderection *= -1
                # Снижаем флот
                self.AnimyDrop()
                break
        # Обновляем врагов
        self.animys.update()

    def AnimyDrop(self):
        for animy in self.animys.sprites():
            animy.rect.y += self.settings.animydrop

    def UpdateBullets(self):
        self.bullets.update()
        # УДАЛЯЕМ НЕНУЖНЫЕ ПУЛИ
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Коллизия групп - 1 - группа 1, 2 - группа 2, 3 - True/False - уничтожение при коллизии из первой группы, 4 - со второй
        pygame.sprite.groupcollide(self.bullets,self.animys, True,True)
    def Start(self):
        while True:
            # Чекаем события
            self.ChekEvents()
            # Обновляем корабль
            self.Ship.Update()
            # Обновляем пули
            self.UpdateBullets()
            self.AnimyUpdate()


            #print(len(self.bullets))

            # Обновляем экран
            self.UpdateScreen()
    def ChekEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.ChekDown(event)
            elif event.type == pygame.KEYUP:
                self.ChekUp(event)

    def ChekDown(self,event):
        if event.key == pygame.K_d:
            self.Ship.right = True
        elif event.key == pygame.K_a:
            self.Ship.left = True
        elif event.key == pygame.K_w:
            self.Ship.up = True
        elif event.key == pygame.K_s:
            self.Ship.down = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_KP_ENTER:
            self.Fire()
        elif event.key == pygame.K_KP0:
            self.FireThreeble()
        elif event.key == pygame.K_KP_5:
            self.FireALotOf(27)
        elif event.key == pygame.K_KP_2:
            self.FireSpred()
    def ChekUp(self,event):
        if event.key == pygame.K_d:
            self.Ship.right = False
        elif event.key == pygame.K_a:
            self.Ship.left = False
        elif event.key == pygame.K_w:
            self.Ship.up = False
        elif event.key == pygame.K_s:
            self.Ship.down = False


    def UpdateScreen(self):
        self.screen.fill(self.settings.color)
        self.Ship.Blitme()
        for bullet in self.bullets.sprites():
            bullet.Blitme()
        self.animys.draw(self.screen)
        pygame.display.flip()
spase=SpaseAdventure()
spase.Start()

