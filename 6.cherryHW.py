#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import cherrypy

def greetings(horario=time.localtime()):

    hora = horario[3]
    min = horario[4]
        
    if 4 < hora <= 12:
        ret = 'Bom dia! '
    elif 12 < hora <= 18:
        ret = 'Boa tarde! '
    else:
        ret = 'Boa noite! '
    
    return ret + 'São %d:%d!'%(hora, min)


class Root(object):

    @cherrypy.expose
    def index(self):
        return greetings()

cherrypy.quickstart(Root())
