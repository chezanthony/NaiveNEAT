import unittest
from NeuralNetworkCore.Gene import CGene
from NeuralNetworkCore import NetworkConstants
from NeuralNetworkCore.ActivationFunctionType import ActivationFunctionType


class CGeneTest(unittest.TestCase):
    def setUp(self):
        self._n_Test_Innovation_Number = 1
        self._b_Test_Is_Node = True
        self._gene = CGene(self._n_Test_Innovation_Number,
                           self._b_Test_Is_Node)

    def test_hash(self):
        n_actual_hash = self._gene.__hash__()
        self.assertEqual(self._n_Test_Innovation_Number,
                         n_actual_hash)

    def test_get_innovation_number(self):
        n_actual_innovation_number = self._gene.get_innovation_number()
        self.assertEqual(self._n_Test_Innovation_Number,
                         n_actual_innovation_number)

    def test_set_attribute_verify_attribute_is_stored(self):
        gene_attributes = self._gene.get_attributes()
        n_attributes_size = len(gene_attributes)

        self._gene.set_attribute(NetworkConstants.ACTIVATION_FUNCTION_TYPE,
                                 ActivationFunctionType.LINEAR)

        new_gene_attributes = self._gene.get_attributes()
        n_new_attributes_size = len(new_gene_attributes)

        n_expected_new_size = n_attributes_size + 1
        self.assertEqual(n_expected_new_size,
                         n_new_attributes_size)

    def test_set_attribute_verify_stored_attribute_name_is_correct(self):
        self._gene.set_attribute(NetworkConstants.ACTIVATION_FUNCTION_TYPE,
                                 ActivationFunctionType.LINEAR)
        actual_attribute =\
            self._gene.get_attribute(NetworkConstants.ACTIVATION_FUNCTION_TYPE)
        s_actual_attribute_name = actual_attribute.get_attribute_name()

        self.assertEqual(NetworkConstants.ACTIVATION_FUNCTION_TYPE,
                         s_actual_attribute_name)

    def test_set_attribute_verify_stored_attribute_value_is_correct(self):
        self._gene.set_attribute(NetworkConstants.ACTIVATION_FUNCTION_TYPE,
                                 ActivationFunctionType.LINEAR)
        actual_attribute =\
            self._gene.get_attribute(NetworkConstants.ACTIVATION_FUNCTION_TYPE)
        n_actual_attribute_value = actual_attribute.get_attribute_value()

        self.assertEqual(ActivationFunctionType.LINEAR,
                         n_actual_attribute_value)

    def test_set_attribute_verify_existing_attribute_value_is_replaced(self):
        self._gene.set_attribute(NetworkConstants.ACTIVATION_FUNCTION_TYPE,
                                 ActivationFunctionType.LINEAR)
        actual_attribute =\
            self._gene.get_attribute(NetworkConstants.ACTIVATION_FUNCTION_TYPE)
        actual_attribute_value = actual_attribute.get_attribute_value()

        self._gene.set_attribute(NetworkConstants.ACTIVATION_FUNCTION_TYPE,
                                 ActivationFunctionType.SIGMOID)

        actual_new_attribute =\
            self._gene.get_attribute(NetworkConstants.ACTIVATION_FUNCTION_TYPE)
        actual_new_attribute_value = actual_new_attribute.get_attribute_value()

        self.assertNotEqual(actual_attribute_value,
                            actual_new_attribute_value)

    def test_get_attribute(self):
        self._gene.set_attribute(NetworkConstants.ACTIVATION_FUNCTION_TYPE,
                                 ActivationFunctionType.LINEAR)
        actual_attribute =\
            self._gene.get_attribute(NetworkConstants.ACTIVATION_FUNCTION_TYPE)
        s_actual_attribute_name = actual_attribute.get_attribute_name()
        n_actual_attribute_value = actual_attribute.get_attribute_value()

        self.assertEqual(NetworkConstants.ACTIVATION_FUNCTION_TYPE,
                         s_actual_attribute_name)
        self.assertEqual(ActivationFunctionType.LINEAR,
                         n_actual_attribute_value)

    def test_get_attributes(self):
        gene_attributes = self._gene.get_attributes()
        n_attributes_size = len(gene_attributes)

        self._gene.set_attribute(NetworkConstants.ACTIVATION_FUNCTION_TYPE,
                                 ActivationFunctionType.LINEAR)

        new_gene_attributes = self._gene.get_attributes()
        n_new_attributes_size = len(new_gene_attributes)

        n_expected_new_size = n_attributes_size + 1
        self.assertEqual(n_expected_new_size,
                         n_new_attributes_size)


if __name__ == '__main__':
    unittest.main()
