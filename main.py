import colors as c
import pygame as g
import random as r
import math as m
g.init()

SCW = 1900
SCH = 1000
speed_multiplier = 1.2
stop_multiplier = 0.5

speed_max = 7
angle_max = 5
gen_count = 1
d_angle = 0

count = 50

weight_range = 0.12
bias_range = 0.12

fl_forward = fl_right = fl_left = False
sc = g.display.set_mode((SCW, SCH))
#sc = g.display.set_mode((SCW, SCH), g.FULLSCREEN)

class Draha():
    def __init__(self):
        self.image = g.image.load('src\draha01.png').convert_alpha()
        self.rect = self.image.get_rect()

draha01 = Draha()

class NN():
    def __init__(self):
        self.original_image = g.image.load(f'src\\auto01.png').convert_alpha()
        self.original_image.set_colorkey(c.WHITE)
        self.image = self.original_image
        
        self.rect = self.image.get_rect()
        self.rect.center = (202, 490)
        self.speed = 0
        self.angle = 90



        # 120 weights + 21 biases 
        self.dnaW = []
        self.dnaB = []
        for _ in range(0,114):
            self.dnaW.append(
                round(
                    r.uniform(-weight_range,weight_range),
                    2
                )
            )

        for _ in range(0,20):
                    self.dnaB.append(
                        round(
                            r.uniform(-bias_range,bias_range),
                            2
                        )
                    )

    def predict(self,inputs):
        for i in range(len(inputs)):
            inputs[i] = inputs[i]//100
        cell_1 = 0
        cell_2 = 0
        cell_3 = 0
        cell_4 = 0
        cell_5 = 0
        cell_6 = 0
        cell_7 = 0
        cell_8 = 0
        cell_9 = 0
        cell_10 = 0
        cell_11 = 0
        cell_12 = 0
        cell_13 = 0
        cell_14 = 0
        cell_15 = 0
        cell_16 = 0
        cell_17 = 0
        cell_18 = 0
        cell_19 = 0

        #TODO LINE 1
        for i in range(0,5):
            cell_1 += inputs[i] * self.dnaW[i]
        for i in range(5,10):
            cell_2 += inputs[i-5] * self.dnaW[i]
        for i in range(10,15):
            cell_3 += inputs[i-10] * self.dnaW[i]
        for i in range(15,20):
            cell_4 += inputs[i-15] * self.dnaW[i]
        for i in range(20,25):
            cell_5 += inputs[i-20] * self.dnaW[i]
        for i in range(25,30):
            cell_6 += inputs[i-25] * self.dnaW[i]

        column1 = [
            cell_1 + self.dnaB[0],
            cell_2 + self.dnaB[1],
            cell_3 + self.dnaB[2],
            cell_4 + self.dnaB[3],
            cell_5 + self.dnaB[4],
            cell_6 + self.dnaB[5]
        ]

        #TODO LINE 3
        for i in range(0,6):
            cell_6 += column1[i] * self.dnaW[i+30]
        for i in range(6,12):
            cell_7 += column1[i-6] * self.dnaW[i+30]
        for i in range(12,18):
            cell_8 += column1[i-12] * self.dnaW[i+30]
        for i in range(18,24):
            cell_9 += column1[i-18] * self.dnaW[i+30]
        for i in range(24,30):
            cell_10 += column1[i-24] * self.dnaW[i+30]
        for i in range(30,36):
            cell_11 += column1[i-30] * self.dnaW[i+30]

        column2 = [
            cell_6 + self.dnaB[6],
            cell_7 + self.dnaB[7],
            cell_8 + self.dnaB[8],
            cell_9 + self.dnaB[9],
            cell_10 + self.dnaB[10],
            cell_11 + self.dnaB[11]
        ]
        #TODO LINE 3
        for i in range(0,6):
            cell_12 += column2[i] * self.dnaW[i+60]
        for i in range(6,12):
            cell_13 += column2[i-6] * self.dnaW[i+60]
        for i in range(12,18):
            cell_14 += column2[i-12] * self.dnaW[i+60]
        for i in range(18,24):
            cell_15 += column2[i-18] * self.dnaW[i+60]
        for i in range(24,30):
            cell_16 += column2[i-24] * self.dnaW[i+60]
        for i in range(30,36):
            cell_17 += column2[i-30] * self.dnaW[i+60]

        column3 = [
            cell_12 + self.dnaB[12],
            cell_13 + self.dnaB[13],
            cell_14 + self.dnaB[14],
            cell_15 + self.dnaB[15],
            cell_16 + self.dnaB[16],
            cell_17 + self.dnaB[17]
        ]
        #TODO LINE 4
        for i in range(0,6):
            cell_18 += column3[i] * self.dnaW[i+90]
        for i in range(6,12):
            cell_19 += column3[i-6] * self.dnaW[i+90]



        column4 = [
            (cell_18 + self.dnaB[18])*100,
            (cell_19 + self.dnaB[19])*100
        ]
        #speed,angle
