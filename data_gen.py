# Here we define some functions to be used to generate data, and modelled  by the other regression models.
import numpy as np

def noise(size, variance):
    return np.random.normal(scale=np.sqrt(variance), size=size)

def data(X, noise_variance):
    """Sinus function plus noise"""
    return 0.5 + np.sin(2 * np.pi * X) + noise(X.shape, noise_variance)