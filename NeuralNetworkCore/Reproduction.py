from NeuralNetworkCore.Mutator import CMutator
from random import random
from NeuralNetworkCore.ReproductionUtils import CReproductionUtils


class CReproduction:

    @staticmethod
    def reproduce(parent1, parent2):

        assert(type(parent1) == type(parent2), 'Different types')

        fit_parent, weak_parent =\
            CReproductionUtils.assign_parent_by_fitness(parent1,
                                                        parent2)

        matching_genes =\
            CReproductionUtils.get_matching_genes(fit_parent,
                                                  weak_parent)

        disjoint_genes =\
            CReproductionUtils.get_disjoint_genes(fit_parent,
                                                  weak_parent)

        excess_genes =\
            CReproductionUtils.get_excess_genes(fit_parent,
                                                weak_parent)

        if random() > 0.5:
            pass
        else:
            pass
