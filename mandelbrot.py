from math import *
from time import sleep

import pygame
pygame.init()

screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)


zoom = 50
# 5, 5, -5, -5
# 
limite_plan = (-2,-1, 3,3)
# limite_plan =(0.3127572016460905, 0.03292181069958847, 0.004115226337448559, 0.004115226337448559)
nbr_iterations = 150

running = True
while running:
    
    pygame.draw.rect(screen, (0,0,0), [0,0,screen.get_width(), screen.get_height()])
    
    for x in range(screen.get_width()):
        for y in range(screen.get_height()):
            y_2 = 500-y
            
            x_nbr = limite_plan[0] + x*(limite_plan[2]/500)
            """
            if limite_plan[1]<0 :
                y_nbr = limite_plan[1] + y_2*(limite_plan[3]/500)
            else :-limite_plan[1] + y*(limite_plan[3]/500)"""
            y_nbr = limite_plan[1] + y_2*(limite_plan[3]/500)
            c = complex(x_nbr,y_nbr)
            # if x==0 and y==0 : print(c, x, y)
            
            z = complex(0,0)
            
            for i in range(nbr_iterations):
                z = (z*z)+c
                
            # print(z, c)
            
            if -5<z.real<5 and -5<z.imag<5 :
                pygame.draw.rect(screen, (255,0,255), [x, y, 1, 1])
            else : pass #pygame.draw.rect(screen, (nbr_iterations*2,0,0), [x, y, 1, 1])
            if c==complex(0,0) :
                print("okay")
                pygame.draw.rect(screen, (255,255,0), [x-5, y-5, 5, 5])
        pygame.display.flip()
        
    # nbr_iterations += 5
        
    
    # dessine le cadrant
    pygame.draw.rect(screen, (255,255,255), (screen.get_width()/3, screen.get_height()/3, screen.get_width()/3, 1))
    pygame.draw.rect(screen, (255,255,255), (screen.get_width()/3, 2*screen.get_height()/3-1, screen.get_width()/3, 1))
    pygame.draw.rect(screen, (255,255,255), (screen.get_width()/3, screen.get_height()/3, 1, screen.get_height()/3))
    pygame.draw.rect(screen, (255,255,255), (2*screen.get_width()/3-1, screen.get_height()/3, 1, screen.get_height()/3+1))
    pygame.display.flip()
    
    
    case = int(input('deplacement suivant : - '))
    if case == '0' : exit()
    elif case == '' : pass
    elif case == 5 :
        limite_plan = (limite_plan[0]+(1/3)*limite_plan[2],
               limite_plan[1]+(1/3)*limite_plan[3],
               limite_plan[2]/3,
               limite_plan[3]/3)
        print(limite_plan)
    elif case == 8 :
        limite_plan = (limite_plan[0]+(1/3)*limite_plan[2],
               limite_plan[1]+(2/3)*limite_plan[3],
               limite_plan[2]/3,
               limite_plan[3]/3)
        print(limite_plan)
    elif case == 9 :
        limite_plan = (limite_plan[0]+(2/3)*limite_plan[2],
                       limite_plan[1]+(2/3)*limite_plan[3],
                       limite_plan[2]/3,
                       limite_plan[3]/3)
        print(limite_plan)
    elif case == 6 :
        limite_plan = (limite_plan[0]+(2/3)*limite_plan[2],
                       limite_plan[1]+(1/3)*limite_plan[3],
                       limite_plan[2]/3,
                       limite_plan[3]/3)
        print(limite_plan)
    elif case == 7 :
        limite_plan = (limite_plan[0],
                       limite_plan[1]+(2/3)*limite_plan[3],
                       limite_plan[2]/3,
                       limite_plan[3]/3)
        print(limite_plan)
    elif case == 3 :
        limite_plan = (limite_plan[0]+(2/3)*limite_plan[2],
                       limite_plan[1],
                       limite_plan[2]/3,
                       limite_plan[3]/3)
        print(limite_plan)
    elif case == 4 :
        limite_plan = (limite_plan[0],
                       limite_plan[1]+(1/3)*limite_plan[3],
                       limite_plan[2]/3,
                       limite_plan[3]/3)
        print(limite_plan)
    elif case == 2 :
        limite_plan = (limite_plan[0]+(1/3)*limite_plan[2],
                       limite_plan[1],
                       limite_plan[2]/3,
                       limite_plan[3]/3)
        print(limite_plan)
    elif case == 1 :
        limite_plan = (limite_plan[0],
                       limite_plan[1],
                       limite_plan[2]/3,
                       limite_plan[3]/3)
        print(limite_plan)
    
    
            
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()