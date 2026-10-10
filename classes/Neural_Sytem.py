import random as r
class NS(): # creates empty NS in list form
    def __init__(self,input_neuron_count,hidden_layer_column_count,hidden_layer_neuron_count,output_neuron_count):
        self.INC = input_neuron_count
        self.HLCC = hidden_layer_column_count
        self.HLGC = hidden_layer_column_count -1 # hidden layer gap count
        self.HLNC = hidden_layer_neuron_count
        self.ONC = output_neuron_count

        self.dna = []
        for _ in range(hidden_layer_column_count+1):
            self.dna.append([])


    def generate_random_dna(self,weight_range,round_range): # generates random weight values
        for _ in range(self.INC*self.HLNC): # input to first hidden
            self.dna[0].append(round(r.uniform(-weight_range,weight_range),round_range))

        for column in range(self.HLGC): # between hidden
            for _ in range(self.HLNC * self.HLNC):
                self.dna[column+1].append(round(r.uniform(-weight_range,weight_range),round_range))

        for _ in range(self.ONC*self.HLNC): # last hidden to output
            self.dna[-1].append(round(r.uniform(-weight_range,weight_range),round_range))
    
    def get_dna(self): # returns dna
        return self.dna
    def predict(self,inputs): # predicts
        if len(inputs) != self.INC:
            raise ValueError(
                f"Expected {self.INC} inputs, but {len(inputs)} were given."
            )

        
        curent_cells = [] # cells that we are working with
        next_cells = [] # cells that we save for next layer

        curent_cell = 0 # curent cell that we are calculating at the moment
        curent_weight = 0 # curent weight index that we are working with

        output_cells = []
        # Input to first hidden
        for _ in range(self.HLNC): 
            curent_cell = 0
            for x_index in range(len(inputs)):
                curent_cell += inputs[x_index]*self.dna[0][curent_weight]
                curent_weight += 1
            next_cells.append(curent_cell)

        curent_cells = next_cells.copy()
        next_cells.clear()
        curent_weight = 0
        curent_cell = 0

        # hidden to hidden
        for gap_index in range(self.HLGC): # how many exchanges
            for _ in range(self.HLNC): # cycle trough n+1 layer
                for cell_index in range(self.HLNC): # cycle trough n layer
                    curent_cell += curent_cells[cell_index] * self.dna[gap_index+1][curent_weight] # first gap is input -> +1
                    curent_weight += 1
                #
                next_cells.append(curent_cell)
                curent_cell = 0
            #
            curent_cells = next_cells.copy()
            curent_weight = 0

        # last hidden to output
        for _ in range(self.ONC):
            for cell_index in range(self.HLNC):
                curent_cell += curent_cells[cell_index] * self.dna[-1][curent_weight]
                curent_weight += 1
            output_cells.append(curent_cell)
            curent_cell = 0

        return output_cells




ns = NS(2,3,3,2)
ns.generate_random_dna(1,1)
print(ns.predict([2,3]))
print(ns.get_dna())