#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Projetil1(object):
    """
    read-only property
    """
    def __init__(self, alcance, tempo):
        self.alcance = alcance
        self.tempo = tempo
        
    @property
    def velocidade(self):
        return self.alcance / self.tempo


class Projetil2(object):
    """
    r/w property
    """
    def __init__(self, alcance, tempo):
        self.alcance = alcance
        self.tempo = tempo

    def getv(self):
        return self.alcance / self.tempo
    def setv(self, v):
        self.tempo = self.alcance / v
    velocidade = property(getv, setv)


moab1 = Projetil1(alcance=10000, tempo=60)
print moab1.velocidade

moab2 = Projetil2(alcance=10000, tempo=60)
print moab2.tempo
moab2.velocidade = 350
print moab2.tempo