from NeuralNetworkCore import NetworkConstants


class CNetworkParams:
    def __init__(self,
                 n_node_deletion_probability,
                 n_node_addition_probability,
                 n_node_split_probability,
                 n_node_value_mutation_probability,
                 n_connection_deletion_probability,
                 n_connection_addition_probability,
                 n_connection_weight_mutation_probability):
        self.params = {
            NetworkConstants.NODE_DELETION: n_node_deletion_probability,
            NetworkConstants.NODE_ADDITION: n_node_addition_probability,
            NetworkConstants.NODE_SPLIT: n_node_split_probability,
            NetworkConstants.NODE_VALUE_MUTATION: n_node_value_mutation_probability,
            NetworkConstants.CONNECTION_DELETION: n_connection_deletion_probability,
            NetworkConstants.CONNECTION_ADDITION: n_connection_addition_probability,
            NetworkConstants.CONNECTION_WEIGHT_MUTATION: n_connection_weight_mutation_probability,
        }

    def get_param(self, s_param_name):
        return self.params.get(s_param_name)
