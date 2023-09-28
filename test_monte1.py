import numpy as np
import monte_integration as mi

def func(x,y):
    #The function is 1/(1+(sin(x)^2)+sin(y)^2)
    return 1 / (1 + np.power(np.sin(x),2) + np.power(np.sin(y),2) ) 

def test_answer():
    assert  np.abs(mi.montycarlo_integration(func, 0, 1, n=999999)-0.67) <= 0.01