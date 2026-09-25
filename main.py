import colors as c
import pygame as g
import random as r
import math as m

g.init()
SCW = 1900
SCH = 1000
mutation_clock = g.USEREVENT + 1
g.time.set_timer(mutation_clock,0000)
# CHANGEABLE OPTIONS # CHANGEABLE OPTIONS # CHANGEABLE OPTIONS #
fl_lines = 0
speed_multiplier = 1.2
stop_multiplier = 0.5
speed_max = 7
angle_max = 10
count = 100
weight_range = 0.12
bias_range = 0.12
weight_mutation_range = 0.2#0.15
bias_mutation_range = 0.2#0.15

max_wieght_mutation = 10 #72 # half
max_bias_mutation = 5 # half 

DNA_INSERT_B = 0
DNA_INSERT_W = 0

circle = [
    [0.23, -0.09, 0.01, -0.10999999999999999, 0.06, -0.05, 0.12, 0.03, -0.020000000000000004, -0.21000000000000002, 0.09, -0.03, -0.06, 0.1, 0.03, -0.16999999999999998, 0.07, 0.04, 0.1, -0.11],
    [0.07, 0.0, -0.08, -0.11, -0.03, 0.08, -0.12, 0.01, -0.07, 0.05, 0.09, -0.08, -0.04, 0.01, -0.09, -0.01, 0.05, 0.0, -0.05, -0.12, 0.0, -0.1, 0.03, -0.04, 0.03999999999999999, -0.12, 0.05, 0.01, 0.02, -0.11, -0.11, 0.11, 0.06, 0.11, -0.06, 0.03, -0.02, -0.18, 0.11, 0.06, -0.09, -0.11, -0.1, 0.01, 0.05, 0.04, 0.03, 0.05, -0.05, 0.05, 0.08, 0.07, 0.05, 0.03, 0.08, 0.02, 0.12, -0.09, -0.07, -0.01, -0.08, -0.1, 0.11, -0.07, -0.01, -0.1, 0.09, -0.1, 0.0, -0.11, -0.06, 0.09, -0.08, 0.08, -0.0, -0.11, -0.08, 0.03, 0.05, 0.09999999999999999, 0.01, 0.21000000000000002, -0.01, -0.030000000000000002, 0.03, 0.04, -0.09, -0.11, -0.13, -0.1, 0.05, -0.08, 0.04, 0.1, 0.09, -0.08, -0.02, 0.08, 0.07, 0.04, 0.08, -0.11, -0.11, -0.020000000000000004, 0.08, 0.1, -0.01, -0.06, 0.05, 0.05, 0.08, -0.1, -0.06, -0.06] 
]
good = [
    [0.06, -0.09000000000000001, 0.38, -0.01999999999999999, -0.39, 0.31999999999999995, -0.01, 0.15000000000000002, -0.06000000000000001, -0.15, -0.15999999999999998, 0.18, -0.26, -0.09, 0.09999999999999999, 0.17, -0.03, -0.07, -0.03, -0.21000000000000002, 0.11, -0.58, -0.06, 0.05, -0.04, 0.06000000000000001, -0.04, -0.04000000000000001, 0.41000000000000003, 0.020000000000000018, 0.10999999999999999, -0.04999999999999999, -0.19, -0.09, 0.09999999999999999, 0.16000000000000003, 0.2, 0.1, -0.06, -0.04000000000000001, 0.08000000000000002, 0.07, -0.01, 0.13, 0.22000000000000003, -0.23, 0.08, 0.29000000000000004, -0.13, -0.0, 0.11, 0.06, 0.25, -0.25, -0.29000000000000004, -0.07, -0.11, 0.48000000000000004, -0.48, -0.020000000000000004, -0.16999999999999998, -0.08000000000000002, 0.26, 0.06, 0.09000000000000001, -0.06, -0.12000000000000001, -0.09, 0.0, -0.17, -0.21999999999999997, 0.06, 0.039999999999999994, -0.18, -0.21000000000000002, -0.25, -0.21000000000000002, 0.25, 0.07999999999999999, 0.15000000000000002, -0.11, -0.18, 6.938893903907228e-18, -0.19999999999999998, -0.09999999999999999, -0.17, 0.26, -0.27, -0.07000000000000002, 0.15000000000000002, 0.36, -0.03, 0.24000000000000002, 0.0, 0.1, -0.09, 0.1, 0.04, 0.05, -0.2, -0.07, -0.05, -0.009999999999999995, 0.23, 0.32, -0.01, 0.04000000000000001, -0.4, -0.38, 0.12000000000000001, -0.11, 0.28, -0.1, -0.07] ,
    [-0.04000000000000001, -0.09000000000000002, 0.33, 0.020000000000000004, -0.029999999999999992, 0.0, 0.10000000000000002, 0.21000000000000002, -0.01, -0.22999999999999998, -0.040000000000000036, 0.15, -0.020000000000000004, -0.13, 0.09, -0.1, 0.15000000000000002, 0.05, 0.07, 0.0]
]
all = [
    [-0.04000000000000001, -0.26, 0.38, -0.01999999999999999, -0.5800000000000001, 0.13999999999999996, 0.16999999999999998, 0.15000000000000002, -0.06000000000000001, -0.28, -0.15999999999999998, 0.18, -0.4, -0.09, 0.09999999999999999, 0.17, -0.03, -0.07, -0.03, -0.09000000000000002, 0.11, -0.41999999999999993, -0.06, -0.09000000000000001, -0.04, 0.06000000000000001, -0.04, -0.04000000000000001, 0.56, 0.020000000000000018, 0.10999999999999999, -0.04999999999999999, -0.28, -0.08, 0.09999999999999999, 0.16000000000000003, 0.2, 0.11000000000000004, 0.07, -0.24, 0.08000000000000002, -0.03, -0.01, 0.08, 0.22000000000000003, -0.11000000000000001, -0.029999999999999992, 0.29000000000000004, -0.13, -0.0, -0.05, 0.04999999999999999, 0.25, -0.25, -0.16000000000000003, -0.07, -0.29, 0.48000000000000004, -0.48, 0.11, -0.24, -0.21000000000000002, 0.23, 0.06, 0.1, -0.06, -0.06000000000000001, -0.07, 0.0, -0.17, -0.10999999999999997, 0.06, 0.12, -0.49, -0.21000000000000002, -0.25, -0.17, 0.25, 0.07999999999999999, 0.15000000000000002, -0.09, -0.35, -0.17, -0.19999999999999998, -0.09999999999999999, -0.17, 0.26, -0.27, -0.05000000000000002, 0.14000000000000004, 0.36, -0.16, 0.24000000000000002, -0.09, 0.1, -0.03, 0.1, 0.09, 0.05, -0.2, -0.07, -0.05, -0.15, 0.23, 0.32, -0.06999999999999999, -0.13999999999999999, -0.27, -0.45, 0.12000000000000001, -0.11, 0.36000000000000004, -0.11, -0.07],
    [-0.04000000000000001, 0.33999999999999997, 0.4, 0.020000000000000004, -0.13, -0.02, 0.24, 0.22, 1.3877787807814457e-17, -0.22, 0.04999999999999997, 0.15, 0.0, -0.15000000000000002, 0.2, -0.26, 0.27, 0.13999999999999999, 0.07, 0.0]
]
dif_map = [
    [-0.04000000000000001, -0.26, 0.26, -0.01999999999999999, -0.5800000000000001, 0.13999999999999996, 0.16999999999999998, 0.15000000000000002, -0.06000000000000001, -0.28, -0.15999999999999998, 0.18, -0.55, -0.09, 0.09999999999999999, 0.17, -0.03, -0.07, -0.03, -0.09000000000000002, 0.11, -0.41999999999999993, -0.06, -0.09000000000000001, -0.04, 0.06000000000000001, -0.04, -0.04000000000000001, 0.56, 0.020000000000000018, 0.10999999999999999, -0.04999999999999999, -0.28, -0.08, 0.09999999999999999, 0.16000000000000003, 0.24000000000000002, 0.18000000000000005, 0.07, -0.24, -0.029999999999999985, -0.03, -0.01, 0.08, 0.22000000000000003, -0.11000000000000001, -0.029999999999999992, 0.29000000000000004, -0.24, -0.0, -0.05, 0.04999999999999999, 0.25, -0.25, -0.16000000000000003, -0.07, -0.44999999999999996, 0.48000000000000004, -0.48, 0.11, -0.15999999999999998, -0.21000000000000002, 0.32, 0.06, 0.1, -0.039999999999999994, -0.06000000000000001, -0.07, 0.0, -0.17, -0.10999999999999997, 0.06, 0.12, -0.49, -0.21000000000000002, -0.25, -0.17, 0.25, 0.07999999999999999, 0.15000000000000002, -0.09, -0.35, -0.17, -0.19999999999999998, -0.09999999999999999, -0.17, 0.26, -0.27, -0.05000000000000002, 0.020000000000000046, 0.36, -0.16, 0.33, -0.09, 0.1, -0.03, 0.1, 0.09, 0.020000000000000004, -0.2, -0.07, -0.12000000000000001, 0.0, 0.23, 0.32, -0.06999999999999999, -0.13999999999999999, -0.27, -0.45, 0.12000000000000001, -0.11, 0.4600000000000001, -0.11, -0.07],
    [-0.12000000000000001, 0.5, 0.45, 0.020000000000000004, -0.13, -0.02, 0.24, 0.31, 0.040000000000000015, -0.22, 0.04999999999999997, 0.12, 0.0, -0.010000000000000009, 0.2, -0.26, 0.27, 0.13999999999999999, 0.07, 0.0]
]
DNA_INSERT_B = dif_map[1]
DNA_INSERT_W = dif_map[0]
# CHANGEABLE OPTIONS # CHANGEABLE OPTIONS # CHANGEABLE OPTIONS #

