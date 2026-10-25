from pygame import transform as t
class Fitness_meter():
    def __init__(self,image,cordinates,rotation):
        self.original_image = image 
        self.image = self.original_image
        self.image = t.rotate(self.image,rotation)
        self.rect = self.image.get_rect()
        self.rect.center = cordinates
    def collide_check(self,car_rect):
        return self.rect.colliderect(car_rect)
    def get_center(self):
        return self.rect.center
    def get_rect(self):
        return self.rect