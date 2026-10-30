import pygame as g
class button():
    def __init__(self,screen_center_position,text):
        self.text = text
        self.screen_center_position = screen_center_position
        text_size = 36
        self.font = g.font.SysFont("Roboto",text_size)
        textW,textH = self.font.size(self.text)
        padding = 20
        width = textW + padding*2 
        height = textH + padding*2
        self.rect_center_position = (self.screen_center_position[0] - width, self.screen_center_position[1])

        self.surface = g.Surface((width,height))
        self.surface.fill((50,50,50))
        self.button_rect = g.Rect(
            self.rect_center_position[0],
            self.rect_center_position[1],
            width,
            height
        )
        self.surface.blit(self.font.render(self.text,1,(255,255,255)),(padding,padding))

    def Fl_clicked(self,mouse_pos):
        if self.button_rect.collidepoint(mouse_pos):
            return True
        else:
            return False

    def draw(self,sc):
        sc.blit(self.surface,self.rect_center_position)
    '''
    def change_text(self,text):
        self.text = text
        text_size = 36
        self.font = g.font.SysFont("Roboto",text_size)
    '''
    def change_text(self, text):
        self.text = text

        padding = 20
        textW, textH = self.font.size(self.text)

        width = textW + padding * 2
        height = textH + padding * 2

        # Zachováme původní pozici tlačítka
        old_center = self.rect_center_position

        self.surface = g.Surface((width, height))
        self.surface.fill((50, 50, 50))

        self.button_rect = g.Rect(
            old_center[0],
            old_center[1],
            width,
            height
        )

        self.surface.blit(
            self.font.render(self.text, True, (255, 255, 255)),
            (padding, padding)
        )
        self.rect_center_position = (self.screen_center_position[0] - width, self.screen_center_position[1])