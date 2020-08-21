class CNetworkXNetworkInterpreter:
    @staticmethod
    def interpret_network(network, nx):
        node_container =\
            network.get_node_container()
        connection_container =\
            network.get_connection_container()

        CNetworkXNetworkInterpreter.\
            _add_nodes(node_container, nx)

        CNetworkXNetworkInterpreter.\
            _add_connections(connection_container,
                             node_container,
                             nx)

    @staticmethod
    def _add_nodes(nodes, nx):
        for node in nodes.values():
            nx.add_node(node)

    @staticmethod
    def _add_connections(connections,
                         nodes,
                         nx):
        for connection in connections.values():
            node_tuple =\
                CNetworkXNetworkInterpreter.\
                _get_nodes_from_connection(nodes,
                                           connection)

            n_input_node = node_tuple[0]
            n_output_node = node_tuple[1]

            nx.add_connection(n_input_node,
                              n_output_node)

    @staticmethod
    def _get_nodes_from_connection(nodes,
                                   connection):
        input_node =\
            nodes[connection.get_input_node_key()]
        output_node =\
            nodes[connection.get_output_node_key()]

        return input_node, output_node
