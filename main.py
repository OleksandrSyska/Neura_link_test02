# import libraries
import classes.colors as c
import pygame as g
import random as r
import math as m
# import files
from classes.Neural_Sytem2 import NN
from classes.Back_Ground import BG
from classes.Car import Car
from classes.Eyes import Eyes
from classes.Fitness_Meter import Fitness_meter
from classes.Fitness_Cotroler import FC
from classes.Button import Button
import value_control.settings as SE
# Constants
FPS = 60
# variables
gen_count = 1
# lists
cars = []
images = {}
meters = []
# functions
def start_with_random_dna():
    for index in range(SE.count):
        cars[index].NN.generate_random_dna(SE.weight_range,SE.bias_range,SE.round_range)

def start_with_dna(dna):
    for index in range(SE.count):
        cars[index].NN.input_dna(dna)
    

def new_gen():
    global gen_count
    gen_count += 1
    print("curent gen: " + str(gen_count))
    heighest_fitness = 0
    heighest_fitness_index = 0
    for car in cars:
        if car.fit_con.get_fitness() == heighest_fitness:
            pass # CROSS MUTATION !!!! WIP
        if car.fit_con.get_fitness() > heighest_fitness:
            heighest_fitness = car.fit_con.get_fitness()
            heighest_fitness_index = cars.index(car)


    best_dna = cars[heighest_fitness_index].NN.get_dna()
    start_with_dna(best_dna)

    for car in cars:
        car.reset()
        car.fit_con.reset()
        car.NN.mutate(
            SE.min_weight_mutation,
            SE.max_weight_mutation,
            SE.weight_mutation_range,
            SE.min_bias_mutation,
            SE.max_bias_mutation,
            SE.bias_mutation_range,
            SE.round_range
        )

# pygame init
g.init()
sc = g.display.set_mode((SE.SCW, SE.SCH)) # init. display

mutation_clock = g.USEREVENT + 1
g.time.set_timer(mutation_clock,0000) # mutation deelay
images = {
    "BG" : g.image.load(f'src\\draha02.png').convert_alpha(),
    "Fitness meter" : g.image.load(f'src\\Fitness_meter.png').convert_alpha(),
    "car" : g.image.load(f'src\\auto01.png').convert_alpha(),
    "gen button" : g.image.load(f'src\\Gen_button.png').convert_alpha()
}
# TODO CLEANUP
#DNA_INSERT_B = dif_map[1]
#DNA_INSERT_W = dif_map[0]
#sc = g.display.set_mode((SCW, SCH), g.FULLSCREEN)


# instances 
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
eyes = Eyes()
gen_button = Button(images["gen button"])
bg = BG(images["BG"],c.LIGHT_BROWN,SE.SCW,SE.SCH,meters)
for _ in range(SE.count): # create cars
    cars.append(
        Car(
            images["car"],
            SE.speed_max,
            SE.angle_max,
            NN(5,3,6,2),
            FC()
            )
        )


# main loop
clock = g.time.Clock()
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
                (SE.SCW,SE.SCH),
                SE.fl_lines
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