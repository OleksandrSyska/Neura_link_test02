from colors import WHITE
from pygame import Surface as SURF
class BG():
    def __init__(self,image,BG_color,SCW,SCH,meters):
        self.image = image 
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

        self.background = SURF((SCW, SCH))
        self.background.fill(BG_color)
        for element in meters:
            self.background.blit(element.image,element.rect)
        self.background.blit(self.image, self.rect)

    def get_image(self):
        return self.image
    def get_rect(self):
        return self.rect
    def draw(self):
        return self.background