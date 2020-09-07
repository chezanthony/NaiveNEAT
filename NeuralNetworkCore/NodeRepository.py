from NeuralNetworkCore.INodeRepository import INodeRepository


class CNodeRepository(INodeRepository):

    def __init__(self, innovation_number, gene_repository):
        self._nodes = dict()
        self._innovation_Number = innovation_number
        self._gene_Repository = gene_repository
        INodeRepository.__init__(self)

    def __hash__(self):
        return hash(self._nodes)

    def __iter__(self):
        return iter(self._nodes)

    def __next__(self):
        return next(self._nodes)

    def __len__(self):
        return len(self._nodes)

    def __getitem__(self, key):
        return self._nodes.get(key)

    def pop(self, n_innovation_number):
        self._nodes.pop(n_innovation_number)

    def update(self, iterable):
        self._nodes.update(iterable)
        self._gene_Repository.update(iterable)

    def get_innovation_number(self,
                              node_type,
                              activation_function_type):
        # TODO: Since there are only few possible values for node activation
        #       function type, nodes are currently not that distinct.
        #       As of now, all nodes are considered unique in the global
        #       gene repository.
        #       Once more activation function types are added,
        #       the snippet below can be used.

        # return self.\
        #     _innovation_Number.\
        #     get_node_innovation_number(node_type,
        #                                activation_function_type)

        return self._innovation_Number.get_innovation_number()

    def get(self, key):
        return self._nodes.get(key)
