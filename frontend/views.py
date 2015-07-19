# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.http import HttpResponse
from time import strftime
import simplejson as json
import re
#from webapp2_extras import sessions

from scraper.lib.dominio import Dominio
from scraper.lib.MotoresBusqueda.yahoo import Yahoo
from scraper.lib.MotoresBusqueda.bing import Bing
from scraper.lib.MotoresBusqueda.google import Google
from scraper.lib.Tecnologias.w3c import W3C
from scraper.lib.Tecnologias.googleAnalytics import GoogleAnalytics
from scraper.lib.Trafico.alexa import Alexa
from scraper.lib.Social.twitter import Twitter
from scraper.lib.Social.facebook import Facebook
from scraper.lib.Social.googlePlus import GooglePlus
from scraper.lib.Contenido.metaTags import MetaTags
from scraper.lib.Contenido.contenido import Contenido
from scraper.lib.wkhtmltoimage import HtmltoImage

dominio_global = ''

########################################################################################
## Funcion de inicio                                                                  ##
########################################################################################
def index (request):
    c = locals()
    c.update(csrf(request))
    response = render_to_response('index.html',c)

    return response

########################################################################################
## Funcion que permite iniciar el analisis del dominio                                ##
########################################################################################
def generar (request):
    if 'dominioInput' in request.POST and request.POST['dominioInput']:
        dominio = str(request.POST.get('dominioInput'))
        eliminar_protocolo = ['http://','https://','www.']

        for srt_tmp in eliminar_protocolo:
          dominio = dominio.replace(srt_tmp, '')

    else:
        error = True
        c = locals()
        c.update(csrf(request))

        return render_to_response('index.html', c)

    return redirect('/analizar/website/' + dominio + '/')

########################################################################################
## Funcion que permite iniciar el analisis del dominio                                ##
########################################################################################
def analizar (request, dominio):
    global dominio_global
    try:
        dominio_global = dominio
        fecha = strftime('%d/%m/%Y %H:%M')
        return render_to_response('analizar.html',locals())

    except:
        return redirect('/')

########################################################################################
##  Funcion que permite obtener los datos de trafico de Alexa                         ##
########################################################################################
def getTrafic (request):
    global dominio_global
    alexa = Alexa()
    data = {'valor':{}, 'paso': 1}

    try:
        dominio = dominio_global
        data['valor'] = alexa.getAlexaRank(dominio)
        return HttpResponse(json.dumps(data), content_type="application/json")

    except:
        return redirect('/')

########################################################################################
##                                                                                    ##
##  Funcion que permite saber si el dominio redirecciona sin el wwww                  ##
##                                                                                    ##
########################################################################################
def getRedireccionWWW (request):
    global dominio_global
    redirect_www = Dominio()
    data = {'valor':{}, 'paso': 3}

    try:
        dominio = dominio_global
        if redirect_www.getRedireccionWWW(dominio) :
            data['paso'] = 1

        return HttpResponse(json.dumps(data), content_type="application/json")

    except:
        return redirect('/')

########################################################################################
##                                                                                    ##
## funcion que permite saber si en un domino existe el archivo robots.txt             ##
##                                                                                    ##
########################################################################################
def getRobots (request):
    global dominio_global
    contenido = Contenido()
    data = {'valor':'N/N', 'paso': 3}

    try:
        dominio = dominio_global
        if contenido.getFile(dominio,'robots.txt') :
            data['valor'] = '<a target="_blank" rel="nofollow" href="http://www.' + dominio + '/robots.txt">http://www.' + dominio + '/robots.txt</a>'
            data['paso'] = 1

        return HttpResponse(json.dumps(data), content_type="application/json")

    except Exception as e:
        print str(e)
        return redirect('/')

########################################################################################
##                                                                                    ##
## funcion que permite saber si en un domino existe el archivo sitemap.xml            ##
##                                                                                    ##
########################################################################################
def getSitemap (request):

    contenido = Contenido()
    data = {'valor':'N/N', 'paso': 3}

    try:

        #self.session = Session()
        #dominio = self.session['dominio']
        #dominio = request.session['dominio']
        dominio = dominio_global
        if contenido.getFile(dominio,'sitemap.xml') :
            data['valor'] = '<a target="_blank" rel="nofollow" href="http://www.' + dominio + '/sitemap.xml">http://www.' + dominio + '/sitemap.xml</a>'
            data['paso'] = 1

        return HttpResponse(json.dumps(data), content_type="application/json")

    except Exception as e:
        print str(e)
        return redirect('/')

