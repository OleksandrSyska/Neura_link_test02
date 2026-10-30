# import libraries
import classes.colors as c
import pygame as g

# import files
from classes.Neural_Sytem3 import NN
from classes.Back_Ground import BG
from classes.Car import Car
from classes.Eyes import Eyes
from classes.Fitness_Meter import Fitness_meter
from classes.Fitness_Cotroler import FC
#from classes.Button import Button
from classes.Button import button
from classes.Changeble_button import C_Button
import value_control.settings as SET
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
    for index in range(SET.count):
        cars[index].NN.generate_random_dna(SET.weight_range,SET.bias_range,SET.round_range)

def start_with_dna(dna):
    for index in range(SET.count):
        cars[index].NN.input_dna(dna)
    

def new_gen():
    global gen_count
    if not cars:
        return
    gen_count += 1
    print(f"Current generation: {gen_count}")
    heighest_fitness = 0
    heighest_fitness_index = 0
    for car in cars:
        if car.fit_con.get_fitness() == heighest_fitness:
            # CROSS MUTATION !!!! WIP
            heighest_fitness = car.fit_con.get_fitness()
            heighest_fitness_index = cars.index(car)
        if car.fit_con.get_fitness() > heighest_fitness:
            heighest_fitness = car.fit_con.get_fitness()
            heighest_fitness_index = cars.index(car)

    best_dna = cars[heighest_fitness_index].NN.get_dna()
    print(f"Best fitnes {heighest_fitness}")
    start_with_dna(best_dna)

    for car in cars:
        car.reset()
        car.fit_con.reset()
        if cars.index(car) != heighest_fitness_index:
            car.NN.mutate(
                SET.min_weight_mutation,
                SET.max_weight_mutation,
                SET.weight_mutation_range,
                SET.min_bias_mutation,
                SET.max_bias_mutation,
                SET.bias_mutation_range,
                SET.round_range
            )

# pygame init
g.init()
sc = g.display.set_mode((SET.SCW, SET.SCH)) # init. display

mutation_clock = g.USEREVENT + 1
g.time.set_timer(mutation_clock,0) # mutation delay
images = {
    "BG" : g.image.load(f'src\\draha01.png').convert_alpha(),
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
    Fitness_meter(images["Fitness meter"],(500, 500),0),
    Fitness_meter(images["Fitness meter"],(575, 550),0),
    Fitness_meter(images["Fitness meter"],(600, 550),0),
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
gen_button = button((SET.SCW,0),"NEW GEN")
auto_gen_swicht = C_Button((SET.SCW,200),["AUTO GEN: OFF","AUTO GEN: ON"])
bg = BG(images["BG"],c.LIGHT_BROWN,SET.SCW,SET.SCH,meters)
for _ in range(SET.count): # create cars
    cars.append(
        Car(
            images["car"],
            SET.speed_max,
            SET.angle_max,
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
            mouse_pos = g.mouse.get_pos()
            if gen_button.Fl_clicked(mouse_pos):
                new_gen()
            if auto_gen_swicht.Fl_clicked(mouse_pos):
                if auto_gen_swicht.get_state():
                    g.time.set_timer(mutation_clock,SET.auto_gen_time)
                else:
                    g.time.set_timer(mutation_clock,0)

        
        if event.type == mutation_clock:
            new_gen()
#----------------------------------------------------------------------
    sc.blit(bg.draw(),(0,0)) # draw BG
    #sc.blit(gen_button.get_image(), gen_button.get_rect())
    gen_button.draw(sc)
    auto_gen_swicht.draw(sc)
    for car_index in range(len(cars)): # moves and draw cars
        if not cars[car_index].get_status(): # checks if car has stopped
            inputs = eyes.lines( # gets distances
                cars[car_index].get_rect().centerx,
                cars[car_index].get_rect().centery,
                cars[car_index].angle,
                bg.get_image(),
                sc,
                (SET.SCW,SET.SCH),
                SET.fl_lines
                )
            if not inputs: # stops car if distances were 0 => crashed
                cars[car_index].stop()
                for meter in meters:
                    if meter not in cars[car_index].fit_con.get_used_meters():
                        if meter.collide_check(cars[car_index].get_rect()):
                            cars[car_index].fit_con.add_used_meter(meter)
                            cars[car_index].fit_con.add_fitness()
            else: # predicts and moves car
                for input_index in range(len(inputs)): # edit raw data to be smaller
                    inputs[input_index] = inputs[input_index] /100
                outputs = cars[car_index].NN.predict(inputs)
        
                for output_index in range(len(outputs)): # edit calculated data
    
                    #outputs[output_index] = outputs[output_index]*7 # FIXME 4*
                    outputs[0] *= 7  # Speed change
                    outputs[1] *= 3  # Angle change 
                
                cars[car_index].move(outputs)
                for meter in meters:
                    if meter not in cars[car_index].fit_con.get_used_meters():
                        if meter.collide_check(cars[car_index].get_rect()):
                            cars[car_index].fit_con.add_used_meter(meter)
                            cars[car_index].fit_con.add_fitness()


        #for element2 in meters:
        #    cars[car_index].add_fitness(element2)
        sc.blit(cars[car_index].get_image(),cars[car_index].get_rect())
    g.display.update()
    clock.tick(FPS)