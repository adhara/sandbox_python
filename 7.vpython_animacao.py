#!/usr/bin/env python
# -*- coding: utf-8 -*-

from visual import *

# Define posi��o inicial da c�mera
scene.forward = (-0.1, -0.1, -0.1)
# Limpa a ilumina��o default
scene.lights = []
# Define a ilumina��o ambiente
scene.ambient = (.1, .1, .2)


box(material=materials.wood)
sphere(radius=.2, pos=(-1, -0.3, 1), color=(.4, .5, .4), material=materials.rough, opacity=.5)
# A l�mpada � um frame composto por uma esfera e uma fonte de luz
c = (1., .9, .8)
lamp = frame(pos=(0, 1, 0))
local_light(frame=lamp, pos=(2, 0, 0), color=c)
sphere(frame=lamp, radius=0.1, pos=(2, 0, 0), color=c, material=materials.emissive)

while True:
# Anima a l�mpada, rotacionando em torno do eixo Y
    lamp.rotate(axis=(0, 1, 0), angle=.1)
    rate(5)