#!/usr/bin/env python
# -*- coding: utf-8 -*-

from visual import *
from visual.controls import *

# Janelas
display(x=0, y=0, width=400, height=800, range=60, center=(0, 10, 0))
c = controls(x=400, y=0, width=400, height=800, range=60, title='Controles')

# Objetos
bola = sphere(pos=(0, 50, 0), radius=5, color=(.5, .4, .3))
solo = box(pos=(0, -30, 0), size=(30, 1, 30), color=(.2, .3, .4))
bola.vel = vector(0.,-0.1, 0.)
bola.val = 1

#evita o autoscale
scene.autoscale = 0

# Slider
def recupera(i):
    bola.val=i
    
s = slider(pos=(-20, -50), width=5, length=100, axis=(0, 1, 0), min=0, max=1, action=lambda: recupera(s.value))
s.value = 1

# Button
def reinicia():
    bola.pos.y = 50.
    bola.vel.y = 0.
    
b = button(pos=(10, 0), width=25, height=20, text='Reiniciar', action=lambda: reinicia())

while True:
    rate(100)
    #Verifica eventos
    c.interact()
    bola.pos = bola.pos + bola.vel / 10
    if bola.pos.y < bola.radius + solo.y:
        bola.pos.y = bola.radius + solo.y
        bola.vel.y = -bola.vel.y * bola.val
    else:
        bola.vel.y = bola.vel.y - .98