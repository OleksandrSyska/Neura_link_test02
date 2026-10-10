class FC():
    def __init__(self):
        self.fitness = 0
    def add_fitness(self):
        self.fitness += 1
    def reset(self):
        self.fitness = 0
    def get_fitness(self):
        return self.fitness
