from NeuralNetworkCore.Gene import CGene
from NeuralNetworkCore import NetworkConstants


class CConnection(CGene):
    def __init__(self,
                 n_innovation_number,
                 n_input_node,
                 n_output_node,
                 n_weight,
                 b_is_enabled=True):
        self.n_Innovation_Number = n_innovation_number
        self.n_Input_Node = n_input_node
        self.n_Output_Node = n_output_node
        self.n_Weight = n_weight
        self.b_Is_Enabled = b_is_enabled

        CGene.__init__(self, n_innovation_number)
        CGene.set_attribute(NetworkConstants.INPUT_NODE,
                            self.n_Input_Node)
        CGene.set_attribute(NetworkConstants.OUTPUT_NODE,
                            self.n_Output_Node)
        CGene.set_attribute(NetworkConstants.WEIGHT,
                            self.n_Weight)
        CGene.set_attribute(NetworkConstants.IS_ENABLED,
                            self.b_Is_Enabled)

    def __hash__(self):
        return CGene.__hash__(self)

    def __eq__(self, other):
        b_return = False

        if(self.n_Innovation_Number == other.n_Innovation_Number and
           self.n_Input_Node == other.n_Input_Node and
           self.n_Output_Node == other.n_Output_Node and
           self.n_Weight == other.n_Weight and
           self.b_Is_Enabled == other.b_Is_Enabled):
            b_return = True

        return b_return

    def get_input_node(self):
        return self.n_Input_Node

    def get_output_node(self):
        return self.n_Output_Node

    def set_output_node(self, n_output_node):
        self.n_Output_Node = n_output_node

    def get_weight(self):
        return self.n_Weight

    def is_enabled(self):
        return self.b_Is_Enabled

    def set_is_enabled(self, b_is_enabled):
        self.b_Is_Enabled = b_is_enabled
