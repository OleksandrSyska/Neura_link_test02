import random as r
class NS(): # creates empty NS in list form
    def __init__(self,input_neuron_count,hidden_layer_column_count,hidden_layer_neuron_count,output_neuron_count):
        self.INC = input_neuron_count
        self.HLCC = hidden_layer_column_count
        self.HLGC = hidden_layer_column_count -1 # hidden layer gap count
        self.HLNC = hidden_layer_neuron_count
        self.ONC = output_neuron_count

        self.weights = []
        self.biases = []
        for _ in range(self.HLCC+1):
            self.weights.append([])

        for _ in range(self.HLCC+1):
            self.biases.append([])


    def generate_random_dna(self,weight_range,round_range,bias_range): 
        # generates random weight values
        for _ in range(self.INC*self.HLNC): # input to first hidden
            self.weights[0].append(round(r.uniform(-weight_range,weight_range),round_range))

        for column in range(self.HLGC): # between hidden
            for _ in range(self.HLNC * self.HLNC):
                self.weights[column+1].append(round(r.uniform(-weight_range,weight_range),round_range))

        for _ in range(self.ONC*self.HLNC): # last hidden to output
            self.weights[-1].append(round(r.uniform(-weight_range,weight_range),round_range))

        # generates random bias values
        
        for column in range(self.HLCC): # hidden columns
            for _ in range(self.HLNC):
                self.biases[column].append(round(r.uniform(-bias_range,bias_range),round_range))
        for _ in range(self.ONC):
            self.biases[-1].append(round(r.uniform(-bias_range,bias_range),round_range))
            
    
    def get_dna(self): # returns dna
        return [self.weights,self.biases]
    
    def predict(self,inputs): # predicts and returns output
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
        for hidden_cell_index in range(self.HLNC): # cycle trough first hidden layer
            curent_cell = self.biases[0][hidden_cell_index]
            for x_index in range(len(inputs)): # cycle trough inputs
                curent_cell += inputs[x_index]*self.weights[0][curent_weight]
                curent_weight += 1
            next_cells.append(curent_cell)

        curent_cells = next_cells.copy()
        next_cells.clear()
        curent_weight = 0

        # hidden to hidden
        for gap_index in range(self.HLGC): # how many exchanges
            for hidden_cell_index in range(self.HLNC): # cycle trough n+1 layer
                curent_cell = self.biases[gap_index+1][hidden_cell_index]
                for cell_index in range(self.HLNC): # cycle trough n layer
                    curent_cell += curent_cells[cell_index] * self.weights[gap_index+1][curent_weight] # first gap is input -> +1
                    curent_weight += 1
                #
                next_cells.append(curent_cell)
            #
            curent_cells = next_cells.copy()
            curent_weight = 0

        # last hidden to output

        for output_cell_index in range(self.ONC):
            curent_cell = self.biases[-1][output_cell_index]
            for cell_index in range(self.HLNC):
                curent_cell += curent_cells[cell_index] * self.weights[-1][curent_weight]
                curent_weight += 1
            output_cells.append(curent_cell)

        return output_cells

    def input_dna(self,new_dna):
        self.weights = [layer.copy() for layer in new_dna[0]]
        self.biases = [layer.copy() for layer in new_dna[1]]




ns = NS(2,3,3,2)
ns.generate_random_dna(1,1)
print(ns.predict([2,3]))
print(ns.get_dna())