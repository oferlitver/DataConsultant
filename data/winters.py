# -*- coding: utf-8 -*-
"""
Generation of Winters model data.
Model is:

d_t = (a+b*t)*c*d + epsilon
"""

__author__ = 'Ofer'

import numpy as np

# model parameters

class TimeSeriesData(object):

    def __init__(self, t=10, a=100, b=1, c=[0.9, 0.9, 0.9, 0.9, 1.1, 1.3, 1],
                 d=[1,1], sd=1):
        self.t = t
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.sd = sd


def generateData(t_tot, a, b, c, d=[1,1], sd):
    """

    :param t_tot: total number of time periods
    :param a: the intercept of the straight line
    :param b: the slope of the straight line
    :param c: list of length 7, describing the weekly demand multiplier
    :param d: FINISH THIS
    :param sd: standard deviation of the error
    :return:
    """
    newData = np.array([t_tot, len(d)])
    print newData

if __name__ == '__main__':
    generateData(20, 10, 0, [1,1,1,1,1.1,1.2,0.7], [1,1], 0)
