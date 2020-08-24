class CGenome:
    def __init__(self,
                 n_id):
        self._n_ID = n_id
        self._n_Fitness = None

    def __hash__(self):
        return hash(self._n_ID)

    def get_id(self):
        return self._n_ID

    def evaluate_fitness(self,
                         f_fitness_function):
        self._n_Fitness = f_fitness_function()
