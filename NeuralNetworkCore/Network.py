from NeuralNetworkCore.Genome import CGenome
from NeuralNetworkCore.Mutator import CMutator
from NeuralNetworkCore.ConnectionRepository import CConnectionRepository
from NeuralNetworkCore.NodeRepository import CNodeRepository
from NeuralNetworkCore.InnovationNumber import CInnovationNumber


class CNetwork(CGenome):
    def __init__(self,
                 n_id,
                 network_params):
        self.n_ID = n_id
        self.network_Params = network_params
        self.innovation_Number = CInnovationNumber()
        self.node_Container = CNodeRepository(None)
        self.connection_Repository =\
            CConnectionRepository(self.innovation_Number)

        CGenome.__init__(self, n_id)

    def get_id(self):
        return self.n_ID

    def mutate(self):
        CMutator.mutate(self.node_Container,
                        self.connection_Repository,
                        self.network_Params)

    def add_node(self, node):
        self.node_Container.\
            update({node.get_innovation_number(): node})

    def get_node_container(self):
        return self.node_Container

    def get_connection_container(self):
        return self.connection_Repository
