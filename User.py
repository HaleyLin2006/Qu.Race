import pygame 
import sys
from Button import Button
from Gates import Q_Circuit

pygame.init()
size = width, height = 700, 480
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Qu.Race - A Quantum Race')

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
            socket.close()

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
        #1 Player
        Start_PvP = Button(650, 480, screen, "Play!", msg_size=40 ,width=40, height=20, bg_color=(53,96,179))
        Start_PvP.draw_button(screen)
        if Start_PvP.mouse_is_over and event.type == pygame.MOUSEBUTTONUP:
            states = "in_PvP"

    pygame.display.flip()

#1 Player Surface
while running and states == "in_PvP":
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #Gates Surface
        Gate_Surface_Color = (73, 65, 105)
        pygame.draw.rect(screen, Gate_Surface_Color, (0,290,700,480))

    pygame.display.update()

pygame.quit()