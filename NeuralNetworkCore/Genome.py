from NeuralNetworkCore.IGenome import IGenome


class CGenome(IGenome):
    def __init__(self,
                 n_id):
        self._n_ID = n_id
        self._n_Fitness = None
        self._f_Fitness_Function = None

    def __hash__(self):
        return hash(self._n_ID)

    def get_id(self):
        return self._n_ID

    def evaluate_fitness(self,
                         f_fitness_function):
        self._n_Fitness = f_fitness_function()

    def evaluate_fitness(self):
        self._n_Fitness = self._f_Fitness_Function()

    def set_fitness_function(self,
                             f_fitness_function):
        self._f_Fitness_Function = f_fitness_function

    def get_fitness(self):
        return self._n_Fitness

    def mutate(self):
        pass

    def reproduce(self):
        pass
