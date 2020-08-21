from NeuralNetworkCore import NetworkConstants
from NeuralNetworkCore.MutationRandomizer import CMutationRandomizer
from NeuralNetworkCore.MutatorUtils import CMutatorUtils


class CNodeMutator:

    @staticmethod
    def mutate(nodes,
               connections,
               network_params):
        CNodeMutator\
            ._node_deletion(nodes,
                            connections,
                            network_params)
        CNodeMutator\
            ._bias_node_addition(nodes,
                                 connections,
                                 network_params)
        CNodeMutator\
            ._node_split(nodes,
                         connections,
                         network_params)

    @staticmethod
    def _node_deletion(nodes,
                       connections,
                       network_params):

        n_probability =\
            network_params.get_param(NetworkConstants.NODE_DELETION)

        if CMutationRandomizer.is_mutation_successful(n_probability):

            node = CMutationRandomizer.randomize_element(nodes)
            nodes.pop(node)

            for connection in connections.values():
                if node == connection.get_output_node():
                    connections.pop(connection)

    @staticmethod
    def _bias_node_addition(nodes,
                            connections,
                            network_params):

        n_probability =\
            network_params.get_param(NetworkConstants.NODE_ADDITION)

        if CMutationRandomizer.is_mutation_successful(n_probability):
            CMutatorUtils.add_new_bias_node(nodes, connections)

    @staticmethod
    def _node_split(nodes,
                    connections,
                    network_params):

        n_probability =\
            network_params.get_param(NetworkConstants.NODE_SPLIT)

        if CMutationRandomizer.is_mutation_successful(n_probability):
            new_node = CMutatorUtils.add_new_node(nodes,
                                                  connections)
            connection =\
                CMutationRandomizer.randomize_element(connections)

            old_output_node = connection.get_output_node()
            connection.set_output_node(new_node)
            CMutatorUtils.add_new_connection(connections,
                                             new_node,
                                             old_output_node)
