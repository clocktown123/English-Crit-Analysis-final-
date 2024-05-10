import pygame
from pygame import mixer
from map import MapF
from car import car
from Player import player
import random

mixer.init()
pygame.init()
pygame.display.set_caption("top down grid map game")
screen = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()

p1 = player()
C = car()

A = 0
D = 1
W = 2
S = 3
SPACE = 4
F = 5
keys = [False, False, False, False, False, False]

worker = pygame.image.load('worker.png') #load your spritesheet
worker.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of

#game state variable
state = 1 #1 is menu, 2 is playing, 3 is credits
button1 = False

mxpos = 0
mypos = 0

mousePos = (mxpos, mypos)
mouseDown = False

ticket = False

ticker = 0

mapNum = 1

Counter = 0

Green = False
Yellow = False
Red = False

def pls(counter):
    if mousePos[0] > 300 and mousePos[0] < 347 and mousePos[1] > 270 and mousePos[1] < 345 and mouseDown == True:
        counter += 1

#dialog = False
#dialog2 = False

map = [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
       [2,2,2,2,2,2,2,2,3,3,3,3,2,2,2,2,2,2,2,2],
       [2,2,2,2,2,2,2,3,3,3,3,3,3,2,2,2,2,2,2,2],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
       [2,2,2,2,2,2,2,2,2,4,4,2,2,2,2,2,2,2,2,2],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

map2 = [[2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,8,2,2,2,2],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,4,4,2,2,2,2,2],
       [2,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,6,6,6,6,6,6,6,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2]]


text_font = pygame.font.SysFont("Sans", 30, bold = True)

def draw_text(text, font, text_col, tx, ty):
    img = font.render(text, True, text_col)
    screen.blit(img, (tx, ty))

