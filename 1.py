# Multiples of 3 and 5
#
# https://projecteuler.net/problem=1
#
# If we list all the natural numbers
# below 10 that are multiples of 3 or
# 5, we get 3, 5, 6 and 9.
#
# The sum of these multiples is 23.
#
# Find the sum of all the multiples
# of 3 or 5 below 1000.


def sum_of_multiples(limit, r1=3, r2=5):
    """
    >>> sum_of_multiples(10)
    23
    >>> sum_of_multiples(1000)
    233168
    """
    return reduce(lambda x, y: x + y,
                  set(range(0, limit, r1)).union(range(0, limit, r2)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print sum_of_multiples(1000)
