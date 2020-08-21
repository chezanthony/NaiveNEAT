from NeuralNetworkCore.Node import CNode
from NeuralNetworkCore.NodeType import NodeType
from NeuralNetworkCore.ActivationFunctionType import ActivationFunctionType


class CNodeFactory:

    @staticmethod
    def create_node(n_innovation_number,
                    node_type=NodeType.HIDDEN,
                    activation_function=ActivationFunctionType.LINEAR):
        return CNode(n_innovation_number,
                     node_type,
                     activation_function)
