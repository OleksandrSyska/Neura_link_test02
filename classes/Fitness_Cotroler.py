class FC():
    def __init__(self):
        self.fitness = 0
        self.used_meters = []
    def add_fitness(self):
        self.fitness += 1
    def reset(self):
        self.fitness = 0
        self.used_meters = []
    def get_fitness(self):
        return self.fitness
    def get_used_meters(self):
        return self.used_meters
    def add_used_meter(self,meter):
        self.used_meters.append(meter)