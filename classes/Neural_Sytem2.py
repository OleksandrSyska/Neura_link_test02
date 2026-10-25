import random as r
# range(0,1) -> 0
# randint(0,1) -> 0/1
# UPDATE: added biases + fixed mutation
class NN(): # creates empty Neural Network in list format
    def __init__(self,input_neuron_count,hidden_layer_column_count,hidden_layer_neuron_count,output_neuron_count):
        if hidden_layer_column_count <= 0:
            raise ValueError(
                f'Minimal value for "hidden_layer_column_count" is 1, but {hidden_layer_column_count} was given.'
            )
        self.INC = input_neuron_count
        self.HLCC = hidden_layer_column_count
        self.HLGC = hidden_layer_column_count -1 # hidden layer gap count
        self.HLNC = hidden_layer_neuron_count
        self.ONC = output_neuron_count
        
        self.WC = self.INC * self.HLNC + self.HLGC*self.HLNC*self.HLNC + self.HLNC*self.ONC
        self.BC = self.HLCC * self.HLNC + self.ONC

        self.weights = []
        self.biases = []
        for _ in range(self.HLCC+1):
            self.weights.append([])

        for _ in range(self.HLCC+1):
            self.biases.append([])


    def generate_random_dna(self,weight_range,bias_range,round_range): 
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
        return [
        [layer.copy() for layer in self.weights],
        [layer.copy() for layer in self.biases]
        ]
    
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
            next_cells.clear()
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

    def mutate(self,min_weight_mutation,max_weight_mutation,weight_mutation_range,min_bias_mutation,max_bias_mutation,bias_mutation_range,round_range):
        already_mutated_index_W = []
        
        for _ in range(self.HLCC+1):
            already_mutated_index_W.append([])

        already_mutated_index_B = []
        for _ in range(self.HLCC+1):
            already_mutated_index_B.append([])
        # MUTATION OF WEIGHTS
        if min_weight_mutation < 0:
            raise ValueError(
                '"min_weight_mutation" cant less than 0.'
            )
        if max_weight_mutation > self.WC:
            raise ValueError(
                f'"max_weight_mutation" cant excede nor be equel to amount of weights, which is {self.WC}.'
            )
        #TODO 1*
        available_indexes = []
        for _ in range(r.randint(min_weight_mutation,max_weight_mutation)): # choses between min and max amount to mutate
            while not available_indexes:
                available_indexes = [] # list to determine unused indexes in chosen column 
                chosen_column = r.randint(0,self.HLCC) # choses which column to mutate
                for index in range(len(self.weights[chosen_column])): # determine unused indexes in chosen column 
                    if index not in already_mutated_index_W[chosen_column]:
                        available_indexes.append(index)
            chosen_index = r.choice(available_indexes)
            self.weights[chosen_column][chosen_index] += round(r.uniform(-weight_mutation_range,weight_mutation_range),round_range)
            already_mutated_index_W[chosen_column].append(chosen_index)
        
        # MUTATION OF BIASES
        if min_bias_mutation < 0:
            raise ValueError(
                '"min_bias_mutation" cant less than 0.'
            )
        
        if max_bias_mutation > self.BC:
            raise ValueError(
                f'"max_bias_mutation" cant excede nor be equel to amount of weights, which is {self.BC}.'
            )
        
        available_indexes = []
        for _ in range(r.randint(min_bias_mutation,max_bias_mutation)):
            while not available_indexes:
                available_indexes = [] # list to determine unused indexes in chosen column 
                chosen_column = r.randint(0,self.HLCC) # choses which column to mutate
                for index in range(len(self.biases[chosen_column])): # determine unused indexes in chosen column 
                    if index not in already_mutated_index_B[chosen_column]:
                        available_indexes.append(index)
            chosen_index = r.choice(available_indexes)
            self.biases[chosen_column][chosen_index] += round(r.uniform(-bias_mutation_range,bias_mutation_range),round_range)
            already_mutated_index_B[chosen_column].append(chosen_index)