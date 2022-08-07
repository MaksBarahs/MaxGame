class Settings:
    def __init__(self):
        # Параметры корабля
        self.width = 1600
        self.height = 900
        self.color = (29,32,200)
        self.ShipSpeed = 2.8

        # Параметры пуль
        self.bulletwidth = 20
        self.bulletheight = 20
        self.bulletcolor = (255,255,0)
        self.bulletspeed = 3.0

        # Параметры врагов
        self.animyspeed = 1.6
        self.animydrop = 20
        self.fleetderection = 1