from NeuralNetworkCore.INodeRepository import INodeRepository


class CNodeRepository(INodeRepository):

    def __init__(self, innovation_number):
        self._nodes = dict()
        self._innovation_Number = innovation_number
        INodeRepository.__init__(self)

    def __hash__(self):
        return hash(self._nodes)

    def __iter__(self):
        return iter(self._nodes)

    def __next__(self):
        return next(self._nodes)

    def __len__(self):
        return len(self._nodes)

    def pop(self, n_innovation_number):
        self._nodes.pop(n_innovation_number)

    def update(self, iterable):
        self._nodes.update(iterable)

    def get_innovation_number(self):
        return self._innovation_Number.get_innovation_number()
