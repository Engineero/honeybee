""" Classes to implement the artificial bee colony algorithm. """


class Colony:
    """ Implements the artificial bee colony algorithm.
    
    Args:
        objective: objective function called by each bee at each food source.
            Must return a "honey" value that will be maximized by the colony.
        num_bees: number of employed bees in the colony, i.e. number of
            solutions searched at each iteration of the algorithm.
    
    """
    def __init__(self, objective, num_bees):
        """ Initialize the colony. """
        self.objective = objective
        self.num_bees = num_bees

    def fit(self):
        pass


# Maybe this should be a sub-class of Colony?
class _Bee:
    """ Defines a single bee in the colony. """
    def __init__(self):
        pass