gen_count = 1




fl_forward = fl_right = fl_left = fl_left = False
sc = g.display.set_mode((SCW, SCH))
#sc = g.display.set_mode((SCW, SCH), g.FULLSCREEN)
class Fitness_meter:
    def __init__(self,cor,rotation):
        self.original_image = g.image.load(f'src\\Fitness_meter.png').convert_alpha()
        self.image = self.original_image
        self.image = g.transform.rotate(self.image,rotation)
        self.rect = self.image.get_rect()
        self.rect.center = cor



class Draha():
    def __init__(self):
        self.image = g.image.load(f'src\\draha02.png').convert_alpha()
        self.image.set_colorkey(c.WHITE)
        self.rect = self.image.get_rect()
draha01 = Draha()

meters = [
    Fitness_meter((65, 434),90),
    Fitness_meter((90, 300),90),
    Fitness_meter((396, 71),0),
    Fitness_meter((500, 250),0),
    Fitness_meter((575, 550),0),
    Fitness_meter((644, 303),0),
    Fitness_meter((755, 377),0),
    Fitness_meter((800, 377),0),
    Fitness_meter((855, 377),0),
    Fitness_meter((1077, 700),0),
    Fitness_meter((1000, 1170),0),
    Fitness_meter((1300, 800),0),
    Fitness_meter((855, 800),0),
    Fitness_meter((65, 600),90),


]


