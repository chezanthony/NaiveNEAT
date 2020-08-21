from NeuralNetworkCore.NodeMutator import CNodeMutator
from NeuralNetworkCore.ConnectionMutator import CConnectionMutator


class CMutator:

    @staticmethod
    def mutate(nodes,
               connections,
               network_params):
        CNodeMutator.mutate(nodes,
                            connections,
                            network_params)

        CConnectionMutator.mutate(nodes,
                                  connections,
                                  network_params)
