import pygame
from pygame import mixer
from map import MapF
from Player import player

mixer.init()
pygame.init()
pygame.display.set_caption("top down grid map game")
screen = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()

p1 = player()

A = 0
D = 1
W = 2
S = 3
SPACE = 4
F = 5
keys = [False, False, False, False, False, False]

counter = 0


#game state variable
state = 1 #1 is menu, 2 is playing, 3 is credits
button1 = False

mxpos = 0
mypos = 0

mousePos = (mxpos, mypos)
mouseDown = False

ticker = 0

mapNum = 1

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

map2 = [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
       [2,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,2],
       [2,0,2,0,0,0,0,0,2,2,2,2,2,2,0,0,0,0,0,2],
       [2,0,2,0,0,0,0,0,2,2,2,2,2,2,0,0,0,0,0,2],
       [2,0,2,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,2,0,2,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,2,0,2,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,2],
       [2,0,0,0,0,0,2,0,0,0,0,2,2,2,0,0,0,0,0,2],
       [2,0,0,0,0,2,2,0,0,0,0,2,2,2,0,0,0,0,0,2],
       [2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
       [2,1,1,1,1,1,1,1,3,3,3,3,3,1,1,1,1,1,1,2]]


text_font = pygame.font.SysFont("Sans", 30, bold = True)

def draw_text(text, font, text_col, tx, ty):
    img = font.render(text, True, text_col)
    screen.blit(img, (tx, ty))

while 1: #GAME LOOP######################################################
    clock.tick(60) # fps
    ticker+=1
    #input section--------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
            
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                keys[SPACE] = True
                counter += 1
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
    #elif mapNum == 2:
        #p1.move(keys , map2)
        
        
       

     #ANIMATION-------------------------------------------------------------------
     
    if state == 1 and mousePos[0]>400 and mousePos[0]<600 and mousePos[1]>400 and mousePos[1]<550:
        button1 = True
    else:
        button1 = False

    if state == 1 and button1 == True and mouseDown == True:
        state = 2

    if p1.xpos > 460 and p1.xpos < 510 and p1.ypos < 221:
        mapNum = 2
    
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
        
            p1.draw(screen)
        
        if mapNum == 2:
            MapF(screen, map2)
            
    
    pygame.display.flip()#this actually puts the pixel on the screen


#end game loop#############################################################################
pygame.quit()