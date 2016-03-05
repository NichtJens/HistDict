#!/usr/bin/env python

from __future__ import division
from math import sqrt
from collections import defaultdict


class HistDict(defaultdict):

    def __init__(self):
        super(HistDict, self).__init__(int)


    def fill(self, value, weight=1):
        self[value] += weight

    def remove(self, value, weight=1):
        self[value] -= weight

    def reset(self, value, content=0):
        self[value] = content


    def scale(self, factor):
        for k in self.keys():
            self[k] *= factor

    def normalize(self):
        c = self.count
        if c:
            self.scale(1/c)


    @property
    def x(self):
        return sorted(self.keys())

    @property
    def y(self):
        return [self[x] for x in self.x]

    @property
    def xy(self):
        return zip(*sorted(self.items()))


    @property
    def integral(self):
        return sum(y*x for x, y in self.items())

    @property
    def count(self):
        return sum(self.values())

    @property
    def mean(self):
        c = self.count
        if not c: return None
        return self.integral / c

    @property
    def variance(self):
        c = self.count
        if not c: return 0
        m = self.mean
        s = sum(y * (x - m)**2 for x, y in self.items())
        return s/c

    @property
    def stddev(self):
        return sqrt(self.variance)

    sigma = stddev

    @property
    def RMS(self):
        c = self.count
        if not c: return None
        s = sum(y * x**2 for x, y in self.items())
        return sqrt(s/c)





#TODO
#rebin?
#multipy, extend, merge 2 hists
#skewness, kurtosis, ...
#bin of max
#fft



