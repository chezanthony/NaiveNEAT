from NeuralNetworkCore.Network import CNetwork
from NeuralNetworkCore.NodeFactory import CNodeFactory
from NeuralNetworkCore.NodeType import NodeType
from NeuralNetworkCore import NetworkConstants


class CNetworkFactory:

    @staticmethod
    def create_network(n_network_id,
                       network_params,
                       gene_repository):

        network = CNetwork(n_network_id,
                           network_params,
                           gene_repository)

        n_input_nodes =\
            network_params.get_param(NetworkConstants.INPUT_NODES)

        for nIndex in range(n_input_nodes):
            node =\
                CNodeFactory.create_node(nIndex,
                                         NodeType.INPUT)
            network.add_node(node)

        n_output_nodes =\
            network_params.get_param(NetworkConstants.OUTPUT_NODES)

        for nIndex in range(n_output_nodes):
            node =\
                CNodeFactory.create_node(nIndex,
                                         NodeType.OUTPUT)

            network.add_node(node)

        return network
