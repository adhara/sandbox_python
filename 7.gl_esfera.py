#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from OpenGL.GL import *
from OpenGL.GLUT import *


def display():
    """
    Fun��o callback que desenha na janela
    """
    # glClear limpa a janela com valores pr�-determinados
    # GL_COLOR_BUFFER_BIT define que o buffer aceita escrita
    # GL_DEPTH_BUFFER_BIT define que o buffer ser� usado
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    
    rgba = [.8, .6, .4, .9]
    # glMaterial especifica os par�metros do material usado no modelo de ilumina��o da cena (no formato RGBA)
    # GL_FRONT define que a face afetada pela fun��o � a frontal
    # GL_AMBIENT especifica que o par�metro � a reflex�o de ambiente
    glMaterialfv(GL_FRONT, GL_AMBIENT, rgba)
    # GL_DIFFUSE especifica que o par�metro � a reflex�o difusa do material
    glMaterialfv(GL_FRONT, GL_DIFFUSE, rgba)
    # GL_SPECULAR especifica que o par�metro � a reflex�o especular
    glMaterialfv(GL_FRONT, GL_SPECULAR, rgba)    
    # GL_EMISSION especifica que o par�metro � a emiss�o do material
    # glMaterialfv(GL_FRONT, GL_EMISSION, rgba)
    # GL_SHININESS especifica o expoente usado pela reflex�o especular
    glMaterialfv(GL_FRONT, GL_SHININESS, 120)
    # Desenha uma esfera s�lida, com raio 0.5 e 128 divis�es na horizontal e na vertical
    glutSolidSphere(0.5, 128, 128)    
    # For�a a execu��o dos comandos da OpenGL
    glFlush()

    # Inicializa a biblioteca GLUT
    glutInit(argv)
    # glutInitDisplayMode configura o modo de exibi��o
    # GLUT_SINGLE define o buffer como simples
    # (tamb�m pode ser duplo, com GLUT_DOUBLE)
    # GLUT_RGB seleciona o modo RGB
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    # Cria a janela principal
    glutCreateWindow('Esfera')
    # Configura a fun��o callback que desenha na janela atual
    glutDisplayFunc(display)    
    # Limpa a janela com a cor especificada
    glClearColor(.25, .15, .1, 1.)
    # Muda a matriz corrente para GL_PROJECTION
    glMatrixMode(GL_PROJECTION)
    # Carrega uma matriz identidade na matriz corrente
    glLoadIdentity()
    # Configurando os par�metros para as fontes de luz
    # GL_DIFFUSE define o par�metro usado para luz difusa (no formato RGBA)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1., 1., 1., 1.])
    # Os tr�s par�metros definem a posi��o da fonte luminosa
    # O quarto define se a fonte � direcional (0) ou posicional (1)
    glLightfv(GL_LIGHT0, GL_POSITION, [-5., 5., -5., 1.])
    # Aplica os par�metros de ilumina��o
    glEnable(GL_LIGHTING)
    # Inclui a fonte de luz 0 no calculo da ilumina��o
    glEnable(GL_LIGHT0)
    
    # Inicia o la�o de eventos da GLUT
    glutMainLoop()