import numpy as np

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