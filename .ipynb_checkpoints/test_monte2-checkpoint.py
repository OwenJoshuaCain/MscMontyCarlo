import monte_integration as mi
import numpy as np

def func1(x,y):
    return x ** 2 + 3 * x * y - y ** 4

def test_answer1():
    assert  np.abs(mi.montycarlo_integration(func1, 0, 1, n=999999)-53/60) <= 0.01