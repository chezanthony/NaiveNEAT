from random import random


class CReproductionUtils:

    @staticmethod
    def assign_parent_by_fitness(parent1, parent2):

        fit_parent =\
            parent1 if parent1 > parent2 else parent2
        weak_parent =\
            parent1 if parent1 < parent2 else parent2

        return fit_parent, weak_parent

    @staticmethod
    def get_matching_genes(parent1, parent2):
        parent1_genes = parent1.get_genes()
        parent2_genes = parent2.get_genes()

        genes = dict()

        for key in parent1_genes:
            if key in parent2_genes:
                gene = parent1_genes.get(key)
                if random() < 0.5:
                    gene = parent2_genes.get(key)

                genes.update({key: gene})

        return genes

    @staticmethod
    def get_disjoint_genes(fit_parent, weak_parent):
        fit_parent_genes = fit_parent.get_genes()
        weak_parent_genes = weak_parent.get_genes()

        n_weak_parent_min_innovation_number =\
            weak_parent.get_min_innovation_number()
        n_weak_parent_max_innovation_number =\
            weak_parent.get_max_innovation_number()

        genes = dict()

        for key in fit_parent_genes:
            if (n_weak_parent_min_innovation_number < key < n_weak_parent_max_innovation_number and
                    key not in weak_parent_genes):
                gene = fit_parent_genes.get(key)
                genes.update({key: gene})

        return genes

    @staticmethod
    def get_excess_genes(fit_parent, weak_parent):
        fit_parent_genes = fit_parent.get_genes()
        weak_parent_genes = weak_parent.get_genes()

        n_weak_parent_max_innovation_number =\
            weak_parent.get_max_innovation_number()

        genes = dict()

        for key in fit_parent_genes:
            if(key < n_weak_parent_max_innovation_number and
                    key not in weak_parent_genes):
                gene = fit_parent_genes.get(key)
                genes.update({key: gene})

    @staticmethod
    def join_genes(matching_genes,
                   disjoint_genes,
                   excess_genes):

        return_genes = matching_genes

        for key in disjoint_genes:
            disjoint_gene = disjoint_genes.get(key)
            return_genes.update({key: disjoint_gene})

        for key in excess_genes:
            excess_gene = excess_genes.get(key)
            return_genes.update({key: excess_gene})

        return return_genes
