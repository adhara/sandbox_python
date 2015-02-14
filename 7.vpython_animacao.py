#!/usr/bin/env python
# -*- coding: utf-8 -*-

from visual import *

# Define posição inicial da câmera
scene.forward = (-0.1, -0.1, -0.1)
# Limpa a iluminação default
scene.lights = []
# Define a iluminação ambiente
scene.ambient = (.1, .1, .2)


box(material=materials.wood)
sphere(radius=.2, pos=(-1, -0.3, 1), color=(.4, .5, .4), material=materials.rough, opacity=.5)
# A lâmpada é um frame composto por uma esfera e uma fonte de luz
c = (1., .9, .8)
lamp = frame(pos=(0, 1, 0))
local_light(frame=lamp, pos=(2, 0, 0), color=c)
sphere(frame=lamp, radius=0.1, pos=(2, 0, 0), color=c, material=materials.emissive)

while True:
# Anima a lâmpada, rotacionando em torno do eixo Y
    lamp.rotate(axis=(0, 1, 0), angle=.1)
    rate(5)