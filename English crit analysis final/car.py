import pygame
import random

A = 0
D = 1
W = 2
S = 3

Right_car = pygame.image.load('Right_Car.png')

class car:
    def __init__(self):
        self.xpos = -10000
        self.ypos = 750
        self.vx = 0
        self.vy = 0
        self.direction = D
    
    def draw(self, screen):
        for i in range(1000):
            screen.blit(Right_car, (self.xpos + i*200, self.ypos, 50, 50))
        #screen.blit(Right_car, (self.xpos-100, self.ypos, 50, 50))
    
    def move(self):
            self.xpos += 3