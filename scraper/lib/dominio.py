# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Dominio
# Requires: Python >= 2.4
# Versions:
# dominio.py 2.0

# Import
import socket
from Coneccion.coneccion import Coneccion

class Dominio:
    def __init__(self):
        self.host_span = 'stopforumspam.com'
        self.url_span = 'http://www.stopforumspam.com/api?ip='

    ########################################################################################
    ## Funcion que permite obtener la ip de un dominio dado                               ##
    ## Recive un string que indica el dominio al que se realizara la busqueda             ##
    ########################################################################################
    def getIp (self, dominio):
        try:
            #validamos si paso o no
            self.paso = True
            return socket.gethostbyname(dominio)

        except:
            self.paso = False
            return 'N/N'

    ########################################################################################
    ## Funcion que permite saber si tiene activada la redireccion sin el www              ##
    ## Recive un string que indica el dominio al que se realizara la busqueda             ##
    ########################################################################################
    def getRedireccionWWW (self, dominio):

        try:
            conn = Coneccion()
            return conn.getRedireccionWWW(dominio)
        except:
            return False

    ########################################################################################
    ## Funcion que permite saber si un IP esta bloqueada por span                         ##
    ## http://www.stopforumspam.com/usage                                                 ##
    ########################################################################################
    def getSpan (self, ip):

        try:
            conn = Coneccion()
            html = conn.getHtml(ip, self.host_span, self.url_span)
            tag = html.find('appears')
            return  tag.text

        except:
            return 'No'