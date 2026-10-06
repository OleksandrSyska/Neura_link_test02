from colors import WHITE
from Math_Logic import Math_Logic as m
from pygame import transform as T
class Car():
    def __init__(self,image,speed_max,angle_max,NN):
        self.original_image = image 
        self.original_image.set_colorkey(WHITE)
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (202, 490)
        self.speed = 1
        self.angle = 90
        self.fl_stop = False
        self.speed_max = speed_max
        self.angle_max = angle_max
        self.NN = NN
        
    def move(self,data):
        speed = data[0]
        angle = data[1]
        if not self.fl_stop:
            if not self.speed + speed > 0:
                self.speed = 0
            elif not self.speed + speed <self.speed_max:
                self.speed = self.speed_max
            else:
                self.speed += speed

            if -self.angle_max < angle < self.angle_max:
                self.angle += angle
            # Rotate from the ORIGINAL image
            self.image = T.rotate(
                self.original_image,
                self.angle
            )
            self.image.set_colorkey(WHITE)
            # Keep the car in the same position
            self.rect = self.image.get_rect(
                center=self.rect.center
            )
            
            self.rect.centerx += m.calc_hor_vec(self.angle,self.speed)
            self.rect.centery += m.calc_ver_vec(self.angle,self.speed) 

    def get_image(self):
        return self.image
    def get_rect(self):
        return self.rect
    def stop(self):
        self.fl_stop = True