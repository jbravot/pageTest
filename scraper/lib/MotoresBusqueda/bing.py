# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Bing
# Requires: Python >= 2.4
# Versions: 2.1 correccion de errores
# bing.py 2.1

# Import
from ..Coneccion.coneccion import Coneccion

class Bing:
    def __init__(self):
        #settings
        self.url = 'http://www.bing.com/search?mkt=en-US&q=site%3A'
        self.host = 'bing.com'
        # Variables tags HTML
        self.tag_result = "span"
        self.class_tag_result = "sb_count" #correcion 2015

        #valores
        self.paso = False
        self.valor = ''

    ########################################################################################
    ## Funcion que permite obtener el numero de paginas indexadas en el buscador bing.com ##
    ## Recive un string que indica el dominio al que se realizara la busqueda             ##
    ########################################################################################
    def getNumIndex (self, dominio):
        try:
            conn = Coneccion()
            html = conn.getHtml(dominio, self.host, self.url)

            tag_result_count = html.find(self.tag_result, attrs={'class':self.class_tag_result}) #correcion 2015
            bing_index = tag_result_count.text

            return bing_index.split(" ")[0]

        except:
            return '0'

    ########################################################################################
    ## Funcion que retorna si paso de la clase                                            ##
    ########################################################################################
    def getPaso (self):
        return self.paso
