#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback

try:
    fn = raw_input('Nome do arquivo: ').strip()
    
    for i, s in enumerate(file(fn)):
        print i+1, s,

except:
    trace = traceback.format_exc()
    print 'Erro:'
    print trace
    file('trace.log', 'a').write(trace)
    raise SystemExit