import random


class CMutationRandomizer:

    @staticmethod
    def randomize_element(container,
                          n_except=-1):
        n_key = n_except

        while n_key == n_except:
            n_key = random.choice(list(container.keys()))

        return container.get(n_key)

    @staticmethod
    def randomize_value():
        return random.random()

    @staticmethod
    def is_mutation_successful(n_probability):
        n_mutation = random.random()
        return n_probability > n_mutation
