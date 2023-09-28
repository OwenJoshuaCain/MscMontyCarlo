import numpy as np


def func(x,y):
    #The function is 1/(1+(sin(x)^2)+sin(y)^2)
    return 1 / (1 + np.power(np.sin(x),2) + np.power(np.sin(y),2) ) 

def func1(x,y):
    return x ** 2 + 3 * x * y - y ** 4

def montycarlo_integration(func, a, b, n=1000):
    #Monty Carlo Integration of the given function over the domain a to b for each parameter
    #Here the dimension is 2
    
    x_list = np.random.uniform(a, b, n)
    y_list = np.random.uniform(a, b, n)
    f = func(x_list,y_list)
    
    f_mean=np.sum(f) / len(f)
    domain = b-a
    
    integ = domain * f_mean
    
    return integ

#montycarlo_integration(func, 0, 1, n=1000)
montycarlo_integration(func1, 0, 1, n=999999)

def test_answer():
    assert  np.abs(montycarlo_integration(func1, 0, 1, n=999999)-53/60) <= 0.01

test_answer()