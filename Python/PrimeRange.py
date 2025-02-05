#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Challenge: Custom Iterable with Generators
#  Implement a class PrimeRange that behaves like range, but only returns prime numbers within the given range.
#
# for prime in PrimeRange(10, 50):
#     print(prime)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import math
def PrimeRange(low, high):
    for candidate in range(low, high):
        last = math.floor(math.sqrt(candidate))
        for divisor in range(2, last+1):
            if candidate % divisor == 0:
                break
            if divisor == last:
                yield candidate

for prime in PrimeRange(10, 50):
    print(prime)
