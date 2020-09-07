import unittest
from unittest.mock import Mock
from unittest.mock import patch
from NeuralNetworkCore.ConnectionMutator import CConnectionMutator


class CConnectionMutatorTest(unittest.TestCase):
    def setUp(self):
        self.mock_Nodes = Mock()
        self.mock_Connections = Mock()
        self.mock_Network_Params = Mock()

        self.n_TestProbability = 0.50
        self.mock_Network_Params.get_param =\
            Mock(return_value=self.n_TestProbability)

    @patch('NeuralNetworkCore.'
           'ConnectionMutator.'
           'CConnectionMutator.'
           '_mutate_connection_deletion')
    @patch('NeuralNetworkCore.'
           'ConnectionMutator.'
           'CConnectionMutator.'
           '_mutate_connection_addition')
    @patch('NeuralNetworkCore.'
           'ConnectionMutator.'
           'CConnectionMutator.'
           '_mutate_connection_weight')
    def test_mutate_connection_deletion_mutated(
            self,
            mock_mutate_connection_weight,
            mock_mutate_connection_addition,
            mock_mutate_connection_deletion):
        CConnectionMutator.mutate(self.mock_Nodes,
                                  self.mock_Connections,
                                  self.mock_Network_Params)

        mock_mutate_connection_deletion.\
            assert_called_with(self.mock_Connections,
                               self.mock_Network_Params)
        mock_mutate_connection_addition.\
            assert_called()
        mock_mutate_connection_weight.\
            assert_called()

    @patch('NeuralNetworkCore.'
           'ConnectionMutator.'
           'CConnectionMutator.'
           '_mutate_connection_deletion')
    @patch('NeuralNetworkCore.'
           'ConnectionMutator.'
           'CConnectionMutator.'
           '_mutate_connection_addition')
    @patch('NeuralNetworkCore.'
           'ConnectionMutator.'
           'CConnectionMutator.'
           '_mutate_connection_weight')
    def test_mutate_connection_addition_mutated(
            self,
            mock_mutate_connection_weight,
            mock_mutate_connection_addition,
            mock_mutate_connection_deletion):
        CConnectionMutator.mutate(self.mock_Nodes,
                                  self.mock_Connections,
                                  self.mock_Network_Params)

        mock_mutate_connection_deletion.\
            assert_called()
        mock_mutate_connection_addition.\
            assert_called_with(self.mock_Nodes,
                               self.mock_Connections,
                               self.mock_Network_Params)
        mock_mutate_connection_weight.\
            assert_called()

    @patch('NeuralNetworkCore.'
           'ConnectionMutator.'
           'CConnectionMutator.'
           '_mutate_connection_deletion')
    @patch('NeuralNetworkCore.'
           'ConnectionMutator.'
           'CConnectionMutator.'
           '_mutate_connection_addition')
    @patch('NeuralNetworkCore.'
           'ConnectionMutator.'
           'CConnectionMutator.'
           '_mutate_connection_weight')
    def test_mutate_connection_weight_called(
            self,
            mock_mutate_connection_weight,
            mock_mutate_connection_addition,
            mock_mutate_connection_deletion):
        CConnectionMutator.mutate(self.mock_Nodes,
                                  self.mock_Connections,
                                  self.mock_Network_Params)

        mock_mutate_connection_deletion.\
            assert_called()
        mock_mutate_connection_addition.\
            assert_called()
        mock_mutate_connection_weight.\
            assert_called_with(self.mock_Connections,
                               self.mock_Network_Params)
