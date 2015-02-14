#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pylab import *

ent = arange(0., 20.1, .1)
sai = cos(ent) #map
plot(ent, sai)

xlabel('entrada')
ylabel('cosseno')
title('Cossenos')
grid(True)
show()

