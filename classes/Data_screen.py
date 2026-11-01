import pygame as g
class Data_screen():
    def __init__(self,on_screen_position,text_and_size):
        self.padding = 20
        self.on_screen_position = on_screen_position
        self.fonts = []
        for element in text_and_size:
            self.fonts.append(g.font.SysFont("Roboto",element[1]))
        text_sizes = []
        for element,font in zip(text_and_size,self.fonts):
            text_sizes.append(font.size(element[0]))

        self.width = 0
        self.height = self.padding 
        longest_word = 0
        for element in text_sizes:
            self.height += element[1] + self.padding
            if longest_word <= element[0]:
                longest_word = element[0]
        self.width = longest_word + self.padding*2
        self.rect_position = (
                    self.on_screen_position[0] - self.width,
                    self.on_screen_position[1]
                    )

        self.surface = g.Surface((self.width,self.height))
        self.surface.fill((50,50,50))
        dy = self.padding
        for i, (element, font) in enumerate(zip(text_and_size, self.fonts)):
            self.surface.blit(
                font.render(element[0], True, (255,255,255)),
                (self.padding, dy)
            )
            dy += self.padding + text_sizes[i][1]

    
    
    def draw(self,sc):
        sc.blit(self.surface,self.rect_position)

    def update(self,text_and_size):
        self.fonts = []
        for element in text_and_size:
            self.fonts.append(g.font.SysFont("Roboto",element[1]))
        text_sizes = []
        for element,font in zip(text_and_size,self.fonts):
            text_sizes.append(font.size(element[0]))

        self.width = 0
        self.height = self.padding
        longest_word = 0
        for element in text_sizes:
            self.height += element[1] + self.padding
            if longest_word <= element[0]:
                longest_word = element[0]
        self.width = longest_word + self.padding*2
        self.rect_position = (
                    self.on_screen_position[0] - self.width,
                    self.on_screen_position[1]
                    )

        self.surface = g.Surface((self.width,self.height))
        self.surface.fill((50,50,50))
        dy = self.padding
        for i, (element, font) in enumerate(zip(text_and_size, self.fonts)):
            self.surface.blit(
                font.render(element[0], True, (255,255,255)),
                (self.padding, dy)
            )
            dy += self.padding + text_sizes[i][1]