""" Classes to implement the artificial bee colony algorithm. """


class Colony:
    """ Implements the artificial bee colony algorithm.
    
    Args:
        objective: objective function called by each bee at each food source.
            Must return a "honey" value that will be maximized by the colony.
        num_bees: number of employed bees in the colony, i.e. number of
            solutions searched at each iteration of the algorithm.
        params: dictionary of optimization parameters and their ranges::

            params = {'param_1': (min, max),
                      'param_2': (min, max),
                      ...,
                      'param_n': (min, max)}
                      
        limit: number of trails without improvement at a food source before it
            is "depleted" and the colony moves on to new food sources.
    
    """
    def __init__(self, objective, num_bees: int, params: dict, limit: int = 5,
                 max_iter: int = 1000, num_scouts: int = 1):
        """ Initialize the colony. """
        self.objective = objective
        self.num_bees = num_bees
        self.params = params
        self.limit = limit
        self.max_iter = max_iter
        self.num_scouts = 1
        self.is_initialized = False
        self.colony = [_Bee(self.objective) for b in range(self.num_bees + self.num_scouts)]
        self.food = [0.] * len(self.colony)

    def fit(self):
        for _ in range(self.max_iter):
            for bee in self.colony:
                bee.evaluate()
            self.food = [bee.food for bee in colony]

    def initialize(self):
        self.is_initialized = True


# Maybe this should be a sub-class of Colony?
class _Bee:
    """ Defines a single bee in the colony. """
    def __init__(self, objective, position=None):
        self.objective = objective
        self.position = position
        self.food = None  # objective function value at position

    def evaluate(self):
        self.food = self.objective(self.position)
