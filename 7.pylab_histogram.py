#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pylab import *
# Dados
x = randn(10000000)
# Histograma (150 faixas)
hist(x, 150, color='b')
show()