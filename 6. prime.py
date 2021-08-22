"""
Optimized solution for prime
"""
def is_prime(num):
    import math

    # There's only one even prime: 2
    if num < 2    : return False
    if num == 2   : return True
    if num %2 == 0: return False

    
    """
    Property:
        Every number n that is not prime has at least one prime divisor p
        such 1 < p < square_root(n)
    """
    root = int(math.sqrt(num))
    
    # We know there's only one even prime, so with that in mind 
    # we're going to iterate only over the odd numbers plus using the above property
    # the performance will be improved
    for i in xrange(3, root+1, 2):
        if num % i == 0: return False

    return True

""" 
from math import sqrt
def is_prime(num):

    if num>1:
        for n in range(2, int(sqrt(num))+1):
            if num%n == 0:
                return False
    else:
        return False
    return True

"""