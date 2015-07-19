# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Social twitter
# Requires: Python >= 2.4
# Versions:
# twitter.py 2.0

# Import
from ..Coneccion.coneccion import Coneccion
import simplejson as json
# Twitter
class Twitter:
    def __init__(self):
        #settings
        self.url = 'http://urls.api.twitter.com/1/urls/count.json?url=www.'
        self.host = 'urls.api.twitter.com'

    ########################################################################################
    ## Funcion que permite obtener el numero de backlinks de Twitter                      ##
    ## Recive un string que indica el dominio al que se realizara la busqueda             ##
    ########################################################################################
    def getBacklinks (self, dominio):
        try:
            conn = Coneccion()
            html = conn.getHtml(dominio, self.host, self.url)

            json_t = json.loads(str(html))

            #validamos si paso o no
            self.paso = True

            return str(json_t["count"])

        except:
            return 'Error'