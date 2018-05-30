# Honeybee

An artificial bee colony implementation in Python

---
## Installation

To install with `pip`:

    pip install honeybee

---
## Usage

To use, first install the package as above, then define a function that you
wish to optimize. This can be a simple mathematical formula, or something that
calls a complicated model training routine. The important thing is that it
depends on hyperparameters that can be passed to the function, and returns a
fitness measure that will be maximized by the algorithm:

```python
def my_func(**params):
    """ Implements Rastrigin's function of two inputs. """
    x = [v for v in params.values()]
    return 20 + sum([a**2 - 10*cos(2*np.pi*a) for a in x])
```    

Next define the ranges of parameters over which you wish to optimize:

```python
params = {'x1': (-5.12, 5.12),
          'x2': (-5.12, 5.12)}
```          

Finally, initialize the colony and fit the objective function:

```python
my_colony = Colony(my_func, params, num_bees=10)
my_colony.fit()
```
