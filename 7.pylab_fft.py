#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pylab import *

a = zeros(1000)
a[:100] = 1
b = fft(a)
plot(b)
show()