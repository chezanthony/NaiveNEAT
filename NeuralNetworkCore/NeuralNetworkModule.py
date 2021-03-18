from NeuralNetworkCore.NetworkParams import CNetworkParams
from NeuralNetworkCore.NetworkFactory import CNetworkFactory


class CNeuralNetworkModule:

    def __init__(self):
        self.network_params = None
        self.network = None

    def initialize_network_params(self,
                                  n_node_deletion_probability,
                                  n_node_addition_probability,
                                  n_node_split_probability,
                                  n_node_value_mutation_probability,
                                  n_connection_deletion_probability,
                                  n_connection_addition_probability,
                                  n_connection_weight_mutation_probability,
                                  n_input_nodes,
                                  n_output_nodes):

        self.network_params =\
            CNetworkParams(
                n_node_deletion_probability,
                n_node_addition_probability,
                n_node_split_probability,
                n_node_value_mutation_probability,
                n_connection_deletion_probability,
                n_connection_addition_probability,
                n_connection_weight_mutation_probability,
                n_input_nodes,
                n_output_nodes)

    def create_network(self,
                       network_params,
                       n_input_nodes=1,
                       n_output_nodes=1,
                       n_network_id=1):

        self.network =\
            CNetworkFactory.create_network(
                network_params,
                n_input_nodes,
                n_output_nodes,
                n_network_id)

    def mutate_network(self):
        self.network.mutate()
