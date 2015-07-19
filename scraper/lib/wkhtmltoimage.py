# -*- coding: utf-8 -*-
#!/usr/bin/env python
# wkhtmltoimage
# Requires: Python >= 2.4
# Versions:
# wkhtmltoimage.py 1.0

# Import
import os

class HtmltoImage:
    def __init__(self):
        #valores
        self.comand = 'wkhtmltoimage.exe'
        self.path_comand = 'C:/Program Files/wkhtmltopdf/'
        self.height_comand = '--height'
        self.width_comand = '--width'
        self.path_image = 'C:/Users/pagetest/TooltestApp/web/images/screenshot/'

    ########################################################################################
    ## Funcion que permite obtener la ip de un dominio dado                               ##
    ## Recive un string que indica el dominio al que se realizara la busqueda             ##
    ########################################################################################
    def getImage (self, dominio, height, width, mobil = 'full'):
        try:
			comand = self.path_comand + self.comand

			file_name = dominio + '_' + mobil + '.jpg'
			path_screenshot = self.path_image + file_name

			dominio = 'http://www.' + dominio
			resultado = os.system(comand +' '+ self.height_comand +' '+ height +' '+ self.width_comand +' '+ width +' '+ dominio +' '+ path_screenshot)

			return '/web/images/screenshot/' + file_name

        except:
            return ''