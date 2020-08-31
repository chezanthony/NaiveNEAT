from NeuralNetworkCore import NetworkConstants
from NeuralNetworkCore.MutationRandomizer import CMutationRandomizer
from NeuralNetworkCore.MutatorUtils import CMutatorUtils


class CConnectionMutator:

    @staticmethod
    def mutate(nodes,
               connections,
               network_params):
        CConnectionMutator\
            ._mutate_connection_deletion(connections,
                                         network_params)
        CConnectionMutator\
            ._mutate_connection_addition(nodes,
                                         connections,
                                         network_params)

    @staticmethod
    def _mutate_connection_deletion(connections,
                                    network_params):

        n_probability =\
            network_params.get_param(NetworkConstants.CONNECTION_DELETION)

        if CMutationRandomizer.is_mutation_successful(n_probability):
            connection =\
                CMutationRandomizer.randomize_element(connections)
            connections.pop(connection)

    @staticmethod
    def _mutate_connection_addition(nodes,
                                    connections,
                                    network_params):

        n_probability =\
            network_params.get_param(NetworkConstants.CONNECTION_ADDITION)

        if CMutationRandomizer.is_mutation_successful(n_probability):

            n_input_node_key =\
                CMutationRandomizer.randomize_element(nodes)
            n_output_node_key = \
                CMutationRandomizer.randomize_element(nodes,
                                                      n_input_node_key)

            new_connection =\
                CMutatorUtils.add_new_connection(connections,
                                                 n_input_node_key,
                                                 n_output_node_key)