class NN():
    def __init__(self,dna_injection_W,dna_injection_B):
        self.original_image = g.image.load(f'src\\auto01.png').convert_alpha()
        self.original_image.set_colorkey(c.WHITE)
        self.image = self.original_image
        self.rect = self.image.get_rect()

        self.fitnesses = []
        self.fitness = 0
        self.rect.center = (202, 490)
        self.speed = 1
        self.angle = 90
        self.stop = False

        self.dnaW = []
        self.dnaB = []
        
        if dna_injection_W:
            self.dnaW = list(dna_injection_W)
            self.dnaB = list(dna_injection_B)
        else:
            # 114 weights + 21 biases 
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
        cell_20 = 0

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
            cell_7 += column1[i] * self.dnaW[i+30]
        for i in range(6,12):
            cell_8 += column1[i-6] * self.dnaW[i+30]
        for i in range(12,18):
            cell_9 += column1[i-12] * self.dnaW[i+30]
        for i in range(18,24):
            cell_10 += column1[i-18] * self.dnaW[i+30]
        for i in range(24,30):
            cell_11 += column1[i-24] * self.dnaW[i+30]
        for i in range(30,36):
            cell_12 += column1[i-30] * self.dnaW[i+30]

        column2 = [
            cell_7 + self.dnaB[6],
            cell_8 + self.dnaB[7],
            cell_9 + self.dnaB[8],
            cell_10 + self.dnaB[9],
            cell_11 + self.dnaB[10],
            cell_12 + self.dnaB[11]
        ]
        #TODO LINE 3
        for i in range(0,6):
            cell_13 += column2[i] * self.dnaW[i+60]
        for i in range(6,12):
            cell_14 += column2[i-6] * self.dnaW[i+60]
        for i in range(12,18):
            cell_15 += column2[i-12] * self.dnaW[i+60]
        for i in range(18,24):
            cell_16 += column2[i-18] * self.dnaW[i+60]
        for i in range(24,30):
            cell_17 += column2[i-24] * self.dnaW[i+60]
        for i in range(30,36):
            cell_18 += column2[i-30] * self.dnaW[i+60]

        column3 = [
            cell_13 + self.dnaB[12],
            cell_14 + self.dnaB[13],
            cell_15 + self.dnaB[14],
            cell_16 + self.dnaB[15],
            cell_17 + self.dnaB[16],
            cell_18 + self.dnaB[17]
        ]
        #TODO LINE 4
        for i in range(0,6):
            cell_19 += column3[i] * self.dnaW[i+90]
        for i in range(6,12):
            cell_20 += column3[i-6] * self.dnaW[i+90]



        column4 = [
            (cell_19 + self.dnaB[18])*100,
            (cell_20 + self.dnaB[19])*100
        ]
        #speed,angle
