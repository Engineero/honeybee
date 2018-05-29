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
        max_iter: maximum number of loops through the colonies fit function.
            Note that the objective function will be evaluated a number of
            times equal to::
            
                max_iter * (num_bees + num_scouts)
                
        num_scouts: number of additional bees in the colony that are solely
            responsible for exploring, i.e. the number of additional random
            guesses made at every iteration of the fit function.
            
    Properties:
        is_initialized: indicates whether the colony has been initialized and
            is ready to be fit.
        colony: list of Bee objects that make up the colony.
        food: list of food values for each bee in the colony.
    
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
    """ Defines a single bee in the colony.
    
    Args:
        objective: objective function called by each bee at each food source.
            Must return a "honey" value that will be maximized by the colony.
        position: initial food source location to test, i.e. initial guess
            for each bee in the colony.
            
    Properties:
        ref_position: reference position around which the bee is searching.
            When enough searches are complete around a given reference position
            without improving it, that reference position is abandoned.
        food: value of the objective function at position.

    """
    def __init__(self, objective, position=None):
        self.objective = objective
        self.position = position
        self.ref_position = position
        self.food = None  # objective function value at position

    def evaluate(self):
        self.food = self.objective(self.position)
