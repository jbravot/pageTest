# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Meta Tags
# Requires: Python >= 2.4
# Versions:
# metaTags.py 2.0

# Import
from ..Coneccion.coneccion import Coneccion
import re

class MetaTags:
    def __init__(self):
        #valores
        self.paso = False
        self.valor = ''

    ########################################################################################
    ## Funcion que permite obtener los valores de los metatags seo                        ##
    ## Recive un string que indica el dominio al que se realizara la validacion           ##
    ########################################################################################
    def getMetaTags (self, dominio):
        try:
            data = {'title': '', 'size-title': '0', 'description': '', 'size-description': '0', 'keywords': '', 'size-keywords':'0' }
            conn = Coneccion()
            html = conn.getHtmlByUrllib2(dominio)

            header = html.find('head')

            title = header.find('title')
            if title:
                data['title'] = title.text
                data['size-title'] = str(len(title.text))

            description = header.find('meta', attrs={'name':['description','Description','DESCRIPTION']})
            if description:
                data['description'] = description['content']
                data['size-description'] = str(len(description['content']))


            keywordlist = header.find('meta', attrs={'name':['keywords','Keywords','KEYWORDS']})
            if keywordlist:
                data['keywords'] = keywordlist['content']
                data['size-keywords'] = str(len(keywordlist['content']))

            return data

        except:
            return data

    ########################################################################################
    ## Funcion que permite obtener los valores de los metatags dublincore                 ##
    ## Recive un string que indica el dominio al que se realizara la validacion           ##
    ########################################################################################
    def getDC (self, dominio):
        try:
            conn = Coneccion()
            html = conn.getHtmlByUrllib2(dominio)
            header = html.find('head')
            data = re.findall('name="DC.(.*)"', str(header))
            if len(data) > 0:
                return True

            return False

        except:
            return False

    ########################################################################################
    ## Funcion que permite obtener los valores de los metatags viewport                   ##
    ## Recive un string que indica el dominio al que se realizara la validacion           ##
    ########################################################################################
    def getMetaViewport (self, dominio):
        try:
            conn = Coneccion()
            html = conn.getHtmlByUrllib2(dominio)
            header = html.find('head')
            data = header.find('meta', attrs={'name':['viewport','Viewport','VIEWPORT']})
            if data:
                return True

            return False

        except:
            return False