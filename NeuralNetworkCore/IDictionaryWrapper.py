from abc import ABC
from abc import abstractmethod


class IDictionaryWrapper(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def __contains__(self, item):
        raise NotImplementedError

    @abstractmethod
    def __delitem__(self, key):
        raise NotImplementedError

    @abstractmethod
    def __eq__(self, other):
        raise NotImplementedError

    @abstractmethod
    def __getitem__(self, item):
        raise NotImplementedError

    @abstractmethod
    def __setitem__(self, key, value):
        raise NotImplementedError

    @abstractmethod
    def __sizeof__(self):
        raise NotImplementedError

    @abstractmethod
    def clear(self):
        raise NotImplementedError

    @abstractmethod
    def copy(self):
        raise NotImplementedError

    @abstractmethod
    def get(self, key):
        raise NotImplementedError

    @abstractmethod
    def items(self):
        raise NotImplementedError

    @abstractmethod
    def pop(self, key, default=None):
        raise NotImplementedError

    @abstractmethod
    def popitem(self):
        raise NotImplementedError

    @abstractmethod
    def setdefault(self, key, value):
        raise NotImplementedError

    @abstractmethod
    def update(self, iterable):
        raise NotImplementedError

    @abstractmethod
    def values(self):
        raise NotImplementedError
