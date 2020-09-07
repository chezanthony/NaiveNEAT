from NeuralNetworkCore.Genome import CGenome
from NeuralNetworkCore.Mutator import CMutator
from NeuralNetworkCore.ConnectionRepository import CConnectionRepository
from NeuralNetworkCore.NodeRepository import CNodeRepository
from NeuralNetworkCore.InnovationNumber import CInnovationNumber
from NeuralNetworkCore.GeneRepository import CGeneRepository


class CNetwork(CGenome):
    def __init__(self,
                 n_id,
                 network_params):
        self.n_ID = n_id
        self.network_Params = network_params
        self.gene_Repository = CGeneRepository()
        self.innovation_Number = CInnovationNumber(self.gene_Repository)
        self.node_Repository =\
            CNodeRepository(self.innovation_Number,
                            self.gene_Repository)
        self.connection_Repository =\
            CConnectionRepository(self.innovation_Number,
                                  self.gene_Repository)

        CGenome.__init__(self, n_id)

    def get_id(self):
        return self.n_ID

    def mutate(self):
        CMutator.mutate(self.node_Repository,
                        self.connection_Repository,
                        self.network_Params)

    def add_node(self, node):
        node_type = node.get_node_type()
        activation_function_type = node.get_activation_function_type()
        n_innovation_number =\
            self.node_Repository.\
            get_innovation_number(node_type,
                                  activation_function_type)

        self.node_Repository.\
            update({n_innovation_number: node})

    def add_connection(self, connection):
        n_input_node_key = connection.get_input_node()
        n_output_node_key = connection.get_output_node()
        n_innovation_number =\
            self.connection_Repository.\
            get_innovation_number(n_input_node_key,
                                  n_output_node_key)
        self.connection_Repository.\
            update({n_innovation_number: connection})

    def get_node_container(self):
        return self.node_Repository

    def get_connection_container(self):
        return self.connection_Repository
