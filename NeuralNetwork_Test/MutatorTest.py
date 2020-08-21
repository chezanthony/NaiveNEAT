import unittest
from unittest.mock import Mock
from unittest.mock import patch
from NeuralNetworkCore.Mutator import CMutator


class CMutatorTest(unittest.TestCase):
    def setUp(self):
        self.mock_Node_Container = Mock()
        self.mock_Connection_Container = Mock()
        self.mock_Network_Params = Mock()

        self.n_TestProbability = 0.50
        self.mock_Network_Params.get_param =\
            Mock(return_value=self.n_TestProbability)

    @patch('NeuralNetworkCore.Mutator.CNodeMutator.mutate')
    @patch('NeuralNetworkCore.Mutator.CConnectionMutator.mutate')
    def test_mutate_node_mutator_mutate_called(self,
                                               mock_node_mutator_mutate,
                                               mock_connection_mutator_mutate):
        CMutator.mutate(self.mock_Node_Container,
                        self.mock_Connection_Container,
                        self.mock_Network_Params)

        mock_node_mutator_mutate.\
            assert_called_with(self.mock_Node_Container,
                               self.mock_Connection_Container,
                               self.mock_Network_Params)

        mock_connection_mutator_mutate.assert_called()

    @patch('NeuralNetworkCore.Mutator.CNodeMutator.mutate')
    @patch('NeuralNetworkCore.Mutator.CConnectionMutator.mutate')
    def test_mutate_connection_mutator_mutate_called(
            self,
            mock_connection_mutator_mutate,
            mock_node_mutator_mutate):
        CMutator.mutate(self.mock_Node_Container,
                        self.mock_Connection_Container,
                        self.mock_Network_Params)

        mock_node_mutator_mutate.assert_called()

        mock_connection_mutator_mutate.\
            assert_called_with(self.mock_Node_Container,
                               self.mock_Connection_Container,
                               self.mock_Network_Params)


if __name__ == '__main__':
    unittest.main()
