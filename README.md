# pageTest
Aplicación que permite probar si un sitio web cumple con 
varios de los principales factores SEO para el posicionamiento 
en los diferentes motores de búsqueda.

pageTest
============

pageTest es una aplicación web desarrollada en Django/Python
que permite probar si un sitio web cumple con varios de los 
principales factores SEO para el posicionamiento en los 
diferentes motores de búsqueda.

El proyecto fue empezado en el 3013, y en Junio del 2015 
se realizó correcciones y se actualizo a la versión 1.7 de Django.

**Note** `Demo 2013` http://seo-tooltest.appspot.com/

**Note** `Video` https://www.youtube.com/watch?v=-iGv0W2oqlQ

**Note** `Junio del 2015` se actualizo las librerías de scraper


Principales Caracteriscitas
===============
El modulo scraper permite consultar varios sitio y servicios entre los cuales:

- Tráfico de Alexa
- Redirección si el www
- Fichero robots.txt
- Mapa del sitio XML
- Google™ Page Rank
- Páginas indexadas (Google, Bing, Yahoo)
- Enlaces en página
- Backlinks
- Título del sitio web
- Descripción del sitio web
- Palabras clave meta del sitio web
- Encabezados del sitio web
- Imágenes del sitio web
- Usa Flash
- Usa Iframes
- Tamaño del sitio web
- Taza Texto/HTML del sitio web
- Etiqueta meta viewport
- Facebook (comentario, likes, compartió)
- Twitter (Backlinks)
- Google™ + (compartió)
- Favicon
- Dublin core
- IP
- Bloquear Span (Se encuentra en lista de span)
- Validador W3C
- Google™ Analytics
- Doctype

Dependencias
============

PageTest fue probado en Python 2.6, y Python 2.7

- Django==1.7
- BeautifulSoup==3.2.1
- simplejson==3.7.3
- mysql-python==1.2.5