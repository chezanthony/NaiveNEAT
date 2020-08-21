import unittest
from NeuralNetworkCore.NodeType import NodeType
from NeuralNetworkCore.ActivationFunctionType import ActivationFunctionType
from NeuralNetworkCore.Node import CNode


class CNodeTest(unittest.TestCase):
    def setUp(self):
        self.n_Test_Innovation_Number = 5
        self.test_Node_Type = NodeType.HIDDEN
        self.test_Activation_Function =\
            ActivationFunctionType.LINEAR
        self.node =\
            CNode(self.n_Test_Innovation_Number,
                  self.test_Node_Type,
                  self.test_Activation_Function)

    def test_hash(self):
        n_actual_hash =\
            self.node.__hash__()

        self.assertEqual(self.n_Test_Innovation_Number,
                         n_actual_hash)

    def test_equality(self):
        test_node = self.node

        self.assertEqual(test_node,
                         self.node)

    def test_equality_different_innovation_number(self):
        test_node = CNode(99,
                          self.test_Node_Type,
                          self.test_Activation_Function)

        self.assertFalse(test_node == self.node)

    def test_equality_different_node_type(self):
        test_node = CNode(self.n_Test_Innovation_Number,
                          NodeType.INPUT,
                          self.test_Activation_Function)

        self.assertFalse(test_node == self.node)

    def test_equality_different_activation_function(self):
        test_node = CNode(self.n_Test_Innovation_Number,
                          self.test_Node_Type,
                          ActivationFunctionType.SIGMOID)

        self.assertFalse(test_node == self.node)

    def test_get_innovation_number(self):
        test_innovation_number =\
            self.node.get_innovation_number()

        self.assertEqual(self.n_Test_Innovation_Number,
                         test_innovation_number)

    def test_get_node_type(self):
        test_node_type =\
            self.node.get_node_type()

        self.assertEqual(self.test_Node_Type,
                         test_node_type)

    def test_get_activation_function_type(self):
        test_activation_function_type =\
            self.node.get_activation_function_type()

        self.assertEqual(self.test_Activation_Function,
                         test_activation_function_type)


if __name__ == '__main__':
    unittest.main()
