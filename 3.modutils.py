#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import sys
import glob

def find(txt):
    """encontra módulos que têm o nome contendo texto"""
    
    resp = []
    for path in sys.path:
        mods = glob.glob('%s/*.py' % path)
            if txt in os.path.basename(mod):
        for mod in mods:
                resp.append(mod)
                return resp

if __name__ == '__main__':
    print find('math')