while 1: #GAME LOOP######################################################
    clock.tick(60) # fps
    ticker+=1
    #C.xpos += .1
    #input section--------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
            
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                keys[SPACE] = True
            if event.key == pygame.K_f:
                keys[F] = True
             
            
            if event.key == pygame.K_a:
                keys[A] = True
                #RowNum = 0
            if event.key == pygame.K_d:
                keys[D] = True
                #RowNum = 3
            if event.key == pygame.K_w:
                keys[W] = True
                #RowNum = 1
            if event.key == pygame.K_s:
                keys[S] = True
                #Rowum = 2
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                keys[SPACE] = False
            if event.key == pygame.K_f:
                keys[F] = False

            if event.key == pygame.K_a:
                keys[A] = False
                #RowNum = 0
            if event.key == pygame.K_d:
                keys[D] = False
                #RowNum = 3
            if event.key == pygame.K_w:
                keys[W] = False
                #RowNum = 1
            if event.key == pygame.K_s:
                keys[S] = False
                #RowNum = 2
            
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
        #keeps track of mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
            if mousePos[0] > 300 and mousePos[0] < 347 and mousePos[1] > 270 and mousePos[1] < 345 and mouseDown == True:
                Counter += 1
        if event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False
        
        #keyboard input (more needed for actual game)
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_q:
                quitGame = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                quitGame = False
    #physics section-------------------------------------------------------

    if mapNum == 1:
        p1.move(keys, map)
    elif mapNum == 2:
        p1.move(keys , map2)
        
        
       

     #ANIMATION-------------------------------------------------------------------
     
    if state == 1 and mousePos[0]>400 and mousePos[0]<600 and mousePos[1]>400 and mousePos[1]<550:
        button1 = True
    else:
        button1 = False

    if state == 1 and button1 == True and mouseDown == True:
        state = 2

    if p1.xpos > 460 and p1.xpos < 510 and p1.ypos < 221:
        mapNum = 2
    
    if ticket == True and p1.xpos > 662 and p1.xpos < 713 and p1.ypos < 122:
        mapNum = 3
    
    if ticker % 40 == 0: #change this number to make him change direction less or more often
            num = random.randrange(0, 3)
            if num == 0:
                Green = True
            elif num == 1:
                Yellow = True
            elif num == 2:
                Red = True

    #if Green == True or Yellow == True:        
        #if p1.ypos - 20 < 800 and p1.ypos + 50 > 760 or p1.ypos - 20 < 605 and p1.ypos + 50 > 554 or p1.ypos - 20 < 400 and p1.ypos + 50 > 370:
            #print("hit")

    #print(Green) 
    #print(Yellow) 
    #print(Red) 
    C.move()
    #C.collision(p1.xpos - 30, p1.ypos - 20)
    #print(p1.xpos, p1.ypos)
   
    #render section-----------------------------------------------------------
    if state == 1:
        screen.fill((100,100,230))# Clear the screen pink

        if button1 == False:
            pygame.draw.rect(screen, (100, 230, 100), (400, 400, 200, 150))
        else:
            pygame.draw.rect(screen, (100, 250, 100), (400, 400, 200, 150))
        
        draw_text("Start", text_font, (0,0,0), 470, 460)
    
        
    
    if state == 2:
        screen.fill((128,128,128))

        if mapNum == 1:
            MapF(screen, map)

            draw_text("The Clock", text_font, (0,0,0), 445, 55)
            draw_text("Theater", text_font, (0,0,0), 455, 100)

            #for i in range(1000, 200):
            C.drawRR(screen)

            
            C.drawLB(screen)
            C.drawRR2(screen)

            p1.draw(screen)
        
        if mapNum == 2:
            MapF(screen, map2)

            draw_text("FNAF", text_font, (0,0,0), 660, 10)

            p1.draw(screen)

            screen.blit(worker, (300, 270, 200, 200))
            
            if Counter == 1:
                pygame.draw.rect(screen, (255, 255, 255), (100, 900, 800, 50))
                draw_text("Worker: Im guessing you're here for the fnaf movie?", text_font, (0,0,0), 200, 900)
            if Counter == 2:
                pygame.draw.rect(screen, (255, 255, 255), (100, 900, 800, 50))
                draw_text("You: Yep, I've been waiting for lieteral YEARS.", text_font, (0,0,0), 200, 900)
            if Counter == 3:
                pygame.draw.rect(screen, (255, 255, 255), (100, 900, 800, 50))
                draw_text("Worker: *This is like the 100th guy today.*", text_font, (0,0,0), 200, 900)
            if Counter == 4:
                pygame.draw.rect(screen, (255, 255, 255), (100, 900, 800, 50))
                draw_text("Worker: *If I need to deal with anymore of these geeks ima lose it.*", text_font, (0,0,0), 100, 900)
            if Counter == 5:
                pygame.draw.rect(screen, (255, 255, 255), (100, 900, 800, 50))
                draw_text("Worker: Here's your ticket nerd.", text_font, (0,0,0), 300, 900)
                ticket = True
            if Counter == 6:
                pygame.draw.rect(screen, (255, 255, 255), (100, 900, 800, 50))
                draw_text("You: Thank y-, wait what?", text_font, (0,0,0), 300, 900)
            if Counter == 7:
                pygame.draw.rect(screen, (255, 255, 255), (100, 900, 800, 50))
                draw_text("Worker: I said here's your ticket sir.", text_font, (0,0,0), 300, 900)
            if Counter == 8:
                pygame.draw.rect(screen, (255, 255, 255), (100, 900, 800, 50))
                draw_text("You: Oh, thank you", text_font, (0,0,0), 350, 900)
            if Counter == 9:
                pygame.draw.rect(screen, (255, 255, 255), (100, 900, 800, 50))
                draw_text("Worker: Your movie is in the room behind you", text_font, (0,0,0), 200, 900)
            if Counter == 10:
                pygame.draw.rect(screen, (255, 255, 255), (100, 900, 800, 50))
                draw_text("Worker: You already got your ticket", text_font, (0,0,0), 200, 900)
            

    pygame.display.flip()#this actually puts the pixel on the screen


#end game loop#############################################################################
pygame.quit()