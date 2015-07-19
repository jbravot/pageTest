# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Alexa API
# Requires: Python >= 2.4
# Versions: 2.1 Modificado el 17/07/2015
# alexa.py 2.1

# Import
from ..Coneccion.coneccion import Coneccion
import re

# Settings
#Alexa - Daily Traffic Rank
#http://traffic.alexa.com/graph?&w=295&h=160&o=f&y=t&r=6m&u=woorank.com
#Alexa - Daily Reach
#http://traffic.alexa.com/graph?&w=295&h=160&o=f&y=r&r=6m&u=woorank.com
#Alexa - Search Visit
#http://traffic.alexa.com/graph?&w=295&h=160&o=f&y=q&r=6m&u=woorank.com
#Alexa - Daily Pageview Per User
#http://traffic.alexa.com/graph?&w=295&h=160&o=f&y=u&r=6m&u=woorank.com

class Alexa:
    def __init__(self):
        #settings
        self.__class__.url = 'http://data.alexa.com/data?cli=10&dat=snbamz&url='
        self.__class__.host = 'data.alexa.com'

    ########################################################################################
    ## Funcion que permite obtener los datos de Global Rank, Country Rank y Backlinks     ##
    ## de Alexa                                                                           ##
    ## Recive un string que indica el dominio al que se realizara la busqueda             ##
    ## Retorna un diccionario con los valores solicitados:                                ##
    ## data = {'global-rank':0, 'country-rank':0, 'country-name':'N/N', 'backlinks':0}    ##                                             ##
    ########################################################################################
    def getAlexaRank (self, dominio):

        try:
            data = {
                'global-rank':0, 
                'country-rank':0, 
                'country-name':'N/N', 
                'country-code':'N/N', 
                'backlinks':0, 
                'img':'N/N'
            }
            conn = Coneccion()
            html = conn.getHtml(dominio, self.__class__.host, self.__class__.url)
            text_html = str(html)

            global_rank = re.findall('popularity url="(.*?)" text="(.*?)"', text_html)
            country_rank = re.findall('country code="(.*?)" name="(.*?)" rank="(.*?)"', text_html)
            backlinks = [0] ###YA NO FUNCIONA (2015) re.findall('linksin num="(.*?)"', text_html)

            data['global-rank'] = global_rank[0][1]
            data['country-rank'] = country_rank[0][2]
            data['country-name'] = country_rank[0][1]
            data['country-code'] = country_rank[0][0].lower()
            data['backlinks'] = backlinks[0]
            data['img'] = 'http://traffic.alexa.com/graph?&w=295&h=160&o=f&y=t&r=6m&u=' + dominio

            return  data

        except:
            return data