#---------------------------------------------------------------------------------
        #print(column4[0])
        print(column4[1])
        if not self.speed + column4[0] > 0:
            self.speed = 0
        elif not self.speed + column4[0] <speed_max:
            self.speed = speed_max
        else:
            self.speed += column4[0]

        if -angle_max < self.angle + column4[1] < angle_max:
            self.angle += column4[1]
        # Rotate from the ORIGINAL image
        self.image = g.transform.rotate(
            self.original_image,
            self.angle
        )
        self.image.set_colorkey(c.WHITE)
        # Keep the car in the same position
        self.rect = self.image.get_rect(
            center=self.rect.center
        )
        self.rect.centerx += m.cos(m.radians(self.angle)) * self.speed
        self.rect.centery -= m.sin(m.radians(self.angle)) * self.speed

    def draw(self):
        self.angle

        # Rotate from the ORIGINAL image
        self.image = g.transform.rotate(
            self.original_image,
            self.angle
        )
        self.image.set_colorkey(c.WHITE)
        # Keep the car in the same position
        self.rect = self.image.get_rect(
            center=self.rect.center
        )
        self.rect.centerx += m.cos(m.radians(self.angle)) * self.speed
        self.rect.centery -= m.sin(m.radians(self.angle)) * self.speed

    def line(self):
        x = float(self.rect.centerx)
        y = float(self.rect.centery)
        distance_FW = 0
        for dis in range(300):
            x += m.cos(m.radians(self.angle))
            y -= m.sin(m.radians(self.angle))

            ix = int(x)
            iy = int(y)

            if ix < 0 or ix >= SCW or iy < 0 or iy >= SCH:
                distance_FW = dis
                break

            color = draha01.image.get_at((ix, iy))

            if color == c.BLACK:
                distance_FW = dis
                break
        g.draw.line(
            sc,
            c.RED,
            self.rect.center,
            (int(x), int(y))
        )
#---------------------------------------------------------------------------
        x = float(self.rect.centerx)
        y = float(self.rect.centery)
        distance_R = 0
        for dis in range(300):
            x += m.cos(m.radians(self.angle-90))
            y -= m.sin(m.radians(self.angle-90))

            ix = int(x)
            iy = int(y)

            if ix < 0 or ix >= SCW or iy < 0 or iy >= SCH:
                distance_R = dis
                break

            color = draha01.image.get_at((ix, iy))

            if color == c.BLACK:
                distance_R = dis
                break
        g.draw.line(
            sc,
            c.RED,
            self.rect.center,
            (int(x), int(y))
        )
#---------------------------------------------------------------------------
        x = float(self.rect.centerx)
        y = float(self.rect.centery)
        distance_L = 0
        for dis in range(300):
            x += m.cos(m.radians(self.angle+90))
            y -= m.sin(m.radians(self.angle+90))

            ix = int(x)
            iy = int(y)

            if ix < 0 or ix >= SCW or iy < 0 or iy >= SCH:
                distance_L = dis
                break

            color = draha01.image.get_at((ix, iy))

            if color == c.BLACK:
                distance_L = dis
                break
        g.draw.line(
            sc,
            c.RED,
            self.rect.center,
            (int(x), int(y))
        )
#---------------------------------------------------------------------------
        x = float(self.rect.centerx)
        y = float(self.rect.centery)
        distance_R45 = 0
        for dis in range(300):
            x += m.cos(m.radians(self.angle-45))
            y -= m.sin(m.radians(self.angle-45))

            ix = int(x)
            iy = int(y)

            if ix < 0 or ix >= SCW or iy < 0 or iy >= SCH:
                distance_R45 = dis
                break

            color = draha01.image.get_at((ix, iy))

            if color == c.BLACK:
                distance_R45 = dis
                break
        g.draw.line(
            sc,
            c.RED,
            self.rect.center,
            (int(x), int(y))
        )
#---------------------------------------------------------------------------
        x = float(self.rect.centerx)
        y = float(self.rect.centery)
        distance_L45 = 0
        for dis in range(300):
            x += m.cos(m.radians(self.angle+45))
            y -= m.sin(m.radians(self.angle+45))

            ix = int(x)
            iy = int(y)

            if ix < 0 or ix >= SCW or iy < 0 or iy >= SCH:
                distance_L45 = dis
                break

            color = draha01.image.get_at((ix, iy))

            if color == c.BLACK:
                distance_L45 = dis
                break
        g.draw.line(
            sc,
            c.RED,
            self.rect.center,
            (int(x), int(y))
        )
        return [distance_FW,distance_R,distance_L,distance_R45,distance_L45]

auta = []

for _ in range(count):
    auta.append(NN())




clock = g.time.Clock()


FPS = 60


print("curent gen: " + str(gen_count))

while 1:
    for event in g.event.get():

        if event.type == g.KEYDOWN:
            if event.key == g.K_ESCAPE:
                exit()
            if event.key == g.K_SPACE:
                pass

            if event.key == g.K_w:
                fl_forward = True
            if event.key == g.K_d:
                fl_right = True
            if event.key == g.K_a:
                fl_left = True

        if event.type == g.KEYUP:
            if event.key == g.K_w:
                fl_forward = False
            if event.key == g.K_d:
                fl_right = False
            if event.key == g.K_a:
                fl_left = False

    #### 

    sc.fill(c.BLACK)
    sc.blit(draha01.image,draha01.rect)
    for element in auta:
        sc.blit(element.image,element.rect)
        inputs = element.line()
        element.predict(inputs)

    d_angle = 0
    g.display.update()
    clock.tick(FPS)