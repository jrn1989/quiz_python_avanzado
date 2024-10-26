import numpy as np

def prime_sequence_generator(n):
    
    result = [is_prime(x,2) for x in list(range(1,n+1)) ]
    
    bool_array = np.array(result)
    
    true_indexes = (np.where(bool_array)[0]+1).tolist()
    
    return true_indexes
    
def is_prime(n, div):
    
    
    if n <= 1:
        return False
    
    if div * div > n:
        return True
    
    if n % div == 0:
        return False
    
    return is_prime(n, div+1)