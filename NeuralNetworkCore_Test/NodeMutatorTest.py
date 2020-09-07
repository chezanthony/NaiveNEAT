import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from NeuralNetworkCore.NodeMutator import CNodeMutator
from NeuralNetworkCore.NodeType import NodeType
from NeuralNetworkCore.ActivationFunctionType import ActivationFunctionType
from NeuralNetworkCore.Node import CNode
from NeuralNetworkCore.Connection import CConnection
from NeuralNetworkCore.ConnectionRepository import CConnectionRepository
from NeuralNetworkCore.NodeRepository import CNodeRepository
from NeuralNetworkCore.InnovationNumber import CInnovationNumber
from NeuralNetworkCore.GeneRepository import CGeneRepository


class CNodeMutatorTest(unittest.TestCase):
    def setUp(self):
        self.gene_Repository = CGeneRepository()
        self.innovation_Number = CInnovationNumber(self.gene_Repository)
        self.test_Nodes = CNodeRepository(self.innovation_Number,
                                          self.gene_Repository)
        self.test_Connections =\
            CConnectionRepository(self.innovation_Number,
                                  self.gene_Repository)

        self.n_Test_Input_Node_Innovation_Number = 1
        self.test_Input_Node_Type = NodeType.INPUT
        self.test_Input_Node_Activation_Function_Type =\
            ActivationFunctionType.LINEAR
        self.test_Input_Node =\
            CNode(self.n_Test_Input_Node_Innovation_Number,
                  self.test_Input_Node_Type,
                  self.test_Input_Node_Activation_Function_Type)
        self.test_Nodes.update({self.n_Test_Input_Node_Innovation_Number:
                                self.test_Input_Node})

        self.n_Test_Hidden_Node_Innovation_Number = 2
        self.test_Hidden_Node_Type = NodeType.HIDDEN
        self.test_Hidden_Node_Activation_Function_Type =\
            ActivationFunctionType.LINEAR
        self.test_Hidden_Node =\
            CNode(self.n_Test_Hidden_Node_Innovation_Number,
                  self.test_Hidden_Node_Type,
                  self.test_Hidden_Node_Activation_Function_Type)
        self.test_Nodes.update({self.n_Test_Hidden_Node_Innovation_Number:
                                self.test_Hidden_Node})

        self.n_Test_Output_Node_Innovation_Number = 3
        self.test_Output_Node_Type = NodeType.OUTPUT
        self.test_Output_Node_Activation_Function_Type =\
            ActivationFunctionType.LINEAR
        self.test_Output_Node =\
            CNode(self.n_Test_Output_Node_Innovation_Number,
                  self.test_Output_Node_Type,
                  self.test_Output_Node_Activation_Function_Type)
        self.test_Nodes.update({self.n_Test_Output_Node_Innovation_Number:
                                self.test_Output_Node})

        self.n_Test_Connection1_Innovation_Number = 4
        self.n_Test_Connection1_Weight = 1
        self.b_Test_Connection1_Is_Enabled = True
        self.test_Connection1 =\
            CConnection(self.n_Test_Connection1_Innovation_Number,
                        self.test_Input_Node,
                        self.test_Hidden_Node,
                        self.n_Test_Connection1_Weight,
                        self.b_Test_Connection1_Is_Enabled)
        self.test_Connections.update({self.n_Test_Connection1_Innovation_Number:
                                      self.test_Connection1})

        self.n_Test_Connection2_Innovation_Number = 5
        self.n_Test_Connection2_Weight = 1
        self.b_Test_Connection2_Is_Enabled = True
        self.test_Connection2 =\
            CConnection(self.n_Test_Connection2_Innovation_Number,
                        self.test_Hidden_Node,
                        self.test_Output_Node,
                        self.n_Test_Connection2_Weight,
                        self.b_Test_Connection2_Is_Enabled)
        self.test_Connections.update({self.n_Test_Connection2_Innovation_Number:
                                      self.test_Connection2})

        self.mock_Network_Params = MagicMock()

        self.n_Test_Probability = 0.50
        self.mock_Network_Params.get_param =\
            MagicMock(return_value=self.n_Test_Probability)

    @patch('NeuralNetworkCore.NodeMutator.CNodeMutator._node_deletion')
    @patch('NeuralNetworkCore.NodeMutator.CNodeMutator._bias_node_addition')
    @patch('NeuralNetworkCore.NodeMutator.CNodeMutator._node_split')
    def test_mutate_node_deletion_mutated(self,
                                          mock_node_split,
                                          mock_bias_node_addition,
                                          mock_node_deletion):
        CNodeMutator.mutate(self.test_Nodes,
                            self.test_Connections,
                            self.mock_Network_Params)

        mock_node_deletion.\
            assert_called_with(self.test_Nodes,
                               self.test_Connections,
                               self.mock_Network_Params)
        mock_bias_node_addition.\
            assert_called()
        mock_node_split.\
            assert_called()

    @patch('NeuralNetworkCore.NodeMutator.CNodeMutator._node_deletion')
    @patch('NeuralNetworkCore.NodeMutator.CNodeMutator._bias_node_addition')
    @patch('NeuralNetworkCore.NodeMutator.CNodeMutator._node_split')
    def test_mutate_bias_node_added(self,
                                    mock_node_split,
                                    mock_bias_node_addition,
                                    mock_node_deletion):
        CNodeMutator.mutate(self.test_Nodes,
                            self.test_Connections,
                            self.mock_Network_Params)

        mock_node_deletion.\
            assert_called()
        mock_bias_node_addition.\
            assert_called_with(self.test_Nodes,
                               self.test_Connections,
                               self.mock_Network_Params)
        mock_node_split.\
            assert_called()

    @patch('NeuralNetworkCore.NodeMutator.CNodeMutator._node_deletion')
    @patch('NeuralNetworkCore.NodeMutator.CNodeMutator._bias_node_addition')
    @patch('NeuralNetworkCore.NodeMutator.CNodeMutator._node_split')
    def test_mutate_node_split_mutated(self,
                                       mock_node_split,
                                       mock_bias_node_addition,
                                       mock_node_deletion):
        CNodeMutator.mutate(self.test_Nodes,
                            self.test_Connections,
                            self.mock_Network_Params)

        mock_node_deletion.\
            assert_called()
        mock_bias_node_addition.\
            assert_called()
        mock_node_split.\
            assert_called_with(self.test_Nodes,
                               self.test_Connections,
                               self.mock_Network_Params)

    @patch('NeuralNetworkCore.NodeMutator.CMutationRandomizer.is_mutation_successful')
    @patch('NeuralNetworkCore.NodeMutator.CMutationRandomizer.randomize_element')
    def test_node_deletion(self,
                           mock_randomize_element,
                           mock_is_mutation_successful):
        mock_is_mutation_successful.\
            return_value = True
        mock_randomize_element.\
            return_value = self.test_Hidden_Node

        CNodeMutator._node_deletion(self.test_Nodes,
                                    self.test_Connections,
                                    self.mock_Network_Params)

        self.assertFalse(self.n_Test_Hidden_Node_Innovation_Number in self.test_Nodes)

    @patch('NeuralNetworkCore.NodeMutator.CMutationRandomizer.is_mutation_successful')
    @patch('NeuralNetworkCore.NodeMutator.CMutationRandomizer.randomize_element')
    def test_node_deletion_failed(self,
                                  mock_randomize_element,
                                  mock_is_mutation_successful):
        mock_is_mutation_successful.\
            return_value = False
        mock_randomize_element.\
            return_value = self.test_Hidden_Node

        CNodeMutator._node_deletion(self.test_Nodes,
                                    self.test_Connections,
                                    self.mock_Network_Params)

        self.assertTrue(self.n_Test_Hidden_Node_Innovation_Number in self.test_Nodes)

    @patch('NeuralNetworkCore.NodeMutator.CMutationRandomizer.is_mutation_successful')
    @patch('NeuralNetworkCore.NodeMutator.CMutatorUtils.add_new_bias_node')
    def test_bias_node_addition(self,
                                mock_add_new_bias_node,
                                mock_is_mutation_successful):
        mock_is_mutation_successful.\
            return_value = True

        CNodeMutator.\
            _bias_node_addition(self.test_Nodes,
                                self.test_Connections,
                                self.mock_Network_Params)

        mock_add_new_bias_node.\
            assert_called_with(self.test_Nodes,
                               self.test_Connections)

    @patch('NeuralNetworkCore.NodeMutator.CMutationRandomizer.is_mutation_successful')
    @patch('NeuralNetworkCore.NodeMutator.CMutatorUtils.add_new_bias_node')
    def test_bias_node_addition_mutation_failed(
                                self,
                                mock_add_new_bias_node,
                                mock_is_mutation_successful):
        mock_is_mutation_successful.\
            return_value = False
        CNodeMutator.\
            _bias_node_addition(self.test_Nodes,
                                self.test_Connections,
                                self.mock_Network_Params)

        mock_add_new_bias_node.\
            assert_not_called()

    @patch('NeuralNetworkCore.NodeMutator.CMutationRandomizer.is_mutation_successful')
    @patch('NeuralNetworkCore.NodeMutator.CMutatorUtils.add_new_node')
    @patch('NeuralNetworkCore.NodeMutator.CMutationRandomizer.randomize_element')
    @patch('NeuralNetworkCore.NodeMutator.CMutatorUtils.add_new_connection')
    def test_node_split(self,
                        mock_add_new_connection,
                        mock_randomize_element,
                        mock_add_new_node,
                        mock_is_mutation_successful):
        mock_is_mutation_successful.\
            return_value = True

        mock_new_node = MagicMock()
        mock_add_new_node.\
            return_value = mock_new_node

        mock_random_connection = MagicMock()
        mock_randomize_element.\
            return_value = mock_random_connection

        mock_old_output_node = MagicMock()
        mock_random_connection.\
            get_output_node.\
            return_value = mock_old_output_node

        CNodeMutator.\
            _node_split(self.test_Nodes,
                        self.test_Connections,
                        self.mock_Network_Params)

        mock_add_new_connection.\
            assert_called_with(self.test_Connections,
                               mock_new_node,
                               mock_old_output_node)

    @patch('NeuralNetworkCore.NodeMutator.CMutationRandomizer.is_mutation_successful')
    @patch('NeuralNetworkCore.NodeMutator.CMutatorUtils.add_new_connection')
    def test_node_split_mutation_failed(self,
                                        mock_add_new_connection,
                                        mock_is_mutation_successful):
        mock_is_mutation_successful.\
            return_value = False

        CNodeMutator.\
            _node_split(self.test_Nodes,
                        self.test_Connections,
                        self.mock_Network_Params)

        mock_add_new_connection.\
            assert_not_called()


if __name__ == '__main__':
    unittest.main()
