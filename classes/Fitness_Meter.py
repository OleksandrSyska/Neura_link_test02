from pygame import transform as t
class Fitness_meter():
    def __init__(self,image,cordinates,rotation):
        self.original_image = image 
        self.image = self.original_image
        self.image = t.rotate(self.image,rotation)
        self.rect = self.image.get_rect()
        self.rect.center = cordinates
    def collide_Q(self):
            pass
            '''
            if self.rect.colliderect(fit):
            if not fit in self.fitnesses:
            self.fitnesses.append(fit)
            self.fitness += 1 
            '''
    def get_center(self):
        return self.rect.center
    def get_rect(self):
        return self.rect