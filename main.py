import colors as c
import pygame as g
import random as r
import math as m


from Neural_Sytem2 import NN
from Back_Ground import BG
from Car import Car
from Eyes import Eyes
from Fitness_Meter import Fitness_meter
from Fitness_Cotroler import FC
from Button import Button

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
round_range = 2
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
sc = g.display.set_mode((SCW, SCH))
#sc = g.display.set_mode((SCW, SCH), g.FULLSCREEN)

images = {
    "BG" : g.image.load(f'src\\draha02.png').convert_alpha(),
    "Fitness meter" : g.image.load(f'src\\Fitness_meter.png').convert_alpha(),
    "car" : g.image.load(f'src\\auto01.png').convert_alpha(),
    "gen button" : g.image.load(f'src\\Gen_button.png').convert_alpha()
}
meters = [
    Fitness_meter(images["Fitness meter"],(65, 434),90),
    Fitness_meter(images["Fitness meter"],(90, 300),90),
    Fitness_meter(images["Fitness meter"],(396, 71),0),
    Fitness_meter(images["Fitness meter"],(500, 250),0),
    Fitness_meter(images["Fitness meter"],(575, 550),0),
    Fitness_meter(images["Fitness meter"],(644, 303),0),
    Fitness_meter(images["Fitness meter"],(755, 377),0),
    Fitness_meter(images["Fitness meter"],(800, 377),0),
    Fitness_meter(images["Fitness meter"],(855, 377),0),
    Fitness_meter(images["Fitness meter"],(1077, 700),0),
    Fitness_meter(images["Fitness meter"],(1000, 1170),0),
    Fitness_meter(images["Fitness meter"],(1300, 800),0),
    Fitness_meter(images["Fitness meter"],(855, 800),0),
    Fitness_meter(images["Fitness meter"],(65, 600),90),
]

bg = BG(images["BG"],c.LIGHT_BROWN,SCW,SCH,meters)
eyes = Eyes()
gen_button = Button(images["gen button"])
cars = []

for _ in range(count):
    cars.append(Car(images["car"],speed_max,angle_max,
                    NN(5,3,6,2)
                    ))

def start_with_random_dna():
    for index in range(count):
        cars[index].NN.generate_random_dna(weight_range,bias_range,round_range)

def input_dna():
    pass


def new_gen():
    print("NEW GEN!!")
clock = g.time.Clock()
FPS = 60

print("curent gen: " + str(gen_count))
start_with_random_dna()
while 1:
    for event in g.event.get():
        if event.type == g.KEYDOWN:
            if event.key == g.K_ESCAPE:
                exit()
        if event.type == g.MOUSEBUTTONDOWN:
            if gen_button.Fl_clicked(g.mouse.get_pos()):
                new_gen()
        '''
        if event.type == mutation_clock:
            gen_count +=1
            print("curent gen: " + str(gen_count))
            heighest_fitness = 0
            heighest_fitness_index = 0
            for auto in cars:
                if auto.fitness > heighest_fitness:
                    heighest_fitness = auto.fitness
                    heighest_fitness_index = cars.index(auto)


            best_dnaW = cars[heighest_fitness_index].dnaW
            best_dnaB = cars[heighest_fitness_index].dnaB
            cars.clear()
            for _ in range(count):
                cars.append(NN(best_dnaW,best_dnaB))

            for auto in cars:
                auto.mutate()
        
            if event.key == g.K_SPACE:
                g.time.set_timer(mutation_clock,0)
                copy_auta = cars.copy()
                for i in copy_auta:
                    if i.fitness != heighest_fitness:
                        cars.remove(i)
                copy_auta.clear()
                for i in cars:
                    print("START START START START START START START START START START START START START START START START ")
                    print(i.dnaW,i.dnaB)
                    print("STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP STOP ")
            if event.key == g.K_w:
                gen_count +=1
                print("curent gen: " + str(gen_count))
                heighest_fitness = 0
                heighest_fitness_index = 0
                for auto in cars:
                    if auto.fitness > heighest_fitness:
                        heighest_fitness = auto.fitness
                        heighest_fitness_index = cars.index(auto)
    
    
                best_dnaW = cars[heighest_fitness_index].dnaW
                best_dnaB = cars[heighest_fitness_index].dnaB
                cars.clear()
                for _ in range(count):
                    cars.append(NN(best_dnaW,best_dnaB))
    
                for auto in cars:
                    auto.mutate()
'''

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
    sc.blit(bg.draw(),(0,0)) # draw BG
    sc.blit(gen_button.get_image(), gen_button.get_rect())
    for car_index in range(len(cars)): # draw cars
        
        inputs = eyes.lines(
                cars[car_index].get_rect().centerx,
                cars[car_index].get_rect().centery,
                cars[car_index].angle,
                bg.get_image(),
                sc,
                (SCW,SCH),
                fl_lines
                )

        if not inputs:
            cars[car_index].stop()
        else:
            for input_index in range(len(inputs)):
                inputs[input_index] = inputs[input_index] //100
            outputs = cars[car_index].NN.predict(inputs)

            for output_index in range(len(outputs)):
                outputs[output_index] = outputs[output_index]*100
            
            cars[car_index].move(outputs)

        #for element2 in meters:
        #    cars[car_index].add_fitness(element2)
        sc.blit(cars[car_index].get_image(),cars[car_index].get_rect())
    g.display.update()
    clock.tick(FPS)