from NeuralNetworkUI.NetworkPlotterType\
    import NetworkPlotterType
from NeuralNetworkUI.NetworkXPlotter\
    import CNetworkXPlotter


class CNetworkPlotter:
    def __init__(self,
                 plotter_type=NetworkPlotterType.NETWORKX):
        self.network_Plotter_Type = plotter_type
        self.plotter_Dictionary = {
            NetworkPlotterType.NETWORK_X: CNetworkXPlotter.plot,
        }

    def plot(self, network):
        self.plotter_Dictionary[self.network_Plotter_Type](network)