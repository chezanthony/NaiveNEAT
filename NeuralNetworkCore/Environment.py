from NeuralNetworkCore.GeneRepository import CGeneRepository
from NeuralNetworkCore.NetworkFactory import CNetworkFactory
from NeuralNetworkCore.Evolution import CEvolution


class CEnvironment:
    def __init__(self,
                 innovation_number,
                 fitness_function):
        self._innovation_Number = innovation_number
        self._fitness_Function = fitness_function
        self._genomes = dict()
        self._global_Gene_Repository = CGeneRepository()
        self._networks = dict()

    def populate_environment(self,
                             network_params,
                             n_population=10):
        for nIndex in range(n_population):
            network = CNetworkFactory.create_network(nIndex,
                                                     network_params,
                                                     self._global_Gene_Repository)
            self._networks.update({nIndex:
                                   network})

    def run_evolution(self,
                      n_iterations,
                      n_target_fitness):
        CEvolution.run_evolution(self._fitness_Function,
                                 self._networks,
                                 n_iterations,
                                 n_target_fitness)
