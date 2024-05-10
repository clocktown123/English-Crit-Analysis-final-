import pygame
import random

A = 0
D = 1
W = 2
S = 3

Right_car = pygame.image.load('Right_Car.png')
Left_car = pygame.image.load('Left_Car.png')

class car:
    def __init__(self):
        self.xpos = -100000
        self.ypos = 750
        self.xpos2 = 0
        self.ypos2 = 550
        self.xpos3 = -20000
        self.ypos3 = 350
        self.vx = 0
        self.vy = 0
        self.direction = D
    
    def drawRR(self, screen):
        for i in range(1000):
            screen.blit(Right_car, (self.xpos + i*200, self.ypos, 50, 50))
    
    def drawRR2(self, screen):
        for i in range(1000):
            screen.blit(Right_car, (self.xpos3 + i*200, self.ypos3, 50, 50))

    def drawLB(self, screen):
        for i in range(1000):
            screen.blit(Left_car, (self.xpos2 + i*200, self.ypos2, 50, 50))
        #screen.blit(Right_car, (self.xpos-100, self.ypos, 50, 50))
    
    def move(self):
        self.xpos += 3
        self.xpos2 -= 3
        self.xpos3 += 3

    #def collision(self, xpos, ypos):
        #if self.xpos < xpos + 50 and self.xpos + 50 > xpos and self.ypos < ypos + 50 and self.ypos + 50 > ypos:
           # print("hit")