#---------------------------------------------------------------------------------
        
        if not self.stop:
            #print(column4[0])
            #print(column4[1])
            if not self.speed + column4[0] > 0:
                self.speed = 0
            elif not self.speed + column4[0] <speed_max:
                self.speed = speed_max
            else:
                self.speed += column4[0]

            if -angle_max < column4[1] < angle_max:
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

            if color == c.BLACK or color == c.DARK_GREEN:
                distance_FW = dis
                break
        if not distance_FW:
            distance_FW = dis
        if fl_lines:
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

            if color == c.BLACK or color == c.DARK_GREEN:
                distance_R = dis
                break
        if not distance_R:
            distance_R = dis
        if fl_lines:
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

            if color == c.BLACK or color == c.DARK_GREEN:
                distance_L = dis
                break
        if not distance_L:
            distance_L = dis
        if fl_lines:
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

            if color == c.BLACK or color == c.DARK_GREEN:
                distance_R45 = dis
                break
        if not distance_R45:
            distance_R45 = dis
        if fl_lines:
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

            if color == c.BLACK or color == c.DARK_GREEN:
                distance_L45 = dis
                break
        if not distance_L45:
            distance_L45 = dis
        if fl_lines:
            g.draw.line(
                sc,
                c.RED,
                self.rect.center,
                (int(x), int(y))
            )

        if not (distance_FW and distance_R and distance_L and distance_R45 and distance_L45):
            self.stop = True
        return [distance_FW,distance_R,distance_L,distance_R45,distance_L45]

    def add_fitness(self,fit):
        if self.rect.colliderect(fit):
            if not fit in self.fitnesses:
                self.fitnesses.append(fit)
                self.fitness += 1 

    def mutate(self):
        already_mutated_index_W = []
        already_mutated_index_B = []
        for _ in range(r.randint(1,max_wieght_mutation)):
            chosen_index = r.randint(0,len(self.dnaW)-1)
            while chosen_index in already_mutated_index_W:
                chosen_index = r.randint(0,len(self.dnaW)-1)
            already_mutated_index_W.append(chosen_index)
            self.dnaW[chosen_index] += round(r.uniform(-weight_mutation_range,weight_mutation_range),2)



        for _ in range(r.randint(1,max_bias_mutation)):
            chosen_index = r.randint(0,len(self.dnaB)-1)
            while chosen_index in already_mutated_index_B:
                chosen_index = r.randint(0,len(self.dnaB)-1)
            already_mutated_index_B.append(chosen_index)
            self.dnaB[chosen_index] += round(r.uniform(-bias_mutation_range,bias_mutation_range),2)

