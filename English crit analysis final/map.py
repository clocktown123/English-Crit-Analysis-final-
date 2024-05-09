import pygame

brick = pygame.image.load('brick.png')
tree = pygame.image.load('tree.png')
street = pygame.image.load('street.png')
sign = pygame.image.load('Signs.png')
door = pygame.image.load('glass_door.png')
table = pygame.image.load('table.png')
table2 = pygame.image.load('table_5.png')
poster = pygame.image.load('fnaf_poster.png')

def MapF (screen, map):
    for i in range(20):
                for j in range(20):
                    if map[i][j] == 1:
                        screen.blit(tree, (j*50, i * 50), (0, 0, 50, 50))
                    if map[i][j] == 2:
                        screen.blit(brick, (j *50, i * 50), (0, 0, 50, 50))
                    if map[i][j] == 3:
                        screen.blit(sign, (j *50, i * 50), (0, 0, 50, 50))
                    if map[i][j] == 4:
                        screen.blit(door, (j *50, i * 50), (0, 0, 50, 50))
                    if map[i][j] == 5:
                        screen.blit(street, (j *50, i * 50), (0, 0, 50, 50))
                    if map[i][j] == 6:
                        screen.blit(table, (j *50, i * 50), (0, 0, 50, 50))
                    if map[i][j] == 7:
                        screen.blit(table2, (j *50, i * 50), (0, 0, 50, 50))
                    if map[i][j] == 8:
                         screen.blit(poster, (j*50, i*50), (0,0,50,50))