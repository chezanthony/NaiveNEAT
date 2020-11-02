from NeuralNetworkCore.IConnectionRepository import IConnectionRepository


class CConnectionRepository(IConnectionRepository):

    def __init__(self, innovation_number, gene_repository):
        self._connections = dict()
        self._innovation_Number = innovation_number
        self._gene_Repository = gene_repository
        self._n_Min_Innovation_Number = 0
        self._n_Max_Innovation_Number = 0
        IConnectionRepository.__init__(self)

    def __hash__(self):
        return hash(self._connections)

    def __iter__(self):
        return iter(self._connections)

    def __next__(self):
        return next(self._connections)

    def __len__(self):
        return len(self._connections)

    def get(self, n_innovation_number):
        return self._connections.get(n_innovation_number)

    def get_connection(self, n_innovation_number):
        return self.get(n_innovation_number)

    def get_connection_from_input_node(self, input_node):

        return_connection = None

        for n_key in self._connections:
            connection = self._connections.get(n_key)
            if input_node == connection.get_input_node():
                return_connection = connection
                break

        return return_connection

    def get_connection_from_output_node(self, output_node):

        return_connection = None

        for connection in self._connections:
            if output_node == connection.get_output_node():
                return_connection = connection
                break

        return return_connection

    def get_size(self):
        return len(self._connections)

    def update(self, iterable):
        self._connections.update(iterable)
        self._gene_Repository.update(iterable)
        self._update_innovation_numbers()

    def pop(self, connection):
        n_innovation_number = connection.get_innovation_number()
        self._connections.pop(n_innovation_number)

    def keys(self):
        return self._connections.keys()

    def get_innovation_number(self,
                              n_input_node,
                              n_output_node):
        return self.\
            _innovation_Number.\
            get_connection_innovation_number(n_input_node,
                                             n_output_node)

    def get_connections(self):
        return self._connections

    def get_min_innovation_number(self):
        return self._n_Min_Innovation_Number

    def get_max_innovation_number(self):
        return self._n_Max_Innovation_Number

    def _update_innovation_numbers(self):
        n_size = len(self._connections)
        keys = list(self._connections.keys())
        n_innovation_number = keys[n_size - 1]

        if self._n_Min_Innovation_Number == 0:
            self._n_Min_Innovation_Number = n_innovation_number

        if self._n_Max_Innovation_Number < n_innovation_number:
            self._n_Max_Innovation_Number = n_innovation_number
