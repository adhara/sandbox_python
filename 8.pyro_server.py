#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Pyro.core

class Calcula(Pyro.core.ObjBase):
    
    def calc(self, n):
        return n**n

class Fala(Pyro.core.ObjBase):
    
    def recebi(self):
        print 'oi!'
        return 'oi tb!'


    
if __name__ == '__main__':
    # Inicia a thread do servidor
    Pyro.core.initServer()
    # Cria o servidor
    daemon = Pyro.core.Daemon()
    # Publica o objeto
    uri = daemon.connect(Fala(),'fala')
    uri = daemon.connect(Calcula(),'calcula')
    # Coloca o servidor em estado operacional
    daemon.requestLoop()