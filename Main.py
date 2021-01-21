import pygame 
import sys
from Button import Button
from Gates import Q_Circuit, Gates
import random

pygame.init()
size = width, height = 700, 480
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Qu.Race - A Quantum Game')

#UI
#BG
UI_bg = pygame.image.load('background-2426328.jpg')
UI_bg = pygame.transform.scale(UI_bg, size)
#icon
UI_icon = pygame.image.load('icon.jpg')

#UI Surface
running = True
states = "in_UI"
while running and states == "in_UI": 
    for event in pygame.event.get():
        #close window
        if event.type == pygame.QUIT:
            sys.exit()

        #Generalize
        #icon
        pygame.display.set_icon(UI_icon)
        #BG
        screen.blit(UI_bg, (0,0))
        #Title(replace by picture)   
        Title_Size = 70
        Title_Font = pygame.font.Font("COOPBL.ttf", Title_Size)
        Title_Surface = Title_Font.render("Qu.Race", True, (18,85,219))
        screen.blit(Title_Surface, (210,90))

        #Start Buttons
        #1 Computer
        Start_PvP = Button(650, 480, screen, "Play!", msg_size=40 ,width=45, height=20, bg_color=(53,96,179))
        Start_PvP.draw_button()
        if event.type == pygame.MOUSEBUTTONDOWN and Start_PvP.mouse_is_over():
            states = "in_PvP"

    pygame.display.flip()

#1 Computer Surface
while running and states == "in_PvP":
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #BG
        screen.fill((255,255,255))
        #Game Surface
        #Make Circuit
        qubit = 5
        PvP_Circuit = Q_Circuit()
        PvP_Circuit.start(qubit)
        display_area_height = 390
        gap = 230//qubit
        Qubit_Font = pygame.font.Font("COOPBL.ttf", 30)
        #Make game surface
        for i in range(qubit):
            y = (i+1)*gap
            Qubit_Name = "q"+str(i)
            Qubit_Font_Surface = Qubit_Font.render(Qubit_Name, True, (0,0,0))
            screen.blit(Qubit_Font_Surface, (10,y))
            pygame.draw.line(screen,(0,0,0),(25,y),(650,y),5)

        #Gates Surface
        Gate_Surface_Color = (73, 65, 105)
        pygame.draw.rect(screen, Gate_Surface_Color, (0,290,700,480))
        
        #Gates
        if event.type == pygame.MOUSEBUTTONDOWN:
            Mouse_Press = True
        else:
            Mouse_Press = False
        H = Gates(screen, 30, 295, "H", Mouse_Press)
        H.draw()
        H.update()
        


    pygame.display.flip()

pygame.quit()