########################################################################################
##                                                                                    ##
## funcion que permite obtener el PR de un dominio                                    ##
##                                                                                    ##
########################################################################################
def getGooglePR (request):
    global dominio_global
    google = Google()
    data = {'valor':{}, 'paso': 1}

    try:
        dominio = dominio_global
        pr = google.getPageRank(dominio)
        data['valor'] = pr

        if int(pr['pr']) > 3 :
            data['paso'] = 1

        elif int(pr['pr']) >= 0 :
            data['paso'] = 2

        else:
            data['paso'] = 3

        return HttpResponse(json.dumps(data), content_type="application/json")

    except Exception as e:
        print str(e)
        return redirect('/')

########################################################################################
##                                                                                    ##
## Funciones que permite obtener el numero de paginas indexadas en los                ##
## motores de busquedas                                                               ##
##                                                                                    ##
########################################################################################
def getIndexBrowser (request):
    global dominio_global
    google = Google()
    bing = Bing()
    yahoo = Yahoo()
    data = {'valor':{}, 'paso': 1}
    index = {'google':0, 'bing':0, 'yahoo':0}

    try:
        dominio = dominio_global
        index['google'] = google.getNumIndex(dominio).replace(',','')
        index['yahoo'] = yahoo.getNumIndex(dominio).replace(',','')
        index['bing'] = bing.getNumIndex(dominio).replace(',','')
        data['valor'] = index

        return HttpResponse(json.dumps(data), content_type="application/json")

    except Exception as e:
        print str(e)
        return redirect('/')

########################################################################################
##                                                                                    ##
## funcion que permite obtener la informacion de los enlaces de pagina                ##
##                                                                                    ##
########################################################################################
def getEnlaces (request):

    contenido = Contenido()
    data = {'valor':{}, 'paso': 1}

    try:

        #self.session = Session()
        #dominio = self.session['dominio']
        #dominio = request.session['dominio']
        dominio = dominio_global
        data['valor'] = contenido.getEnlaces(dominio)

        return HttpResponse(json.dumps(data), content_type="application/json")

    except Exception as e:
        print str(e)

        return redirect('/')

########################################################################################
##                                                                                    ##
## funcion que permite obtener el numero de backlinks de alexa y google de 1 pagina   ##
##                                                                                    ##
########################################################################################
def getBacklinks (request):

    alexa = Alexa()
    google = Google()
    data = {'valor':{} , 'paso': 1}
    backlinks = {'google':0, 'alexa': 0}

    try:

        #self.session = Session()
        #dominio = self.session['dominio']
        #dominio = request.session['dominio']
        dominio = dominio_global
        data_tmp = alexa.getAlexaRank(dominio)
        backlinks['alexa'] = data_tmp['backlinks']
        backlinks['google'] = google.getNumBacklinks(dominio).replace(',','')

        data['valor'] = backlinks

        return HttpResponse(json.dumps(data), content_type="application/json")

    except Exception as e:
        print str(e)

        return redirect('/')

########################################################################################
##                                                                                    ##
## Funcion que permite obtener los meta tags de un dominio                            ##
##                                                                                    ##
########################################################################################
def getMetaTags (request):

    meta = MetaTags()

    data = {'valor':{}, 'paso': 1}

    try:

        #self.session = Session()
        #dominio = self.session['dominio']
        #dominio = request.session['dominio']
        dominio = dominio_global
        data['valor'] = meta.getMetaTags(dominio)

        return HttpResponse(json.dumps(data), content_type="application/json")

    except Exception as e:
        print str(e)

        return redirect('/')

