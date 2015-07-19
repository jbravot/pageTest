# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Social Google
# Requires: Python >= 2.4
# Versions:
# googlePlus.py 2.0

# Import
from ..Coneccion.coneccion import Coneccion

# Google
class GooglePlus:
    def __init__(self):
        #settings
        self.url = 'https://plusone.google.com/u/0/_/+1/fastbutton?count=true&url=http%3A%2F%2Fwww.'
        self.host = 'plusone.google.com'
        self.id_div_g = 'aggregateCount'
        self.tag_g = 'div'

    ########################################################################################
    ## Funcion que permite obtener el numero de Plus One de Google+                       ##
    ## Recive un string que indica el dominio al que se realizara la busqueda             ##
    ########################################################################################
    def getPlusOne (self, dominio):
        try:
            conn = Coneccion()
            html = conn.getHtmlByHttps(dominio, self.host, self.url)

            plus_one = html.find(self.tag_g, attrs={'id':self.id_div_g})

            #validamos si paso o no
            self.paso = True

            return plus_one.text

        except:
            return 'Error'