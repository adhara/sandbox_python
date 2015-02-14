#!/usr/bin/env python
# -*- coding: utf-8 -*-

class String(str):
    """
    Adicionando capacidade de subtra��o para string (remover uma substring)
    """
    def __sub__(self, s):
        return self.replace(s, '')


s1 = String('Juliana Cavalcanti Correa')
s2 = 'Cavalcanti '
print '"%s" - "%s" = "%s"' % (s1, s2, s1 - s2)