########################################################################################
##                                                                                    ##
## Funcion que permite obtener los datos del contenido de un dominio                  ##
##                                                                                    ##
########################################################################################
def getTagsContenido (request):

    contenido = Contenido()
    data = {'valor': { 'encabezados': {}, 'imagenes': {}, 'flash': False, 'iframe': False, 'size': '0 KB', 'text_ratio': '0%' }, 'paso': 1}

    try:

        #self.session = Session()
        #dominio = self.session['dominio']
        #dominio = request.session['dominio']
        dominio = dominio_global

        flash_iframe = contenido.getFlashIframe(dominio)
        tamanio_radio = contenido.getTamanioRadio(dominio)
        data['valor']['encabezados'] = contenido.getEncabezados(dominio)
        data['valor']['imagenes'] = contenido.getImagenesAlt(dominio)

        data['valor']['flash'] = flash_iframe['flash']
        data['valor']['iframe'] = flash_iframe['iframe']

        data['valor']['size'] = tamanio_radio['size']
        data['valor']['text_ratio'] = tamanio_radio['text_ratio']

        return HttpResponse(json.dumps(data), content_type="application/json")

    except Exception as e:
        print str(e)

        return redirect('/')

########################################################################################
##                                                                                    ##
## Funcion que permite obtener los meta tags para movil de un dominio                 ##
##                                                                                    ##
########################################################################################
def getMetaMovil (request):

    meta = MetaTags()
    data = {'valor':'false', 'paso': 3}

    try:

        #self.session = Session()
        #dominio = self.session['dominio']
        #dominio = request.session['dominio']
        dominio = dominio_global
        data['valor'] = meta.getMetaViewport(dominio)
        if data['valor'] :
            data['paso'] = 1

        return HttpResponse(json.dumps(data), content_type="application/json")
    except Exception as e:
        print str(e)

        return redirect('/')

########################################################################################
##                                                                                    ##
##  Funcion que permite obtener datos de los aspectos Sociales de un dominio          ##
##                                                                                    ##
########################################################################################
def getSocial (request):

    twitter = Twitter()
    facebook = Facebook()
    googlePlus = GooglePlus()

    data = {'valor':{ 'facebook': {}, 'twitter': 0, 'googlePlus':0 }, 'paso': 3}

    try:

        #self.session = Session()
        #dominio = self.session['dominio']
        #dominio = request.session['dominio']
        dominio = dominio_global

        data['valor']['facebook'] = facebook.getFB(dominio)

        data['valor']['twitter'] = twitter.getBacklinks(dominio)

        data['valor']['googlePlus'] = googlePlus.getPlusOne(dominio)

        return HttpResponse(json.dumps(data), content_type="application/json")
    except Exception as e:
        print str(e)

        return redirect('/')

########################################################################################
##                                                                                    ##
## funcion que permite saber si en un domino existe el favicon                        ##
##                                                                                    ##
########################################################################################
def getFavicon (request):

    contenido = Contenido()
    data = {'valor':'N/N', 'paso': 3}

    try:

        #self.session = Session()
        #dominio = self.session['dominio']
        #dominio = request.session['dominio']
        dominio = dominio_global
        valor = contenido.getFavicon(dominio)
        if( valor != 'N/N' and valor != 'Error'):
            data['valor'] = '<a target="_blank" rel="nofollow" href="' + valor + '"><img src="' + valor + '" alt="favicon" /></a>'
            data['paso'] = 1
        return HttpResponse(json.dumps(data), content_type="application/json")
    except Exception as e:
        print str(e)

        return redirect('/')

########################################################################################
##                                                                                    ##
## Funcion  que permite obtener los meta tags DC de un dominio                        ##
##                                                                                    ##
########################################################################################
def getDC (request):

    meta = MetaTags()
    data = {'valor':'N/N', 'paso': 3}

    try:

        #self.session = Session()
        #dominio = self.session['dominio']
        #dominio = request.session['dominio']
        dominio = dominio_global
        if meta.getDC(dominio) :
            data['paso'] = 1

        return HttpResponse(json.dumps(data), content_type="application/json")

    except Exception as e:
        print str(e)

        return redirect('/')

########################################################################################
##                                                                                    ##
##  Funcion que permite obtener la IP de un dominio                                   ##
##                                                                                    ##
########################################################################################
def getIp (request):

    dominio_kpi = Dominio()
    data = {'valor':'N/N', 'paso': 3}

    try:

        #self.session = Session()
        #dominio = self.session['dominio']
        #dominio = request.session['dominio']
        dominio = dominio_global
        data['valor'] = dominio_kpi.getIp(dominio)

        return HttpResponse(json.dumps(data), content_type="application/json")
    except Exception as e:
        print str(e)

        return redirect('/')

