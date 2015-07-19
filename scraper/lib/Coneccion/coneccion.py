# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Permite conectarme por HTTP a un host
# Requires: Python >= 2.4
# Versions:
# coneccion.py 1.0

# Import
import httplib
import urllib2
from ..BeautifulSoup.BeautifulSoup import BeautifulSoup

class Coneccion:

    def __init__(self):
        self.mime_type = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        self.content_type = 'text/html; charset=UTF-8'
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.56 Safari/537.17'

	########################################################################################
    ## debuelve un objeto BeautifulSoup de a un host                                      ##
    ########################################################################################
    def getHtml (self, dominio, host, url, flag_https = False):

        try:
            path = url + dominio
            headers = { 'Accept' : self.mime_type, 'Content-Type' : self.content_type, 'Host' : host, 'User-Agent' : self.user_agent }

            if(flag_https):
            	conn = httplib.HTTPSConnection(host)
            else:
                conn = httplib.HTTPConnection(host)

            conn.request("GET", path, "", headers)
            response = conn.getresponse()
            html = response.read()
            conn.close()

            return BeautifulSoup(html)

        except:
            return 'Error en la Conección'

    ########################################################################################
    ## debuelve un objeto BeautifulSoup de a un host con HTTPS                            ##
    ########################################################################################
    def getHtmlByHttps (self, dominio, host, url):

        try:
            return self.getHtml (dominio, host, url, True)
        except:
            return 'Error en la Conección'

    ########################################################################################
    ## debuelve un objeto BeautifulSoup de a un host                                      ##
    ########################################################################################
    def getPRConeccion (self, dominio, host, url):

        try:
            headers = { 'Accept' : self.mime_type, 'Content-Type' : self.content_type, 'Host' : host, 'User-Agent' : self.user_agent }
            conn = httplib.HTTPConnection(host)
            conn.request("GET", url, "", headers)
            response = conn.getresponse()
            html = response.read()
            conn.close()

            return html

        except:
            return 'Error en la Conección'

    ########################################################################################
    ## debuelve un objeto Connection de a un host con HTTPS                               ##
    ########################################################################################
    def getResponseHttp (self, dominio, host, url):

        try:
            path = url + dominio
            headers = { 'Accept' : self.mime_type, 'Content-Type' : self.content_type, 'Host' : host, 'User-Agent' : self.user_agent }

            conn = httplib.HTTPConnection(host)
            conn.request("GET", path, "", headers)

            return conn.getresponse()

        except:
            return 'Error en la Conección'

    ########################################################################################
    ## debuelve un objeto BeautifulSoup de a un host                                      ##
    ########################################################################################
    def getHtmlByUrllib2 (self, dominio):

        try:
            path = 'http://www.' + dominio
            request_header = { 'Accept' : self.mime_type, 'Content-Type' : self.content_type, 'User-Agent' : self.user_agent }

            req = urllib2.Request(path, headers = request_header)
            con = urllib2.urlopen( req )
            html = con.read()

            return BeautifulSoup(html)

        except:
            return 'Error en la Conección'

    ########################################################################################
    ## debuelve un objeto Connection de a un host con HTTPS                               ##
    ########################################################################################
    def getResponseHttpByUrllib2 (self, dominio):

        try:
            data = {'coneccion': '', 'html': '' }
            path = 'http://www.' + dominio
            request_header = { 'Accept' : self.mime_type, 'Content-Type' : self.content_type, 'User-Agent' : self.user_agent }

            req = urllib2.Request(path, headers = request_header)
            con = urllib2.urlopen( req )
            html = con.read()

            data['html'] = BeautifulSoup(html)
            data['coneccion'] = con

            return data

        except:
            return data

    ########################################################################################
    ## debuelve un objeto Connection de a un host con HTTPS                               ##
    ########################################################################################
    def getRedireccionWWW (self, dominio):

        try:
            path = 'http://' + dominio
            request_header = { 'Accept' : self.mime_type, 'Content-Type' : self.content_type, 'User-Agent' : self.user_agent }

            req = urllib2.Request(path, headers = request_header)
            con = urllib2.urlopen(req)
            return str(con.geturl())

        except:
            return ''

    ########################################################################################
    ## Funcion que permite saber si tiene o no un archivo ej: robots.txt, sitemap.xml     ##
    ## Recive un string que indica el dominio al que se realizara la busqueda             ##
    ########################################################################################
    def getFile (self, dominio,file_name):

        try:

            path = 'http://www.' + dominio + '/' + file_name
            request_header = { 'Accept' : self.mime_type, 'Content-Type' : self.content_type, 'User-Agent' : self.user_agent }
            req = urllib2.Request(path, headers = request_header)
            try:
                con = urllib2.urlopen( req )
                return True
            except urllib2.URLError, e:
                if e.code == 404:
                    return False
        except:
            return False

    ########################################################################################
    ## Funcion que permite saber si tiene activada la redireccion sin el www              ##
    ## Recive un string que indica el dominio al que se realizara la busqueda             ##
    ########################################################################################
    def getRedireccionWWW (self, dominio):

        try:
            path = 'http://' + dominio
            request_header = { 'Accept' : self.mime_type, 'Content-Type' : self.content_type, 'User-Agent' : self.user_agent}
            req = urllib2.Request(path, headers = request_header)
            con = urllib2.urlopen( req )
            url_full = str(con.geturl())

            if '//www.' in url_full:
                return True
            else:
                return False
        except:
            return False