# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Social facebook
# Requires: Python >= 2.4
# Versions:
# facebook.py 2.0

# Import
from ..Coneccion.coneccion import Coneccion
import re

# Facebook
class Facebook:
    def __init__(self):
        #settings
        self.url = 'http://api.facebook.com/restserver.php?method=links.getStats&urls=www.'
        self.host = 'api.facebook.com'

    ########################################################################################
    ## Funcion que permite obtener el numero de likes de Facebook.com                     ##
    ## Recive un string que indica el dominio al que se realizara la busqueda             ##
    ########################################################################################
    def getFB (self, dominio):
        try:
            data = {'share':0, 'like':0, 'comment':0}
            conn = Coneccion()
            html = conn.getHtml(dominio, self.host, self.url)

            text_html = str(html)
            share = re.findall('<share_count>(.*?)</share_count>', text_html)
            like = re.findall('<like_count>(.*?)</like_count>', text_html)
            comment = re.findall('<comment_count>(.*?)</comment_count>', text_html)

            data['share'] = share[0]
            data['like'] = like[0]
            data['comment'] = comment[0]

            #validamos si paso o no
            self.paso = True

            return  data

        except:
            return data