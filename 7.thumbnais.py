#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import Image
import ImageFilter

for fn in glob.glob("*.jpg"):
    # Retorna o nome do arquivo
    prename = glob.os.path.splitext(fn)[0]
    print 'Processando:', fn
    
    imagem = Image.open(fn)    
    # Cria thumbnail (miniatura) da imagem de tamanho 256x256 usando antialiasing
    imagem.thumbnail((256, 256), Image.ANTIALIAS)
    # Suaviza a imagem
    imagem = imagem.filter(ImageFilter.SMOOTH)
    # Salva como arquivo PNG
    imagem.save(prename + '.png', 'PNG')