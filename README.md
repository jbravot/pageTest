# pageTest
Aplicaci�n que permite probar si un sitio web cumple con 
varios de los principales factores SEO para el posicionamiento 
en los diferentes motores de b�squeda.

pageTest
============

pageTest es una aplicaci�n web desarrollada en Django/Python
que permite probar si un sitio web cumple con varios de los 
principales factores SEO para el posicionamiento en los 
diferentes motores de b�squeda.

El proyecto fue empezado en el 3013, y en Junio del 2015 
se realiz� correcciones y se actualizo a la versi�n 1.7 de Django.

**Note** `Demo 2013` http://seo-tooltest.appspot.com/

**Note** `Video` https://www.youtube.com/watch?v=-iGv0W2oqlQ

**Note** `Junio del 2015` se actualizo las librer�as de scraper


Principales Caracteriscitas
===============
El modulo scraper permite consultar varios sitio y servicios entre los cuales:

- Tr�fico de Alexa
- Redirecci�n si el www
- Fichero robots.txt
- Mapa del sitio XML
- Google� Page Rank
- P�ginas indexadas (Google, Bing, Yahoo)
- Enlaces en p�gina
- Backlinks
- T�tulo del sitio web
- Descripci�n del sitio web
- Palabras clave meta del sitio web
- Encabezados del sitio web
- Im�genes del sitio web
- Usa Flash
- Usa Iframes
- Tama�o del sitio web
- Taza Texto/HTML del sitio web
- Etiqueta meta viewport
- Facebook (comentario, likes, comparti�)
- Twitter (Backlinks)
- Google� + (comparti�)
- Favicon
- Dublin core
- IP
- Bloquear Span (Se encuentra en lista de span)
- Validador W3C
- Google� Analytics
- Doctype

Dependencias
============

PageTest fue probado en Python 2.6, y Python 2.7

- Django==1.7
- BeautifulSoup==3.2.1
- simplejson==3.7.3
- mysql-python==1.2.5