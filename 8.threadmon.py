#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import threading

class Monitor(threading.Thread):
    def __init__(self, ip):
        self.ip = ip
        self.status = None
        threading.Thread.__init__(self)
        
    def run(self):
        ping = os.popen('ping -n 1 %s' % self.ip).read()
        if 'Esgotado' in ping:
            self.status = False
        else:
            self.status = True


if __name__ == '__main__':
    
    monitores = []
    for i in range(1, 10):
        ip = '10.10.10.%d' % i
        monitores.append(Monitor(ip))
    for monitor in monitores:
        monitor.start()
        
    ping = True
    while ping:
        ping = False
        for monitor in monitores:
            if monitor.status == None:
                ping = True
                break
                
        time.sleep(1) # Espera 1 segundo
    
    # Imprima os resultados no final
    for monitor in monitores:
        if monitor.status:
            print '%s no ar' % monitor.ip
        else:
            print '%s fora do ar' % monitor.ip