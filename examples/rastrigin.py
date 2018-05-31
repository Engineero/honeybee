""" Attempts to find the minimum of Rastrigin's function with ABC. """

import numpy as np
from honeybee import Colony


# Define the objective function.
def rastrigin_fcn(**params):
    """ Implements Rastrigin's function of two inputs. """
    x = [v for v in params.values()]
    return 20 + sum([a**2 - 10*cos(2*np.pi*a) for a in x])


if __name__ == '__main__':
    # Define the parameter bounds.
    params = {'x1': (-5.12, 5.12),
              'x2': (-5.12, 5.12)}
    # Optimize the objective function.
    my_colony = Colony(my_func, params, num_bees=10)
    my_colony.fit(verbose=True)
