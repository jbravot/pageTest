# -*- coding: utf-8 -*-
#!/usr/bin/env python
# W3C Validator KPI
# Requires: Python >= 2.4
# Versions:
# w3c.py 2.0

# Import
from ..Coneccion.coneccion import Coneccion

class W3C:
    def __init__(self):
        #settings
        self.url = 'http://validator.w3.org/check?uri=http%3A%2F%2F'
        self.host = 'validator.w3.org'

    ########################################################################################
    ## Funcion que permite obtener el valor de la validacion W3C Validator                ##
    ## Recive un string que indica el dominio al que se realizara la validacion           ##
    ########################################################################################
    def isValid (self, dominio):
        try:
            data = { 'status':'', 'num-errors': 0, 'num-warnings': 0 }
            conn = Coneccion()
            response = conn.getResponseHttp(dominio, self.host, self.url)
            data['status'] = response.getheader('X-W3C-Validator-Status')
            data['errors'] = response.getheader('X-W3C-Validator-Errors')
            data['warnings'] = response.getheader('X-W3C-Validator-Warnings')

            return data

        except:
            return data
