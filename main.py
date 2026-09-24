import colors as c
import pygame as g
import random as r
import math as m

g.init()
SCW = 1900
SCH = 1000

# CHANGEABLE OPTIONS # CHANGEABLE OPTIONS # CHANGEABLE OPTIONS #
fl_lines = 1
speed_multiplier = 1.2
stop_multiplier = 0.5
speed_max = 7
angle_max = 10
count = 50
weight_range = 0.12
bias_range = 0.12
weight_mutation_range = 0.15
bias_mutation_range = 0.15
max_wieght_mutation = 10 #72 # half
max_bias_mutation = 5 # half 
DNA_INSERT_B = [0.1, -0.11, -0.06, -0.07, -0.06, 0.11, -0.03, -0.11, -0.07, 0.12, 0.1, 0.1, 0.07, -0.11, 0.12, 0.01, 0.08, 0.04, 0.11, -0.04]
DNA_INSERT_W = [-0.08, -0.03, 0.11, 0.04, 0.01, 0.12, -0.06, -0.0, -0.07, 0.07, 0.03, 0.03, 0.09, -0.06, -0.1, 0.08, -0.02, -0.03, -0.12, -0.05,
                0.05, -0.11, -0.04, -0.01, 0.02, -0.05, 0.09, 0.07, -0.01, -0.02, 0.05, -0.07, 0.08, 0.07, -0.01, 0.02, 0.03, 0.01, 0.04, -0.01,
                -0.08, 0.06, -0.07, -0.03, -0.1, 0.03, -0.05, -0.01, 0.05, -0.11, -0.08, -0.11, -0.03, -0.1, -0.07, -0.04, -0.08, -0.07, 0.11,
                0.03, 0.02, 0.03, 0.08, -0.0, 0.01, 0.04, -0.03, 0.11, -0.09, 0.1, -0.02, 0.11, -0.07, 0.03, 0.09, -0.11, 0.09, -0.0, 0.07, -0.09,
                0.08, -0.07, 0.11, -0.08, 0.11, 0.06, -0.0, -0.1, 0.04, -0.07, -0.05, 0.09, 0.05, 0.09, -0.02, 0.05, -0.02, -0.03, -0.08, 0.09,
                -0.07, -0.0, 0.09, -0.04, 0.08, 0.09, 0.04, -0.04, 0.08, -0.0, -0.01, -0.09, -0.06, 0.04]
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
        self.image = g.image.load(f'src\\draha01.png').convert_alpha()
        self.image.set_colorkey(c.WHITE)
        self.rect = self.image.get_rect()
draha01 = Draha()

meters = [
    Fitness_meter((65, 434),90),
    Fitness_meter((90, 300),90),
    Fitness_meter((396, 71),0),
    Fitness_meter((500, 250),0),
    Fitness_meter((644, 303),0),
    Fitness_meter((755, 377),0)
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
    auta.append(NN(0,0))



clock = g.time.Clock()


FPS = 60



print("curent gen: " + str(gen_count))


background = g.Surface((SCW, SCH))
background.fill(c.LIGHT_BROWN)
for element in meters:
    background.blit(element.image,element.rect)
background.blit(draha01.image, draha01.rect)


while 1:
    for event in g.event.get():
        if event.type == g.KEYDOWN:
            if event.key == g.K_ESCAPE:
                exit()
            if event.key == g.K_SPACE:
                heighest_fitness = 0
                heighest_fitness_index = 0
                for auto in auta:
                    if auto.fitness > heighest_fitness:
                        heighest_fitness = auto.fitness
                        heighest_fitness_index = auta.index(auto)

                print(heighest_fitness)
                best_dnaW = auta[heighest_fitness_index].dnaW
                best_dnaB = auta[heighest_fitness_index].dnaB
                copy_auta = auta.copy()
                for i in copy_auta:
                    if i.fitness != heighest_fitness:
                        auta.remove(i)
                auta.clear()
                copy_auta.clear()
                for _ in range(count):
                    auta.append(NN(best_dnaW,best_dnaB))

                for auto in auta:
                    auto.mutate()
                print(len(auta))

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