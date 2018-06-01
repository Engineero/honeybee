""" Classes to implement the artificial bee colony algorithm. """

from numpy.random import uniform

class Colony:
    """ Implements the artificial bee colony algorithm.
    
    Args:
        objective: objective function called by each bee at each food source.
            Must return a "honey" value that will be maximized by the colony.
        params: dictionary of optimization parameters and their ranges::

            params = {'param_1': (min, max),
                      'param_2': (min, max),
                      ...,
                      'param_n': (min, max)}

    Keyword Args:
        num_bees: number of employed bees in the colony, i.e. number of
            solutions searched at each iteration of the algorithm.
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

    Raises:
        TypeError: if objective is not callable.
        TypeError: if params is not a dictionary.
        TypeError: if any entry in params is not a range or callable.
    
    """
    def __init__(self, objective, params: dict, num_bees: int = 10,
                 limit: int = 5, max_iter: int = 1000, num_scouts: int = 1):
        """ Initialize the colony. """
        if not callable(objective):
            raise TypeError('objective must be callable!')
        if not isinstance(params, dict):
            msg = 'params argument must be a dictionary of parameters and '\
                  + 'ranges or callable distributions!'
            raise TypeError(msg)
        for key in params.keys():
            if not isinstance(params[key], tuple):
                if not callable(params[key]):
                    msg = f'params[{key}] must be a range or callable!'
                    raise TypeError(msg)
        self.objective = objective
        self.num_bees = num_bees
        self.params = params
        self.limit = limit
        self.max_iter = max_iter
        self.num_scouts = num_scouts
        self.is_initialized = False
        self.colony = [_Bee(self.objective) for b in range(self.num_bees + self.num_scouts)]
        self.food = [0.] * len(self.colony)
        self.chosen = False * len(self.colony)

    def fit(self, verbose: bool = False):
        """ Maximizes the objective function using the bee colony.
        
        Keyword Args:
            verbose: if true, output periodic updates about the fitting process.
                Default is False.
        
        """
        if not self.is_initialized:
            self.initialize()
        for _ in range(self.max_iter):
            for bee in self.colony:
                bee.evaluate()
            self.food = [bee.food for bee in self.colony]
            # TODO (ENG): pick where the bees go next based on food values.
            self._choose_food
            self._perturb_params

            # Send scouts to random locations always.
            for bee in self.colony[-self.num_scouts:]:
                bee.goto(self._draw_params)

    def initialize(self):
        """ Initializes the colony with first guesses for all bees. """
        for bee in self.colony:
            bee.goto(self._draw_params)
        self.is_initialized = True

    def _draw_params(self):
        """ Makes a random draw of parameters. """
        draw = {}
        for k, v in params.items():
            if isinstance(v, tuple):
                draw[k] = uniform(*v)  # uniform for ranges
            elif callable(v):
                draw[k] = v()  # call function for provided distributions
        return draw

    def _choose_food(self):
        """ Chooses which food sources to keep or abandon. """
        pass

    def _perturb_params(self):
        """ Perturbs param values for selected food sources. """
        pass


# Maybe this should be a sub-class of Colony?
class _Bee:
    """ Defines a single bee in the colony.
    
    Args:
        objective: objective function called by each bee at each food source.
            Must return a "honey" value that will be maximized by the colony.
        position: dicationary of parameter/value pairs defining the initial
            food source location to test, i.e. initial guess for each bee in
            the colony.
            
    Properties:
        food: value of the objective function at position.

    """
    def __init__(self, objective, position: dict = None):
        self.objective = objective
        self.position = position
        self.food = None  # objective function value at position

    def evaluate(self):
        """ Evaluate the objective function at the given position.

        TODO:
            - Spawn a new process for each bee.
            - Spawn processes intelligently for bees.

        """
        self.food = self.objective(self.position)

    def goto(self, params: dict):
        """ Tells the bee where to go next.

        Args:
            params: dictionary of key, value pairs, where each key is a
                parameter of the objective function, and each value is a
                concrete value that the parameter takes.

        """
        self.position = params
