from abc import ABC
from abc import abstractmethod


class IGene(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def get_innovation_number(self):
        raise NotImplementedError

    @abstractmethod
    def set_attribute(self,
                      s_attribute_name,
                      attribute_value):
        raise NotImplementedError

    @abstractmethod
    def get_attribute(self, s_attribute_name):
        raise NotImplementedError
