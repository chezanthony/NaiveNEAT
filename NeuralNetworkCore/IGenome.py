from abc import ABC
from abc import abstractmethod


class IGenome(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def get_id(self):
        raise NotImplementedError

    @abstractmethod
    def evaluate_fitness(self,
                         f_fitness_function):
        raise NotImplementedError

    @abstractmethod
    def evaluate_fitness(self):
        raise NotImplementedError

    @abstractmethod
    def set_fitness_function(self,
                             f_fitness_function):
        raise NotImplementedError

    @abstractmethod
    def get_fitness(self):
        raise NotImplementedError

    @abstractmethod
    def mutate(self):
        raise NotImplementedError
