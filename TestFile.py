from NeuralNetworkCore.NetworkParams import CNetworkParams
from NeuralNetworkCore.NetworkFactory import CNetworkFactory


def main():
    network_params = CNetworkParams(0.25,
                                    0.25,
                                    0.25,
                                    0.25,
                                    0.25,
                                    0.25,
                                    0.25)

    network =\
        CNetworkFactory.\
        create_network(network_params,
                       2,
                       1)

    network.mutate()


if __name__ == '__main__':
    main()
