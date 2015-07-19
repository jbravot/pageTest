# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Google
# Requires: Python >= 2.4
# Versions:
# google.py 2.0

# Import
from ..Coneccion.coneccion import Coneccion
import simplejson as json

# paginas populares
# http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=site:espol.edu.ec
#
# sitios web relacionados
# http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=related:espol.edu.ec
#
# numero de backlinks
# http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=%22espol.edu.ec%22-site:espol.edu.ec
# estimatedResultCount

class Google:
    def __init__(self):
        #settings
        self.url_search = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q='
        self.host_search = 'ajax.googleapis.com'
        self.pr_url='/tbr?client=navclient-auto&ch=%s&features=Rank&q=info:%s'
        self.pr_host='toolbarqueries.google.com'

        #valores
        self.paso = False
        self.valor = ''

    ########################################################################################
    ## Funcion que devuelve un Hash para obtener el Page Rank                             ##
    ## Recive un string que indica el dominio al que se realizara la busqueda             ##
    ## Retorna el Hash                                                                    ##
    ########################################################################################
    @staticmethod
    def getHash (dominio):

        SEED = "Mining PageRank is AGAINST GOOGLE'S TERMS OF SERVICE. Yes, I'm talking to you, scammer."
        Result = 0x01020345

        for i in range(len(dominio)) :
            Result ^= ord(SEED[i%len(SEED)]) ^ ord(dominio[i])
            Result = Result >> 23 | Result << 9
            Result &= 0xffffffff

        return '8%x' % Result

    ########################################################################################
    ## Funcion que permite obtener el Page Rank                                           ##
    ## Recive un string que indica el dominio al que se realizara la busqueda             ##
    ## Retorna el Page Rank                                                               ##
    ########################################################################################
    def getPageRank (self, dominio):

        try:
            data = {'pr':'N/N'}
            hash = Google.getHash(dominio)
            path = self.pr_url % (hash,dominio)

            conn = Coneccion()
            html = conn.getPRConeccion(dominio, self.pr_host, path)

            data['pr'] = int(html.split(":")[-1])
            return data

        except:
            return data

    ########################################################################################
    ## Funcion que permite obtener el numero de paginas indexadas en el buscador Google   ##
    ## Recive un string que indica el dominio al que se realizara la busqueda             ##
    ########################################################################################
    def getNumIndex (self, dominio):
        try:
            conn = Coneccion()
            html = conn.getHtml(dominio, self.host_search, self.url_search + 'site:')
            data = json.loads(str(html))
            return data['responseData']['cursor']['estimatedResultCount']

        except:
            return '0'

    ########################################################################################
    ## Funcion que permite obtener el numero de backlikns de un dominio en el             ##
    ## buscador Google                                                                    ##
    ## Recive un string que indica el dominio al que se realizara la busqueda             ##
    ########################################################################################
    def getNumBacklinks (self, dominio):
        try:
            conn = Coneccion()
            html = conn.getHtml(dominio, self.host_search, self.url_search + '%22'+ dominio + '%22-site:')
            data = json.loads(str(html))
            return data['responseData']['cursor']['estimatedResultCount']

        except:
            return '0'

    ########################################################################################
    ## Funcion que retorna si paso de la clase                                            ##
    ########################################################################################
    def getPaso (self):
        return self.paso
