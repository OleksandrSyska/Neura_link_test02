class FC():
    def __init__(self):
        self.fitnesses = []
        self.fitness = 0

    def add_fitness(self,fit):
        if self.rect.colliderect(fit):
            if not fit in self.fitnesses:
                self.fitnesses.append(fit)
                self.fitness += 1 
