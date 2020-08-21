import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from NeuralNetworkCore.NodeMutator import CNodeMutator


class CNodeMutatorTest(unittest.TestCase):
    def setUp(self):
        self.mock_Nodes = MagicMock()
        self.mock_Connections = MagicMock()
        self.mock_Network_Params = MagicMock()
        self.mock_Node = MagicMock()
        self.mock_Connection = MagicMock()
        self.mock_Connection.get_output_node =\
            MagicMock(return_value=self.mock_Node)

        self.n_Test_Probability = 0.50
        self.mock_Network_Params.get_param =\
            MagicMock(return_value=self.n_Test_Probability)

        self.test_Connection_List =\
            [self.mock_Connection]
        self.mock_Connections.values =\
            MagicMock(return_value=self.test_Connection_List)

    @patch('NeuralNetworkCore.NodeMutator.CNodeMutator._node_deletion')
    @patch('NeuralNetworkCore.NodeMutator.CNodeMutator._bias_node_addition')
    @patch('NeuralNetworkCore.NodeMutator.CNodeMutator._node_split')
    def test_mutate_node_deletion_mutated(self,
                                          mock_node_split,
                                          mock_bias_node_addition,
                                          mock_node_deletion):
        CNodeMutator.mutate(self.mock_Nodes,
                            self.mock_Connections,
                            self.mock_Network_Params)

        mock_node_deletion.\
            assert_called_with(self.mock_Nodes,
                               self.mock_Connections,
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
        CNodeMutator.mutate(self.mock_Nodes,
                            self.mock_Connections,
                            self.mock_Network_Params)

        mock_node_deletion.\
            assert_called()
        mock_bias_node_addition.\
            assert_called_with(self.mock_Nodes,
                               self.mock_Connections,
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
        CNodeMutator.mutate(self.mock_Nodes,
                            self.mock_Connections,
                            self.mock_Network_Params)

        mock_node_deletion.\
            assert_called()
        mock_bias_node_addition.\
            assert_called()
        mock_node_split.\
            assert_called_with(self.mock_Nodes,
                               self.mock_Connections,
                               self.mock_Network_Params)

    @patch('NeuralNetworkCore.NodeMutator.CMutatorUtils.is_mutation_successful')
    @patch('NeuralNetworkCore.NodeMutator.CMutationRandomizer.randomize_element')
    def test_node_deletion(self,
                           mock_randomize_element,
                           mock_is_mutation_successful):
        mock_is_mutation_successful.\
            return_value = True
        mock_randomize_element.\
            return_value = self.mock_Node

    @patch('NeuralNetworkCore.NodeMutator.CMutatorUtils.is_mutation_successful')
    @patch('NeuralNetworkCore.NodeMutator.CMutatorUtils.add_new_bias_node')
    def test_bias_node_addition(self,
                                mock_add_new_bias_node,
                                mock_is_mutation_successful):
        mock_is_mutation_successful.\
            return_value = True

        CNodeMutator.\
            _bias_node_addition(self.mock_Nodes,
                                self.mock_Connections,
                                self.mock_Network_Params)

        mock_add_new_bias_node.\
            assert_called_with(self.mock_Nodes,
                               self.mock_Connections)

    @patch('NeuralNetworkCore.NodeMutator.CMutatorUtils.is_mutation_successful')
    @patch('NeuralNetworkCore.NodeMutator.CMutatorUtils.add_new_bias_node')
    def test_bias_node_addition_mutation_failed(
                                self,
                                mock_add_new_bias_node,
                                mock_is_mutation_successful):
        mock_is_mutation_successful.\
            return_value = False
        CNodeMutator.\
            _bias_node_addition(self.mock_Nodes,
                                self.mock_Connections,
                                self.mock_Network_Params)

        mock_add_new_bias_node.\
            assert_not_called()

    @patch('NeuralNetworkCore.NodeMutator.CMutatorUtils.is_mutation_successful')
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
            _node_split(self.mock_Nodes,
                        self.mock_Connections,
                        self.mock_Network_Params)

        mock_add_new_connection.\
            assert_called_with(self.mock_Connections,
                               mock_new_node,
                               mock_old_output_node)

    @patch('NeuralNetworkCore.NodeMutator.CMutatorUtils.is_mutation_successful')
    @patch('NeuralNetworkCore.NodeMutator.CMutatorUtils.add_new_connection')
    def test_node_split_mutation_failed(self,
                                        mock_add_new_connection,
                                        mock_is_mutation_successful):
        mock_is_mutation_successful.\
            return_value = False

        CNodeMutator.\
            _node_split(self.mock_Nodes,
                        self.mock_Connections,
                        self.mock_Network_Params)

        mock_add_new_connection.\
            assert_not_called()


if __name__ == '__main__':
    unittest.main()
