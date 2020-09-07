

class CInnovationNumber:
    def __init__(self, gene_repository):
        self._n_Innovation_Number = 0
        self._gene_Repository = gene_repository

    def get_innovation_number(self):
        self._n_Innovation_Number += 1
        return self._n_Innovation_Number

    def get_node_innovation_number(self,
                                   node_type,
                                   activation_function_type):
        n_return = -1

        for n_key in self._gene_Repository:
            gene = self._gene_Repository.get(n_key)
            if(gene.is_node() and
               gene.get_node_type() == node_type and
               gene.get_activation_function_type == activation_function_type):
                n_return = gene.get_innovation_number()

        if -1 == n_return:
            self._n_Innovation_Number += 1
            n_return = self._n_Innovation_Number

        return n_return

    def get_connection_innovation_number(self,
                                         n_input_node,
                                         n_output_node):
        n_return = -1

        for n_key in self._gene_Repository:
            gene = self._gene_Repository.get(n_key)
            if(not gene.is_node and
               gene.get_input_node() == n_input_node and
               gene.get_output_node() == n_output_node):
                n_return = gene.get_innovation_number()

        if -1 == n_return:
            self._n_Innovation_Number += 1
            n_return = self._n_Innovation_Number

        return n_return
