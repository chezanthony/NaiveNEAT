import networkx as nx
import matplotlib.pyplot as plt
from NeuralNetworkUI.NetworkXNetworkInterpreter\
    import CNetworkXNetworkInterpreter

# This class serves as a wrapper to the NetworkX library.
# The NetworkX library is currently being used to plot the
# current implementation of the network.
# This looks like a massive under-utilization of the NetworkX library,
# because it is.
# But the implementation of the network is already in place before
# the NetworkX library has been added, which is a poor excuse to
# not refactor the code.
# However, the many strengths of the NetworkX library is not urgently
# needed for this project.
# The main reason to refactor the code to use the library to represent
# the network would be to fix the inevitable performance issues when
# the network scales up.
# That will be addressed when those issues arise.


class CNetworkXPlotter:
    @staticmethod
    def plot(network):
        plot = nx.DiGraph()
        CNetworkXNetworkInterpreter.\
            interpret_network(network, plot)
        nx.draw(plot)
        plt.show()
