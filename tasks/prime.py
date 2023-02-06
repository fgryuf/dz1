__all__ = (
    'is_prime',
)
from math import sqrt

def is_prime(number: int) -> bool:
    prime = True
    for i in range(int(sqrt(number) + 1)) :
        if number % i == 0 :
            prime = False
    return prime
