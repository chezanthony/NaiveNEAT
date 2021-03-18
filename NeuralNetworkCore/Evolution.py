class CEvolution:

    @staticmethod
    def run_evolution(fitness_function,
                      networks,
                      n_iterations,
                      n_target_fitness):

        for nIteration in range(n_iterations):

            n_max_fitness = 0

            for network in networks.values():
                network.evaluate_fitness(fitness_function)
                n_current_fitness = network.get_fitness()

                if n_current_fitness > n_max_fitness:
                    n_max_fitness = n_current_fitness

            if n_iterations >= n_target_fitness:
                break
