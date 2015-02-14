#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mpl_toolkits.basemap import Basemap
from matplotlib import pyplot
from numpy import arange

# Cria um mapa usando Basemap
mapa = Basemap(projection='robin', lat_0=-0, lon_0=0,
resolution='l', area_thresh=1e3)

# desenha a costa dos continentes
mapa.drawcoastlines(color='#777799')
# Desenha as fronteiras
mapa.drawcountries(color='#ccccee')
# Pinta os continentes
mapa.fillcontinents(color='#ddddcc')

# Desenha os meridianos
mapa.drawmeridians(arange(0, 360, 30), color='#ccccee')
# Desenha os paralelos
mapa.drawparallels(arange(-180, 180, 30), color='#ccccee')
# Desenha os limites do mapa
mapa.drawmapboundary()
# Salva a imagem
pyplot.show()