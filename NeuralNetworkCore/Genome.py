from NeuralNetworkCore.IGenome import IGenome
from NeuralNetworkCore.Reproduction import CReproduction


class CGenome(IGenome):
    def __init__(self,
                 n_id):
        self._n_ID = n_id
        self._n_Fitness = None
        self._f_Fitness_Function = None

    def __hash__(self):
        return hash(self._n_ID)

    def __gt__(self, other):
        return self._n_Fitness > other.get_fitness()

    def __lt__(self, other):
        return self._n_Fitness < other.get_fitness()

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
