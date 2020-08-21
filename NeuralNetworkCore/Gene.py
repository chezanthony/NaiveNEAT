from NeuralNetworkCore.GeneAttribute import CGeneAttribute


class CGene:
    def __init__(self,
                 n_innovation_number):
        self._n_Innovation_Number = n_innovation_number
        self._gene_attributes = list()

    def __hash__(self):
        return self._n_Innovation_Number

    def get_innovation_number(self):
        return self._n_Innovation_Number

    def set_attribute(self,
                      s_attribute_name,
                      attribute_value):

        if self._attribute_exist(s_attribute_name):
            for attribute in self._gene_attributes:
                if attribute.get_attribute_name() == s_attribute_name:
                    attribute.set_attribute_value(attribute_value)
                    break
        else:
            new_attribute = \
                CGeneAttribute(s_attribute_name, attribute_value)
            self._gene_attributes.append(new_attribute)

    def get_attribute(self, s_attribute_name):

        return_attribute = None

        for attribute in self._gene_attributes:
            if s_attribute_name == attribute.get_attribute_name():
                return_attribute = attribute
                break

        return return_attribute

    def get_attributes(self):
        return self._gene_attributes

    def _attribute_exist(self, s_attribute_name):
        b_return = False

        for attribute in self._gene_attributes:
            if attribute.get_attribute_name() == s_attribute_name:
                b_return = True
                break

        return b_return
