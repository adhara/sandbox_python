#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path
import pickle

setupfile = 'data/setup.pkl'

if not os.path.exists(setupfile):
    setup = {
        'timeout': 10,
        'server': '10.0.0.1',
        'port': 80 
    }
    pickle.dump(setup, file(setupfile, 'w'))

setup = pickle.load(file(setupfile, 'r'))

print setup
