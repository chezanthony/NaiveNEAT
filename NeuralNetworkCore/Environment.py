from NeuralNetworkCore.InnovationNumber import CInnovationNumber
from NeuralNetworkCore.GeneRepository import CGeneRepository
from NeuralNetworkCore.NetworkFactory import CNetworkFactory


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
                             population=10,
                             n_input_nodes=1,
                             n_output_nodes=1):
        for nIndex in population:
            network = CNetworkFactory.create_network(nIndex,
                                                     network_params,
                                                     self._global_Gene_Repository,
                                                     n_input_nodes,
                                                     n_output_nodes)
            self._networks.update({nIndex:
                                   network})

    def run_evolution(self):
        pass
