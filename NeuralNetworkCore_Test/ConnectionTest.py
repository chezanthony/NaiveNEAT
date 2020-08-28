import unittest
from unittest.mock import Mock
from NeuralNetworkCore.Connection import CConnection


class CConnectionTest(unittest.TestCase):
    def setUp(self):
        self.n_Test_Innovation_Number = 1
        self.n_Test_Input_Node = Mock()
        self.n_Test_Input_Node.get_innovation_number = Mock()
        self.n_Test_Output_Node = Mock()
        self.n_Test_Weight = 5
        self.b_Test_Is_Enabled = True
        self.connection =\
            CConnection(self.n_Test_Innovation_Number,
                        self.n_Test_Input_Node,
                        self.n_Test_Output_Node,
                        self.n_Test_Weight,
                        self.b_Test_Is_Enabled)

    def test_hash(self):
        n_expected_hash = hash(self.n_Test_Innovation_Number)
        n_actual_hash = hash(self.connection)

        self.assertEqual(n_expected_hash,
                         n_actual_hash)

    def test_equality(self):
        test_connection = self.connection

        self.assertEqual(test_connection,
                         self.connection)

    def test_equality_different_innovation_number(self):
        test_connection =\
            CConnection(99,
                        self.n_Test_Input_Node,
                        self.n_Test_Output_Node,
                        self.n_Test_Weight,
                        self.b_Test_Is_Enabled)

        self.assertFalse(self.connection ==\
                         test_connection)

    def test_equality_different_input_node(self):
        test_input_node = Mock()
        test_connection =\
            CConnection(self.n_Test_Innovation_Number,
                        test_input_node,
                        self.n_Test_Output_Node,
                        self.n_Test_Weight,
                        self.b_Test_Is_Enabled)

        self.assertFalse(self.connection ==\
                         test_connection)

    def test_equality_different_output_node(self):
        test_output_node = Mock()
        test_connection =\
            CConnection(self.n_Test_Innovation_Number,
                        self.n_Test_Input_Node,
                        test_output_node,
                        self.n_Test_Weight,
                        self.b_Test_Is_Enabled)

        self.assertFalse(self.connection ==\
                         test_connection)

    def test_equality_different_weight(self):
        test_weight = 99
        test_connection =\
            CConnection(self.n_Test_Innovation_Number,
                        self.n_Test_Input_Node,
                        self.n_Test_Output_Node,
                        test_weight,
                        self.b_Test_Is_Enabled)

        self.assertFalse(self.connection == test_connection)

    def test_equality_different_enabled_status(self):
        test_enabled_status = False
        test_connection =\
            CConnection(self.n_Test_Innovation_Number,
                        self.n_Test_Input_Node,
                        self.n_Test_Output_Node,
                        self.n_Test_Weight,
                        test_enabled_status)

        self.assertFalse(self.connection == test_connection)

    def test_get_innovation_number(self):
        n_expected_innovation_number =\
            self.n_Test_Innovation_Number
        n_actual_innovation_number =\
            self.connection.get_innovation_number()

        self.assertEqual(n_expected_innovation_number,
                         n_actual_innovation_number)

    def test_get_input_node(self):
        expected_input_node =\
            self.n_Test_Input_Node
        actual_input_node =\
            self.connection.get_input_node()

        self.assertEqual(expected_input_node,
                         actual_input_node)

    def test_get_output_node(self):
        expected_output_node =\
            self.n_Test_Output_Node
        actual_output_node =\
            self.connection.get_output_node()

        self.assertEqual(expected_output_node,
                         actual_output_node)

    def test_set_output_node(self):
        test_output_node = Mock()
        self.connection.\
            set_output_node(test_output_node)

        actual_output_node =\
            self.connection.get_output_node()

        self.assertEqual(test_output_node,
                         actual_output_node)

    def test_get_weight(self):
        n_expected_weight =\
            self.n_Test_Weight
        n_actual_weight =\
            self.connection.get_weight()

        self.assertEqual(n_expected_weight,
                         n_actual_weight)

    def test_is_enabled(self):
        b_expected_is_enabled =\
            self.b_Test_Is_Enabled
        b_actual_is_enabled =\
            self.connection.is_enabled()

        self.assertEqual(b_expected_is_enabled,
                         b_actual_is_enabled)

    def test_set_is_enabled(self):
        node_enabled_status_tuple =\
            (True,
             False)

        for status in node_enabled_status_tuple:
            self.connection.set_is_enabled(status)
            self.assertEqual(status,
                             self.connection.is_enabled())


if __name__ == '__main__':
    unittest.main()
