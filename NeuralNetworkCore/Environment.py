from NeuralNetworkCore.InnovationNumber import CInnovationNumber


class CEnvironment:
    def __init__(self,
                 innovation_number,
                 fitness_function):
        self._innovation_Number = innovation_number
        self._fitness_Function = fitness_function
        self._genomes = dict()

    def run_evolution(self):
        pass

