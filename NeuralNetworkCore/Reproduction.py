from NeuralNetworkCore.ReproductionUtils import CReproductionUtils
from NeuralNetworkCore.NetworkFactory import CNetworkFactory
import random


class CReproduction:

    @staticmethod
    def reproduce(parent1, parent2, n_network_id):

        assert(type(parent1) == type(parent2), 'Different types')

        offspring_genes = dict()

        fit_parent, weak_parent =\
            CReproductionUtils.assign_parent_by_fitness(parent1,
                                                        parent2)

        offspring_genes.update(
            CReproductionUtils.get_matching_genes(fit_parent,
                                                  weak_parent))
        offspring_genes.update(
            CReproductionUtils.get_disjoint_genes(fit_parent,
                                                  weak_parent))
        offspring_genes.update(
            CReproductionUtils.get_excess_genes(fit_parent,
                                                weak_parent))

        network_params = fit_parent.get_network_params()
        gene_repository = fit_parent.get_gene_repository()

        # TODO: Allow creation of network with input and output nodes other than 1.
        offspring = CNetworkFactory.create_network(n_network_id,
                                                   network_params,
                                                   gene_repository,
                                                   1,
                                                   1)
        offspring.set_genes(offspring_genes)

        if random.random() >= 0.5:
            offspring.mutate()

        return offspring
