from Values import *
import math


def add(val1, val2):
    return simple('+', val1, val2)


def subtract(val1, val2):
    return simple('-', val1, val2)


def multiply(val1, val2):
    actual = val1.actual * val2.actual
    # absolute = abs(val1.actual * val2.absolute_unc) + \
    #     abs(val2.actual * val1.absolute_unc)
    absolute = abs(actual) * (val1.percent_unc + val2.percent_unc)
    return Values(actual, absolute)


def divide(val1, val2):
    actual = val1.actual / val2.actual
    absolute = abs(actual) * (val1.percent_unc + val2.percent_unc)
    return Values(actual, absolute)


def simple(oper, val1, val2):
    actual = eval(str(val1.actual) + oper + str(val2.actual))
    absolute_unc = abs(val1.absolute_unc + val2.absolute_unc)
    return Values(actual, absolute_unc)


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
