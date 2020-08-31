from NeuralNetworkCore.MutationRandomizer import CMutationRandomizer
from NeuralNetworkCore.NodeFactory import CNodeFactory
from NeuralNetworkCore.ConnectionFactory import CConnectionFactory


class CMutatorUtils:

    @staticmethod
    def is_mutation_successful(s_network_param,
                               network_params):
        b_return = False
        n_probability =\
            network_params.get_param(s_network_param)

        if CMutationRandomizer.is_mutation_successful(n_probability):
            b_return = True

        return b_return

    @staticmethod
    def add_new_bias_node(nodes, connections):
        new_node = CMutatorUtils._create_node(nodes)

        output_node = CMutationRandomizer\
            .randomize_element(nodes)

        CMutatorUtils\
            ._create_connection(connections,
                                new_node.get_innovation_number(),
                                output_node.get_innovation_number())

        return new_node

    @staticmethod
    def add_new_node(nodes, connections):
        new_node = CMutatorUtils.add_new_bias_node(nodes,
                                                   connections)

        input_node = CMutationRandomizer\
            .randomize_element(nodes)

        CMutatorUtils\
            ._create_connection(connections,
                                input_node.get_innovation_number(),
                                new_node.get_innovation_number())

        return new_node

    @staticmethod
    def add_new_connection(connections,
                           n_input_node_key,
                           n_output_node_key):
        new_connection =\
            CMutatorUtils._create_connection(connections,
                                             n_input_node_key,
                                             n_output_node_key)
        return new_connection

    @staticmethod
    def get_random_element(container):
        return CMutationRandomizer.randomize_element(container)

    @staticmethod
    def _create_node(nodes):
        n_innovation_number = nodes.get_innovation_number()

        new_node = CNodeFactory.create_node(n_innovation_number)

        nodes.update({n_innovation_number:
                      new_node})

        return new_node

    @staticmethod
    def _create_connection(connections,
                           n_input_node_key,
                           n_output_node_key):
        n_innovation_number = connections.get_innovation_number()
        n_weight = CMutationRandomizer.randomize_value()

        new_connection =\
            CConnectionFactory\
            .create_connection(n_innovation_number,
                               n_input_node_key,
                               n_output_node_key,
                               n_weight)

        connections.update({n_innovation_number:
                            new_connection})

        return new_connection
