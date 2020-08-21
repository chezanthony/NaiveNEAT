from NeuralNetworkCore.Connection import CConnection


class CConnectionFactory:

    @staticmethod
    def create_connection(n_innovation_number,
                          n_input_node_key,
                          n_output_node_key,
                          n_weight,
                          b_is_enabled=True):
        return CConnection(n_innovation_number,
                           n_input_node_key,
                           n_output_node_key,
                           n_weight,
                           b_is_enabled)
