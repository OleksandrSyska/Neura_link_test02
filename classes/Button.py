import pygame as g
class Button():
    def __init__(self,on_screen_position,titles,changable):
        self.CHANGABLE = changable
        self.titles = titles
        self.title = self.titles[0]
        self.state = 0
        self.padding = 20
        text_size = 36
        self.on_screen_position = on_screen_position
        self.font = g.font.SysFont("Roboto",text_size)
        textW,textH = self.font.size(self.title)
        width = textW + self.padding*2 
        height = textH + self.padding*2
        self.rect_position = (self.on_screen_position[0] - width, self.on_screen_position[1])

        self.surface = g.Surface((width,height))
        self.surface.fill((50,50,50))
        self.button_rect = g.Rect(
            self.rect_position[0],
            self.rect_position[1],
            width,
            height
        )
        self.surface.blit(self.font.render(self.title,1,(255,255,255)),(self.padding,self.padding))

    def draw(self,sc):
        sc.blit(self.surface,self.rect_position)

    def get_state(self):
        return self.state

    def change_text(self, text):
        self.title = text
        textW, textH = self.font.size(self.title)

        width = textW + self.padding * 2
        height = textH + self.padding * 2

        old_center = self.rect_position

        self.surface = g.Surface((width, height))
        self.surface.fill((50, 50, 50))

        self.button_rect = g.Rect(
            old_center[0],
            old_center[1],
            width,
            height
        )
        
        self.surface.blit(
            self.font.render(self.title, True, (255, 255, 255)),
            (self.padding, self.padding)
        )
        self.rect_position = (self.on_screen_position[0] - width, self.on_screen_position[1])
    
    def Fl_clicked(self,mouse_pos):
        if self.button_rect.collidepoint(mouse_pos):
            if self.state:
                self.state = 0
            else:
                self.state += 1
                
            if self.CHANGABLE:
                self.change_text(self.titles[self.state])
            return True
        else:
            return False