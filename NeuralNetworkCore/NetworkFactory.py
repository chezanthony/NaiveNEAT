from NeuralNetworkCore.Network import CNetwork
from NeuralNetworkCore.NodeFactory import CNodeFactory
from NeuralNetworkCore.NodeType import NodeType


class CNetworkFactory:

    @staticmethod
    def create_network(n_network_id,
                       network_params,
                       gene_repository,
                       n_input_nodes=1,
                       n_output_nodes=1):

        network = CNetwork(n_network_id,
                           network_params,
                           gene_repository)

        for nIndex in range(n_input_nodes):
            node =\
                CNodeFactory.create_node(nIndex,
                                         NodeType.INPUT)
            network.add_node(node)

        for nIndex in range(n_output_nodes):
            node =\
                CNodeFactory.create_node(nIndex,
                                         NodeType.OUTPUT)

            network.add_node(node)

        return network
