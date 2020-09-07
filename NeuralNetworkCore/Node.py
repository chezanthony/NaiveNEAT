from NeuralNetworkCore.NodeType import NodeType
from NeuralNetworkCore.ActivationFunctionType import ActivationFunctionType
from NeuralNetworkCore.Gene import CGene
from NeuralNetworkCore import NetworkConstants


class CNode(CGene):
    def __init__(self,
                 n_innovation_number,
                 node_type=NodeType.HIDDEN,
                 activation_function_type=ActivationFunctionType.LINEAR):
        self._n_Innovation_Number = n_innovation_number
        self._node_Type = node_type
        self._activation_Function_Type = activation_function_type

        CGene.__init__(self,
                       n_innovation_number,
                       True)
        CGene.set_attribute(self,
                            NetworkConstants.NODE_TYPE,
                            self._node_Type)
        CGene.set_attribute(self,
                            NetworkConstants.ACTIVATION_FUNCTION_TYPE,
                            self._activation_Function_Type)

    def __hash__(self):
        return CGene.__hash__(self)

    def __eq__(self, other):
        b_return = False

        if(self._n_Innovation_Number == other.get_innovation_number() and
           self._node_Type == other.get_node_type() and
           self._activation_Function_Type == other.get_activation_function_type()):
            b_return = True

        return b_return

    def get_node_type(self):
        return self._node_Type

    def get_activation_function_type(self):
        return self._activation_Function_Type