auta = []

for _ in range(count):
    auta.append(NN(DNA_INSERT_W,DNA_INSERT_B))



clock = g.time.Clock()


FPS = 60



print("curent gen: " + str(gen_count))


background = g.Surface((SCW, SCH))
background.fill(c.LIGHT_BROWN)
for element in meters:
    background.blit(element.image,element.rect)
background.blit(draha01.image, draha01.rect)
clock
while 1:
    for event in g.event.get():
        if event.type == mutation_clock:
            gen_count +=1
            print("curent gen: " + str(gen_count))
            heighest_fitness = 0
            heighest_fitness_index = 0
            for auto in auta:
                if auto.fitness > heighest_fitness:
                    heighest_fitness = auto.fitness
                    heighest_fitness_index = auta.index(auto)


            best_dnaW = auta[heighest_fitness_index].dnaW
            best_dnaB = auta[heighest_fitness_index].dnaB
            auta.clear()
            for _ in range(count):
                auta.append(NN(best_dnaW,best_dnaB))

            for auto in auta:
                auto.mutate()
        if event.type == g.KEYDOWN:
            if event.key == g.K_ESCAPE:
                exit()
            if event.key == g.K_SPACE:
                g.time.set_timer(mutation_clock,0)
                copy_auta = auta.copy()
                for i in copy_auta:
                    if i.fitness != heighest_fitness:
                        auta.remove(i)
                copy_auta.clear()
                for i in auta:
                    print("START START START START START START START START START START START START START START START START ")
                    print(i.dnaW,i.dnaB)
                    print("STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP ")
            if event.key == g.K_w:
                gen_count +=1
                print("curent gen: " + str(gen_count))
                heighest_fitness = 0
                heighest_fitness_index = 0
                for auto in auta:
                    if auto.fitness > heighest_fitness:
                        heighest_fitness = auto.fitness
                        heighest_fitness_index = auta.index(auto)
    
    
                best_dnaW = auta[heighest_fitness_index].dnaW
                best_dnaB = auta[heighest_fitness_index].dnaB
                auta.clear()
                for _ in range(count):
                    auta.append(NN(best_dnaW,best_dnaB))
    
                for auto in auta:
                                auto.mutate()


    '''
            if event.key == g.K_w:
                fl_forward = True
            if event.key == g.K_d:
                fl_right = True
            if event.key == g.K_a:
                fl_left = True
            if event.key == g.K_s:
                fl_left = True
        if event.type == g.KEYUP:
            if event.key == g.K_w:
                fl_forward = False
            if event.key == g.K_d:
                fl_right = False
            if event.key == g.K_a:
                fl_left = False
            if event.key == g.K_s:
                fl_left = False
    '''

#----------------------------------------------------------------------
    sc.blit(background,(0,0))
    for element in auta:
        sc.blit(element.image,element.rect)
        inputs = element.line()
        element.predict(inputs)

        for element2 in meters:
            element.add_fitness(element2)
    g.display.update()
    clock.tick(FPS)