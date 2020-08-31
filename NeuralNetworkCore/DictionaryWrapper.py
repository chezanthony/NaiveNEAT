from NeuralNetworkCore.IDictionaryWrapper import IDictionaryWrapper


class CDictionaryWrapper(IDictionaryWrapper):

    def __init__(self):
        self._dictionary = dict()
        IDictionaryWrapper.__init__(self)

    def __contains__(self, item):
        return item in self._dictionary

    def __delitem__(self, key):
        del self._dictionary[key]

    def __eq__(self, other):
        return self._dictionary == other._dictionary

    def __getitem__(self, item):
        return self._dictionary[item]

    def __setitem__(self, key, value):
        self._dictionary[key] = value

    def __sizeof__(self):
        return len(self._dictionary)

    def clear(self):
        self._dictionary.clear()

    def copy(self):
        return self._dictionary.copy()

    def get(self, key):
        return self._dictionary.get(key)

    def items(self):
        return self._dictionary.items()

    def pop(self, key, default=None):
        return self._dictionary.pop(key, default)

    def popitem(self):
        return self._dictionary.popitem()

    def setdefault(self, key, value=None):
        return self._dictionary.setdefault(key, value)

    def update(self, iterable):
        self._dictionary.update(iterable)

    def values(self):
        return self._dictionary.values()
