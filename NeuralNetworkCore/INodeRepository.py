from abc import ABC
from abc import abstractmethod


class INodeRepository(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def pop(self, n_innovation_number):
        raise NotImplementedError

    @abstractmethod
    def get_innovation_number(self,
                              node_type,
                              activation_function_type):
        raise NotImplementedError
