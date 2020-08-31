from NeuralNetworkCore.IConnectionRepository import IConnectionRepository


class CConnectionRepository(IConnectionRepository):

    def __init__(self, innovation_number):
        self._connections = dict()
        self._innovation_Number = innovation_number
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
        return self._connections[n_innovation_number]

    def get_connection(self, n_innovation_number):
        return self._connections[n_innovation_number]

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

    def pop(self, connection):
        n_innovation_number = connection.get_innovation_number()
        self._connections.pop(n_innovation_number)

    def keys(self):
        return self._connections.keys()

    def get_innovation_number(self):
        return self._innovation_Number.get_innovation_number()
