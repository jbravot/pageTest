# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Yahoo!
# Requires: Python >= 2.4
# Versions:
# yahoo.py 2.0

# Import
from ..Coneccion.coneccion import Coneccion

class Yahoo:
    def __init__(self):
        #settings
        self.url = 'http://search.yahoo.com/search?q=site%3A'
        self.host = 'search.yahoo.com'
        # Variables tags HTML

        #valores
        self.paso = False
        self.valor = ''

    ########################################################################################
    ## Funcion que permite obtener el numero de paginas indexadas en yahoo.com            ##
    ## Recive un string que indica el dominio al que se realizara la busqueda             ##
    ########################################################################################
    def getNumIndex (self, dominio):
        try:
            conn = Coneccion()
            html = conn.getHtml(dominio, self.host, self.url)
            html = html.find('div', attrs={'class': 'compPagination'}) #correcion 2015
            yahoo_index = html.find('span') #correcion 2015

            return yahoo_index.text.split(" ")[0]

        except:
            return '0'

    ########################################################################################
    ## Funcion que retorna si paso de la clase                                            ##
    ########################################################################################
    def getPaso (self):
        return self.paso
