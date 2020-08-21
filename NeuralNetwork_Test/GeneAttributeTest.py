import unittest
from NeuralNetworkCore.Gene import CGeneAttribute
from NeuralNetworkCore import NetworkConstants
from NeuralNetworkCore.NodeType import NodeType


class CGeneAttributeTest(unittest.TestCase):
    def setUp(self):
        self._s_Test_Attribute_Name = NetworkConstants.NODE_TYPE
        self._n_Test_Attribute_Value = NodeType.INPUT
        self._gene_Attribute = CGeneAttribute(self._s_Test_Attribute_Name,
                                              self._n_Test_Attribute_Value)

    def test_equality(self):
        test_attribute = CGeneAttribute(self._s_Test_Attribute_Name,
                                        self._n_Test_Attribute_Value)

        self.assertEqual(self._gene_Attribute,
                         test_attribute)

    def test_get_attribute_name(self):
        s_actual_attribute_name = self._gene_Attribute.get_attribute_name()

        self.assertEqual(self._s_Test_Attribute_Name,
                         s_actual_attribute_name)

    def test_get_attribute_value(self):
        n_actual_attribute_value = self._gene_Attribute.get_attribute_value()

        self.assertEqual(self._n_Test_Attribute_Value,
                         n_actual_attribute_value)

    def test_set_attribute_value(self):
        test_attribute_value = NodeType.HIDDEN
        self._gene_Attribute.set_attribute_value(test_attribute_value)

        actual_attribute_value = self._gene_Attribute.get_attribute_value()

        self.assertEqual(test_attribute_value,
                         actual_attribute_value)


if __name__ == '__main__':
    unittest.main()
