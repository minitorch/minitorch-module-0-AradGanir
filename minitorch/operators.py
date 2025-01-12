"""Collection of the core mathematical operators used throughout the code base."""

import math
from typing import Callable, Iterable


# ## Task 0.1


#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.
def mul(x, y):
    """multiply.

    Args:
    ----
        x (int): The first argument.
        y (int): The second argument.

    Returns:
    -------
        int: The result of multiplying x and y.

    """
    return x * y


def id(x):
    """Returns argument x"""
    return x


def add(x, y):
    """Adds two arguments, x, y, returns x+y"""
    return x + y


def sub(x, y):
    """Subtracts two arguments, x, y, returns x-y"""
    return x - y


def neg(x):
    """Negates argument, returns -x"""
    return -x


def lt(x, y):
    """Returns True if x is less than y, returns False otherwise."""
    return x < y


def eq(x, y):
    """Returns True if x is equal to y, returns False otherwise."""
    return x == y


def max(x, y):
    """Returns the maximum value of x and y."""
    return x if x > y else y


def is_close(input, other):
    """Takes input, other, and returns true if input is within .01 of others."""
    return abs(input - other) <= 1e-2


def sigmoid(x):
    """Implements sigmoid function symmetrically"""
    if x >= 0:
        return 1 / (1 + math.exp(-x))
    else:
        return math.exp(x) / (1 + math.exp(x))


def relu(x):
    """Implements the relu function"""
    return max(0, x)


def log(x):
    """Renames the math.log function"""
    return math.log(x)


def exp(x):
    """Renames the mathexp function"""
    return math.exp(x)


def inv(x):
    """Returns reciprocal"""
    return 1 / x


def log_back(a, b):
    """Returns the derivative of a function 'a', and multiplies by value of b"""
    return b * inv(a)


def inv_back(a, b):
    return -b * (inv(a) ** 2)


def relu_back(a, b):
    """Returns the value of the derivative of relu multiplied by b.
    If over 0, returns b otherwise returns 0
    """
    if a > 0:
        return b
    else:
        return 0


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
def map(fn: Callable[[float], float], a: Iterable[float]) -> Iterable[float]:
    return [fn(i) for i in a]


def zipWith(
    fn: Callable[[float, float], float], a: Iterable[float], b: Iterable[float]
) -> Iterable[float]:
    return [fn(a, b) for a, b in zip(a, b)]


def reduce(fn: Callable[[float, float], float], values: Iterable[float]) -> float:
    result = values[0]
    for value in values[1:]:
        result = fn(result, value)
    return result


def negList(ls):
    return map(neg, ls)


def addLists(l1, l2):
    if l1 is None or l2 is None:
        return l1, l2
    else:
        return zipWith(add, l1, l2)


def sum(x):
    if not x:
        return 0
    elif len(x) == 1:
        return x[0]
    else:
        return reduce(add, x)


def prod(x):
    if not x:
        return 0
    elif len(x) == 1:
        return x[0]
    else:
        return reduce(mul, x)
