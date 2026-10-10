import pygame as g
class Button():
    def __init__(self,image):
        self.image = image
        self.rect = self.image.get_rect()
    def Fl_clicked(self,mouse):
        if self.rect.collidepoint(mouse):
            return True
        else:
            return False
    def get_image(self):
        return self.image
    def get_rect(self):
        return self.rect