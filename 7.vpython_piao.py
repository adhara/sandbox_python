#!/usr/bin/env python
# -*- coding: utf-8 -*-

from visual import *

azul = (.25, .25, .5)
verde = (.25, .5, .25)

# Caixa
box(pos=(0, -0.5, 0), color=azul, size=(10., .5, 8.))
box(pos=(0, -0.5, 4.), color=azul, size=(11., 1., 1.))
box(pos=(0, -0.5, -4.), color=azul, size=(11., 1., 1.))
box(pos=(5., -0.5, 0), color=azul, size=(1., 1., 8.))
box(pos=(-5., -0.5, 0), color=azul, size=(1., 1., 8.))
eixo = (0, 1, 0)
fr = frame(axis=eixo)

# Objeto a ser animado
py1 = pyramid(frame=fr, pos=(1, 0, 0), color=verde, axis=(1, 0, 0))
py2 = pyramid(frame=fr, pos=(1, 0, 0), color=verde, axis=(-1, 0, 0))

# Passo
delta_x = .01
delta_z = .01
while True:
    # Inverte o sentido em x
    if abs(fr.x) > 4.2:
        delta_x = -delta_x
    # Inverte o sentido em z
    if abs(fr.z) > 3.1:
        delta_z = -delta_z    
    fr.x += delta_x
    fr.z += delta_z
    # Rotaciona em Pi / 100 no eixo
    fr.rotate(angle=pi / 100, axis=eixo)
    # Controla a velocidade
    rate(1000)