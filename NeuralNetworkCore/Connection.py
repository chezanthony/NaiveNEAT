from NeuralNetworkCore.Gene import CGene
from NeuralNetworkCore import NetworkConstants


class CConnection(CGene):
    def __init__(self,
                 n_innovation_number,
                 n_input_node,
                 n_output_node,
                 n_weight,
                 b_is_enabled=True):
        self._n_Innovation_Number = n_innovation_number
        self._n_Input_Node = n_input_node
        self._n_Output_Node = n_output_node
        self._n_Weight = n_weight
        self._b_Is_Enabled = b_is_enabled

        CGene.__init__(self,
                       n_innovation_number,
                       False)
        CGene.set_attribute(self,
                            NetworkConstants.INPUT_NODE,
                            self._n_Input_Node)
        CGene.set_attribute(self,
                            NetworkConstants.OUTPUT_NODE,
                            self._n_Output_Node)
        CGene.set_attribute(self,
                            NetworkConstants.WEIGHT,
                            self._n_Weight)
        CGene.set_attribute(self,
                            NetworkConstants.IS_ENABLED,
                            self._b_Is_Enabled)

    def __hash__(self):
        return CGene.__hash__(self)

    def __eq__(self, other):
        b_return = False

        if(self._n_Innovation_Number == other.get_innovation_number() and
           self._n_Input_Node == other.get_input_node() and
           self._n_Output_Node == other.get_output_node()):
            b_return = True

        return b_return

    def get_input_node(self):
        return self._n_Input_Node

    def get_output_node(self):
        return self._n_Output_Node

    def set_output_node(self, n_output_node):
        self._n_Output_Node = n_output_node

    def get_weight(self):
        return self._n_Weight

    def set_weight(self, n_weight):
        self._n_Weight = n_weight

    def is_enabled(self):
        return self._b_Is_Enabled

    def set_is_enabled(self, b_is_enabled):
        self._b_Is_Enabled = b_is_enabled
