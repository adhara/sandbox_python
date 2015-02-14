#!/usr/bin/env python
# -*- coding: utf-8 -*-

# chave = string com nome da banda; valor = lista com os álbuns da banda
progs = {
    'The Corrs': ['Home', 'Borrowed Heaven'],
    'Lighthouse Family': ['Whatever gets you through the day', 'Postcards from heaven'],
    'Vanessa-Mae': ['The violin player', 'Storm'],
    'Nenhuma': ['Nenhum']
}

# se existe, altera; se não existe, cria
progs['Josh Groban'] = ['Closer', 'Awake']
    
if progs.has_key('Nenhuma'):
    del progs['Nenhuma']

# Iteração
for prog, albuns in progs.items():
    print prog, '=>', albuns
    
#matriz esparsa
dim = 6, 12     #dimensões da matriz
mat = {}        #dicionário vazio
# Cada tupla representa uma posição na matriz
mat[3, 7] = 3
mat[4, 6] = 5
mat[0, 3] = 7
mat[5, 4] = 6
mat[2, 9] = 4
mat[1, 0] = 9
for lin in range(dim[0]):
    for col in range(dim[1]):        
        print mat.get((lin, col), 0), # get(chave, valor default) -> se a chave não existir, retorna valor default
    print
