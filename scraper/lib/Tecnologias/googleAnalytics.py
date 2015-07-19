# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Google Analytics
# Requires: Python >= 2.4
# Versions:
# googleAnalytics.py 1.0

# Import
from ..Coneccion.coneccion import Coneccion

class GoogleAnalytics:
    def __init__(self):
        #valores
        self.paso = False

    ########################################################################################
    ## Funcion que permite saber si un dominio tiene instalado GoogleAnalytics            ##
    ## Recive un string que indica el dominio al que se realizara la validacion           ##
    ########################################################################################
    def getGoogleAnalytics (self, dominio):
        try:
            conn = Coneccion()
            html = conn.getHtmlByUrllib2(dominio)

            valor = str(html).find('google-analytics.com/ga.js');
            if valor != -1:
                return True
            else:
                return False

        except:
            return False