# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Meta Tags
# Requires: Python >= 2.4
# Versions:
# metaTags.py 2.0

# Import
from ..Coneccion.coneccion import Coneccion
from HTMLParser import HTMLParser
import re

class Contenido:
    def __init__(self):
        #valores
        self.paso = False

    ########################################################################################
    ## Funcion que permite obtener todos los encabezados de un texto (H1, H2..., H5)      ##
    ## Recive un string que indica el dominio                                             ##
    ########################################################################################
    def getEncabezados (self, dominio):
        try:
            data = { 'h1': [ 0, [] ], 'h2': [ 0, [] ], 'h3': [ 0, [] ],'h4': [ 0, [] ], 'h5': [ 0, [] ] }
            conn = Coneccion()
            html = conn.getHtmlByUrllib2(dominio)

            body = html.find('body')
            data['h1'] = Contenido.getNumHx(body, 'h1')
            data['h2'] = Contenido.getNumHx(body, 'h2')
            data['h3'] = Contenido.getNumHx(body, 'h3')
            data['h4'] = Contenido.getNumHx(body, 'h4')
            data['h5'] = Contenido.getNumHx(body, 'h5')

            return data

        except:
            return data

    ########################################################################################
    ## Funcion que permite obtener todas las imagenes y saber si tiene el atributo ALT    ##
    ## Recive un string que indica el dominio                                             ##
    ########################################################################################
    def getImagenesAlt (self, dominio):
        try:
            data = {'img': 0, 'alt_vacios': 0 }
            conn = Coneccion()
            html = conn.getHtmlByUrllib2(dominio)

            body = html.find('body')
            imagenes = body.findAll('img')
            num_alt_vacios = 0
            for img in imagenes :
                try:
                    if img['alt'] == '':
                        num_alt_vacios += 1
                except :
                    num_alt_vacios += 1
            data['img'] = len(imagenes)
            data['alt_vacios'] =  num_alt_vacios
            return data

        except:
            return data

    ########################################################################################
    ## Funcion que permite obtener el numero de enlaces del sitio                         ##
    ## Recive un string que indica el dominio                                             ##
    ########################################################################################
    def getEnlaces (self, dominio):
        try:
            data = { 'text': '', 'nInternos': 0, 'nExternos': 0, 'nFollow': 0 }
            conn = Coneccion()
            html = conn.getHtmlByUrllib2(dominio)

            body = html.find('body')
            links = body.findAll('a')

            num_links_internos = 0
            num_links_externos = 0
            num_links_externos_notfollow = 0
            num_links_externos_follow = 0
            for link in links:
                try:
                    link_href = link['href']
                    if link_href.startswith('/') or link_href.startswith('http://www.' + dominio) :
                        num_links_internos += 1
                    else:
                        num_links_externos += 1
                        try:
                            if link['rel'] == 'nofollow' :
                                num_links_externos_notfollow += 1
                        except:
                            tmp=0
                except :
                    pass

            #print "==== List link ==="
            data['text'] = 'Se encontraron ' + str(len(links)) + ' enlaces'
            data['nInternos'] = num_links_internos
            data['nNoFollow'] =  num_links_externos_notfollow
            num_links_externos_follow = num_links_externos - num_links_externos_notfollow
            data['nFollow'] = num_links_externos_follow
            #print "==== fin ==="
            return data

        except:
            return data

    ########################################################################################
    ## Funcion que permite saber si existen elementos Flash y Iframe                      ##
    ## Recive un string que indica el dominio                                             ##
    ########################################################################################
    def getFlashIframe (self, dominio):
        try:
            data = {'flash': False, 'iframe': False }
            conn = Coneccion()
            html = conn.getHtmlByUrllib2(dominio)

            body = html.find('body')

            iframe = body.find('iframe')
            if iframe:
                data['iframe'] = True

            flash = body.find('object')
            if flash:
                data['flash'] = True

            return data

        except:
            return data

    ########################################################################################
    ## Funcion que permite saber el tamaño del archivo html del dominio                   ##
    ## Recive un string que indica el dominio                                             ##
    ########################################################################################
    def getTamanioRadio (self, dominio):
        try:
            data = {'size': '0 KB', 'text_ratio': '0%' }
            conn = Coneccion()
            data_conn = conn.getResponseHttpByUrllib2(dominio)

            coneccion = data_conn['coneccion']
            html = data_conn['html']
            body = html.find('body')

            try:
                data['size'] = '%.2f KB' % float(float(coneccion.getheaders()) / 1024)
            except:
                data['size'] = '%.2f KB' % float(float(len(str(html))) / 1024)

            try:
                parser = MyHTMLParser()
                parser.feed(str(body).decode('utf-8'))

                len_html = float(len(str(html)))
                len_text = float(len(parser.getTextHtml()))
                #len_code = len_html - len_text
                data['text_ratio'] = '%.2f' % float((len_text/len_html)*100) + ' %'

            except:
                data['text_ratio'] = '0%'

            return data

        except:
            return data

    ########################################################################################
    ## Funcion que permite saber si tiene o no un archivo ej: robots.txt, sitemap.xml     ##
    ## Recive un string que indica el dominio al que se realizara la busqueda             ##
    ########################################################################################
    def getFile (self, dominio, file_name):

        conn = Coneccion()
        return conn.getFile(dominio, file_name)

    ########################################################################################
    ## Funcion que permite saber si tiene o no favicon                                    ##
    ## Recive un string que indica el dominio al que se realizara la busqueda             ##
    ########################################################################################
    def getFavicon (self, dominio):
        try:
            conn = Coneccion()
            html = conn.getHtmlByUrllib2(dominio)
            header = html.find('head')

            favicon = header.find("link", attrs={'rel':["shortcut icon","Shortcut Icon","SHORTCUT ICON", "icon", "ICON"]})
            if favicon:
                link = favicon["href"]
                if link.startswith('http'):
                    return link
                elif link.startswith('//'):
                    return link
                else:
                    return 'http://www.' + dominio + '/' + link
            else:
                return 'N/N'
        except:
            return 'Error'

    ########################################################################################
    ## Funcion que permite saber si tiene activada la redireccion sin el www              ##
    ## Recive un string que indica el dominio al que se realizara la busqueda             ##
    ########################################################################################
    def getRedireccionWWW (self, dominio):

        conn = Coneccion()
        return conn.getRedireccionWWW(dominio)

    ########################################################################################
    ## Funcion que permite saber el Doctype de un dominio                                 ##
    ## Recive un string que indica el dominio al que se realizara la busqueda             ##
    ########################################################################################
    def getDoctype (self, dominio):
        try:
            doctype = 'HTML'
            conn = Coneccion()
            html = conn.getHtmlByUrllib2(dominio)
            doctype_html = html.contents[0].upper()
            if doctype_html == 'DOCTYPE HTML':
                return 'HTML 5'

            data = re.findall('//DTD (.*)//EN', doctype_html)
            if data[0] != '':
                doctype = data[0]
            return doctype

        except:
            return 'HTML'

    ########################################################################################
    ## Funcion que permite obtener los Meta tags de un dominio dado                       ##
    ## Recive un string que indica el dominio al que se realizara la busqueda             ##
    ########################################################################################
    @staticmethod
    def getNumHx (body, hx):
        hx_array = body.findAll(hx)
        data = [len(hx_array)]
        hx_text = []

        for h in hx_array :
            hx_text.append(h.text)

        data.append(hx_text)
        return data

########################################################################################
## Clase que hereda de HTMLParser para poder realizar la obtencion de solo            ##
## texto del html                                                                     ##
########################################################################################
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.textHtml = ''
    def handle_data(self, data):
        self.textHtml += data
    def getTextHtml(self):
        return self.textHtml