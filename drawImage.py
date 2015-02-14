#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Image
import ImageDraw

wd, ht = 512, 512

# Cria uma imagem nova com fundo branco
imagem = Image.new('RGBA', (wd, ht), 'white')
# O objeto desenho age sobre o objeto imagem
desenho = ImageDraw.Draw(imagem)
# Calcula a largura da faixa de cor
faixa = wd / 256
# Desenha o gradiente de cor
for i in xrange(0, wd):
    rgb = (30, i / 3, 192 - i / 3)
    cor = '#%02x%02x%02x' % rgb
    desenho.line((0, i, wd, i), fill=cor)

# Copia e cola recortes invertidos do gradiente
for i in xrange(wd, wd / 2, -wd / 10):
    # Tamanho do recorte
    area = (wd - i, ht - i, i, i)
    # Copia e inverte
    flip = Image.FLIP_TOP_BOTTOM
    recorte = imagem.crop(area).transpose(flip)
    # Cola de volta na imagem original
    imagem.paste(recorte, area)
    # Salva como arquivo PNG
    
imagem.save('desenho.png', 'PNG')