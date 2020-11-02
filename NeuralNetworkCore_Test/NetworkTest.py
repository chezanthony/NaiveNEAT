import unittest
from unittest.mock import Mock
from unittest.mock import patch
from NeuralNetworkCore.Network import CNetwork
from NeuralNetworkCore.Node import CNode
from NeuralNetworkCore.Connection import CConnection


class CNetworkTest(unittest.TestCase):
    def setUp(self):
        self._n_Test_ID = 1

        self._mock_Network_Params = Mock()

        self._mock_Gene = Mock()
        self._mock_Gene.is_node = Mock(return_value=True)

        self._test_Gene_Repository_Dict = dict()
        self._test_Gene_Repository_Dict.update({0:
                                                Mock()})

        self._mock_Gene_Repository = Mock()
        self._mock_Gene_Repository.get =\
            Mock(return_value=self._mock_Gene)
        self._mock_Gene_Repository.__iter__ =\
            Mock(return_value=self._test_Gene_Repository_Dict.__iter__())

        self._network = CNetwork(self._n_Test_ID,
                                 self._mock_Network_Params,
                                 self._mock_Gene_Repository)
        self._n_Test_Input_Node_Key = 1
        self._test_Input_Node = CNode(self._n_Test_Input_Node_Key)

        self._n_Test_Output_Node_Key = 2
        self._test_Output_Node = CNode(self._n_Test_Output_Node_Key)

        self._n_Test_Connection_Key = 3
        self._n_Test_Weight = 1
        self._test_Connection = CConnection(self._n_Test_Connection_Key,
                                            self._n_Test_Input_Node_Key,
                                            self._n_Test_Output_Node_Key,
                                            self._n_Test_Weight)

    def test_node_container_is_initially_empty(self):
        node_container =\
            self._network.get_node_container()
        n_node_container_size = len(node_container)

        self.assertEqual(0,
                         n_node_container_size)

    def test_connection_container_is_initially_empty(self):
        connection_container =\
            self._network.get_connection_container()
        n_connection_container_size = len(connection_container)

        self.assertEqual(0,
                         n_connection_container_size)

    def test_get_ID(self):
        n_expected_id = self._n_Test_ID
        n_actual_id = self._network.get_id()

        self.assertEqual(n_expected_id,
                         n_actual_id)

    @patch('NeuralNetworkCore.Network.CMutator.mutate')
    def test_mutate(self, mock_mutator):
        self._network.mutate()
        mock_mutator.assert_called()

    def test_add_node(self):
        self._network.add_node(self._test_Input_Node)

        node_container =\
            self._network.get_node_container()

        actual_node = node_container.get(self._n_Test_Input_Node_Key)

        self.assertEqual(self._test_Input_Node,
                         actual_node)

    def test_add_node_node_container_size_increments_by_one(self):
        node_container =\
            self._network.get_node_container()
        n_node_container_size =\
            len(node_container)

        self.assertEqual(0,
                         n_node_container_size)

        self._network.add_node(self._test_Input_Node)

        n_node_container_size =\
            len(node_container)

        self.assertEqual(1,
                         n_node_container_size)

    def test_add_connection(self):
        self._network.add_node(self._test_Input_Node)
        self._network.add_node(self._test_Output_Node)
        self._network.add_connection(self._test_Connection)

        connection_container =\
            self._network.get_connection_container()

        actual_connection =\
            connection_container.get(self._n_Test_Connection_Key)

        self.assertEqual(self._test_Connection,
                         actual_connection)

    def test_add_connection_connection_container_size_increments_by_one(self):
        connection_container = \
            self._network.get_connection_container()
        n_connection_container_size =\
            len(connection_container)

        self.assertEqual(0,
                         n_connection_container_size)

        self._network.add_node(self._test_Input_Node)
        self._network.add_node(self._test_Output_Node)
        self._network.add_connection(self._test_Connection)

        n_node_container_size =\
            len(connection_container)

        self.assertEqual(1,
                         n_node_container_size)


if __name__ == '__main__':
    unittest.main()
