from NeuralNetworkCore.GeneAttribute import CGeneAttribute
from NeuralNetworkCore.IGene import IGene


class CGene(IGene):
    def __init__(self,
                 n_innovation_number,
                 b_is_node):
        self._n_Innovation_Number = n_innovation_number
        self._b_Is_Node = b_is_node
        self._gene_attributes = dict()

    def __hash__(self):
        return hash(self._n_Innovation_Number)

    def get_innovation_number(self):
        return self._n_Innovation_Number

    def is_node(self):
        return self._b_Is_Node

    def set_attribute(self,
                      s_attribute_name,
                      attribute_value):
        new_attribute = CGeneAttribute(s_attribute_name, attribute_value)
        self._gene_attributes[s_attribute_name] = new_attribute

    def get_attribute(self, s_attribute_name):
        return self._gene_attributes.get(s_attribute_name)

    def get_attributes(self):
        return self._gene_attributes
