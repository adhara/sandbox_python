# -*- coding: latin1 -*-

import cProfile

def rgb1():
    """Função usando range()"""
    rgbs = []
    for r in range(256):
        for g in range(256):
            for b in range(256):
                rgbs.append('#%02x%02x%02x' % (r, g, b))
    return rgbs
    
def rgb2():
    """Função usando xrange()"""
    rgbs = []
    for r in xrange(256):
        for g in xrange(256):
            for b in xrange(256):
                rgbs.append('#%02x%02x%02x' % (r, g, b))
    return rgbs

def rgb3():
    """Gerador usando xrange()"""
    for r in xrange(256):
        for g in xrange(256):
            for b in xrange(256):
                yield '#%02x%02x%02x' % (r, g, b)
                
def rgb4():
    """ List comprehension usando xrange"""
    return ['#%06x' % r for r in xrange(256*256*256)]
        
#print 'rgb1:'
#cProfile.run('rgb1()')
#print 'rgb2:'
#cProfile.run('rgb2()')
#print 'rgb3:'
#cProfile.run('list(rgb3())')
print 'rgb4:'
cProfile.run('list(rgb4())')