from Values import *
import math


def add(val1, val2):
    actual = val1.actual + val2.actual
    absolute = val1.absolute_unc + val2.absolute_unc
    return Values(actual, absolute)


def subtract(val1, val2):
    actual = val1.actual - val2.actual
    absolute = val1.absolute_unc + val2.absolute_unc
    return Values(actual, absolute)


def multiply(val1, val2):
    # dz = (dx*y+dy*x)s
    actual = val1.actual * val2.actual
    absolute = abs(val1.absolute_unc * val2.actual) + \
        abs(val2.absolute_unc * val1.actual)
    return Values(actual, absolute)


def divide(val1, val2):
    if val2.actual != 0:
        actual = val1.actual / val2.actual
        absolute = abs(val1.absolute_unc / val2.actual) + \
            abs(val2.absolute_unc * val1.actual / pow(val2.actual, 2))
        return Values(actual, absolute)
    else:
        print("trying to divide by zero! " + "Values 1: " +
              val1.output_self() + "Values 2: " + val2.output_self())
        return "Failure to divide by zero. Please see console."


def power(val1, n):
    actual = pow(val1.actual, n)
    uncertainty = n * val1.absolute_unc
    return Values(actual, uncertainty)


def scale(val1, amount):
    actual = amount * val1.actual
    absolute_unc = amount * val1.absolute_unc
    return Values(actual, absolute_unc)


def average(val1, val2):
    return scale(add(val1, val2), 0.5)
