from abc import ABC
from abc import abstractmethod


class IConnectionRepository(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def get(self, n_innovation_number):
        raise NotImplementedError

    @abstractmethod
    def get_connection(self, n_innovation_number):
        raise NotImplementedError

    @abstractmethod
    def get_connection_from_input_node(self, input_node):
        raise NotImplementedError

    @abstractmethod
    def get_connection_from_output_node(self, output_node):
        raise NotImplementedError

    @abstractmethod
    def get_size(self):
        raise NotImplementedError

    @abstractmethod
    def update(self, connection):
        raise NotImplementedError

    @abstractmethod
    def pop(self, connection):
        raise NotImplementedError

    @abstractmethod
    def keys(self):
        raise NotImplementedError

    @abstractmethod
    def get_innovation_number(self,
                              n_input_node,
                              n_output_node):
        raise NotImplementedError
