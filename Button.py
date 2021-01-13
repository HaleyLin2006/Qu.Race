import pygame

pygame.init()

class Button():
    #Initialize
    def __init__ (self, left, top, screen, msg, bg_color=(0,0,0), msg_color=(250,250,250), msg_size=20, width=20, height=10):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = width, height
        self.bg_color = bg_color
        self.rect = pygame.Rect(left,top,width,height)
        self.rect.center = (left+width)//2, (top+height)//2
        self.deal_msg(msg,msg_size, msg_color,bg_color)
    
    #change msg --> img
    def deal_msg(self, msg, msg_size, msg_color, bg_color):
        text = pygame.font.Font("COOPBL.ttf", msg_size)
        self.msg_img = text.render(msg, True, msg_color, bg_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center
    
    def draw_button(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)

#Problem!!!! Not working
    def mouse_is_over(self):
        Mouse_x, Mouse_y = pygame.mouse.get_pos()
        x, y = self.rect.center
        #Half way distance of button
        edge_x, edge_y = (self.width//2), (self.height//2)
        #Mouse in the button --> Turn whiter
        if (x-edge_x < Mouse_x and x+edge_x > Mouse_x) and (y-edge_y < Mouse_y and y+edge_y > Mouse_y):
            Color_Code = [i for i in self.bg_color]
            self.bg_color = (Color_Code[0]+100, Color_Code[1]+100, Color_Code+100)
            return True
        else:
            return False
    
    def mouse_clicked(self):
        if self.mouse_is_over():
            pygame.event.get()
            if pygame.mouse.get_pressed():
                return True
        else:
            return False


