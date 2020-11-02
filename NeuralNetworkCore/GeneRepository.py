class CGeneRepository:
    def __init__(self):
        self._genes = dict()

    def __iter__(self):
        return iter(self._genes)

    def __next__(self):
        return next(self._genes)

    def __len__(self):
        return len(self._genes)

    def update(self, iterable):
        self._genes.update(iterable)

    def add(self, gene):
        n_innovation_number = gene.get_innovation_number()
        self.update({n_innovation_number:
                     gene})

    def find(self, gene):
        return self._genes.get(gene)

    def get(self, n_key):
        return self._genes.get(n_key)
