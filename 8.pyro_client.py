#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Pyro.core

# Cria um objeto local para acessar o objeto remoto
proxy = Pyro.core.getProxyForURI('PYROLOC://127.0.0.1/fala')

# Evoca um método do objeto remoto
print proxy.recebi()

proxy = Pyro.core.getProxyForURI('PYROLOC://127.0.0.1/calcula')

print proxy.calc(3)