#!/usr/bin/env python
# -*- coding: utf-8 -*-

from visual.graph import *

# Gráfico de linha simples
g1 = gcurve(color=(.8, .6, .3))
# Gráfico de barras
g2 = gvbars(delta=0.02, color=(.6, .4, .6))

# Limites do eixo X do gráfico
for x in arange(0., 10.1, .1):

    g1.plot(pos=(x, 3 * sin(x) + cos(5 * x)))
    g2.plot(pos=(x, tan(x) * sin(4 * x)))