########################################################################################
##                                                                                    ##
##  Funcion que permite saber si una ip esta bloqueada por span                       ##
##                                                                                    ##
########################################################################################
def getSpanBlock (request):

    dominio_kpi = Dominio()
    data = {'valor':'N/N', 'paso': 3}

    try:

        #self.session = Session()
        #dominio = self.session['dominio']
        #dominio = request.session['dominio']
        dominio = dominio_global
        ip = dominio_kpi.getIp(dominio)
        data['valor'] = dominio_kpi.getSpan(ip)
        data['paso'] = 1
        if data['valor'].lower() != 'no':
            data['paso'] = 3

        return HttpResponse(json.dumps(data), content_type="application/json")
    except Exception as e:
        print str(e)

        return redirect('/')

########################################################################################
##                                                                                    ##
##  Funcion que permite obtener si un dominio cumple el estandar de la W3C            ##
##                                                                                    ##
########################################################################################
def getW3cValidate (request):

    w3c = W3C()
    data = {'valor':'N/N', 'paso': 3}

    try:

        #self.session = Session()
        #dominio = self.session['dominio']
        #dominio = request.session['dominio']
        dominio = dominio_global
        data['valor'] = w3c.isValid(dominio)

        if data['valor']['errors'] != 0:
            data['paso'] = 3
        elif data['valor']['warnings'] != 0 :
            data['paso'] = 2
        else:
            data['paso'] = 1

        return HttpResponse(json.dumps(data), content_type="application/json")
    except Exception as e:
        print str(e)

        return redirect('/')

########################################################################################
##                                                                                    ##
##  Funcion que permite saber si un dominio tiene instalado GoogleAnalytics           ##
##                                                                                    ##
########################################################################################
def getGoogleAnalytics (request):

    googleAnalytics = GoogleAnalytics()
    data = {'valor':'N/N', 'paso': 3}

    try:

        #self.session = Session()
        #dominio = self.session['dominio']
        #dominio = request.session['dominio']
        dominio = dominio_global
        data['valor'] = googleAnalytics.getGoogleAnalytics(dominio)
        if data['valor'] :
            data['paso'] = 1

        return HttpResponse(json.dumps(data), content_type="application/json")

    except Exception as e:
        print str(e)

        return redirect('/')

########################################################################################
##                                                                                    ##
##  Funcion que permite obtener el doctype de un dominio                              ##
##                                                                                    ##
########################################################################################
def getDoctype (request):
    contenido = Contenido()
    data = {'valor':'N/N', 'paso': 3}

    try:

        #self.session = Session()
        #dominio = self.session['dominio']
        #dominio = request.session['dominio']
        dominio = dominio_global
        data['valor'] = contenido.getDoctype(dominio)

        return HttpResponse(json.dumps(data), content_type="application/json")

    except Exception as e:
        print str(e)

        return redirect('/')

########################################################################################
##                                                                                    ##
##  Funcion que permite obtener una imagen del dominio                                ##
##                                                                                    ##
########################################################################################
def getScreenshotWebsite (request):
        htmltoimage = HtmltoImage()
        data = {'valor':'N/N', 'paso': 1}

    #try:

        #self.session = Session()
        #dominio = self.session['dominio']
        #dominio = request.session['dominio']
        dominio = dominio_global
        data['valor'] = htmltoimage.getImage(dominio, '681', '1366')

        return HttpResponse(json.dumps(data), content_type="application/json")

    #except:

        #return redirect('/')

########################################################################################
##                                                                                    ##
##  Funcion que permite obtener una imagen del dominio en dispositivos moviles        ##
##                                                                                    ##
########################################################################################
def getScreenshotWebsiteMovil (request):

    htmltoimage = HtmltoImage()
    data = {'valor':{'smartphone':'N/N','tablet':'N/N'}, 'paso': 1}

    try:

        #self.session = Session()
        #dominio = self.session['dominio']
        #dominio = request.session['dominio']
        dominio = dominio_global

        data['valor']['smartphone'] = htmltoimage.getImage(dominio, '479', '320', 'smartphone')
        data['valor']['tablet'] = htmltoimage.getImage(dominio, '766', '1025', 'tablet')

        return HttpResponse(json.dumps(data), content_type="application/json")

    except Exception as e:
        print str(e)

        return redirect('/')