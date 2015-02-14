#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pylab import *

pie (x=[2, 4, 7], explode=(0, 0.03, 0), labels=['x', 'y', 'z'], shadow=True)
title('Olha que coisa bonita', bbox={'facecolor':'0.8', 'pad':7})
show()