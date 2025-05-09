import numpy as np
from sklearn import datasets

N_SAMPLES = 1500

np.random.seed(0)

def circles():
    """Concentric circles

    Returns:
        ndarray (1500x2): data
    """

    data, _ = datasets.make_circles(n_samples=N_SAMPLES)
    return data

def moons():
    """Half-moons

    Returns:
        ndarray (1500x2): data
    """

    data, _ = datasets.make_circles(n_samples=N_SAMPLES)
    return data