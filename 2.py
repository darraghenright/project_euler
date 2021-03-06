# Even Fibonacci numbers
# https://projecteuler.net/problem=2
#
# Each new term in the Fibonacci
# sequence is generated by adding
# the previous two terms. By starting
# with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the
# Fibonacci sequence whose values
# do not exceed four million, find
# the sum of the even-valued terms.


def fibonacci(terms=10):
    """
    >>> fibonacci(10)
    [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    """
    sequence = [1, 2]
    while len(sequence) < terms:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def sum_of_evens(sequence):
    """
    >>> sum_of_evens([1, 2])
    2
    >>> sum_of_evens([1, 2, 3, 5, 8])
    10
    """
    evens = [n for n in sequence if n % 2 == 0]
    return reduce(lambda x, y: x + y, evens)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
