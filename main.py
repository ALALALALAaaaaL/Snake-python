import pygame
import sys
 
pygame.init()
 
display = pygame.display.set_mode((300, 300))
 

while True:
       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
               print("DAŁN")

            if event.key == pygame.K_UP:
               print("UP")

            if event.key == pygame.K_LEFT:
               print("LEFT")

            if event.key == pygame.K_RIGHT:
               print("RIGHT")