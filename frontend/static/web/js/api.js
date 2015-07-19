;(function( ApiCtr, $, undefined ){

    /*************************************/
    /* ======== SECCION TRAFIC ========  */
    /*************************************/

    //========= ALEXA =========//
    /*------------------------------------*/
    /*-- Consultamos los datos de ALEXA --*/
    /*------------------------------------*/
	ApiCtr.getTrafic = function(){
        $.getJSON('/analizar/getTrafic/', function(data){
            /* validamos los parametros */
            ApiCtr.dataTrafic(data);
            ToolsCtr.animarBarra(VALOR_ANIMAR_BAR);

            /* Llamamos a la otra peticion */
            ApiCtr.getRobots();
        });
    };

    /*-----------------------------------------*/
    /*-- Validamos los parametros de la data --*/
    /*-----------------------------------------*/
    ApiCtr.dataTrafic = function(data){
        $("#data-global-rank").text(data["valor"]["global-rank"]);
        $("#data-country-rank").text(data["valor"]["country-rank"]);
        $("#flag-country").addClass("flag-" + data["valor"]["country-code"]);
        $("#flag-country").attr("alt", data["valor"]["country-name"]);
        $("#data-country-name").text(data["valor"]["country-name"]);
        $("#data-backlinks").text(data["valor"]["backlinks"]);
        $("#alexa-traffic").attr("src",data["valor"]["img"]);

        $("#trafico .loader").hide();
    };


    /*******************************************/
    /* ======== SECCION ESENCIAL SEO ========  */
    /*******************************************/

    //========= REDIRECCION  WWW =========//
    /*---------------------------------------------------*/
    /*-- Consultamos si existe la redireccion sin WWW. --*/
    /*---------------------------------------------------*/
    ApiCtr.getRedireccionWWW = function(){
        $.getJSON('/analizar/getRedireccionWWW/', function(data){
            /* validamos los parametros */
            ApiCtr.dataRedireccionWWW(data);
            ToolsCtr.animarBarra(VALOR_ANIMAR_BAR);

            /* Llamamos a la otra peticion */
            ApiCtr.getSitemap();
        });
    };

    /*-----------------------------------------*/
    /*-- Validamos los parametros de la data --*/
    /*-----------------------------------------*/
    ApiCtr.dataRedireccionWWW = function(data){
        if(data["paso"] == 1){
            $("#si-www").show();
            $("#no-www").hide();
        }
        /* validamos si paso la prueba el parametro */
        ToolsCtr.validarPaso("#www",data["paso"]);
    };

    //========= FICHERO ROBOTS =========//
    /*-------------------------------------------------*/
    /*-- Consultamos si existe la un fichero ROBOTS. --*/
    /*-------------------------------------------------*/
    ApiCtr.getRobots = function(){
        $.getJSON('/analizar/getRobots/', function(data){
             /* validamos los parametros */
            ApiCtr.dataRobots(data);
            ToolsCtr.animarBarra(VALOR_ANIMAR_BAR);

            /* Llamamos a la otra peticion */
            ApiCtr.getGooglePR();
        });
    };
    
    /*-----------------------------------------*/
    /*-- Validamos los parametros de la data --*/
    /*-----------------------------------------*/
    ApiCtr.dataRobots = function(data){
        $("#data-robots").html(data["valor"]);

        /* validamos si paso la prueba el parametro */
        ToolsCtr.validarPaso("#seo-robots",data["paso"]);
    };

    //========= FICHERO SITEMAP =========//
    /*--------------------------------------------------*/
    /*-- Consultamos si existe la un fichero SITEMAP. --*/
    /*--------------------------------------------------*/
    ApiCtr.getSitemap = function(){
        $.getJSON('/analizar/getSitemap/', function(data){
            /* validamos los parametros */
            ApiCtr.dataSitemap(data);
            ToolsCtr.animarBarra(VALOR_ANIMAR_BAR);

            /* Llamamos a la otra peticion */
            ApiCtr.getIndexBrowser();
        });
    };

    /*-----------------------------------------*/
    /*-- Validamos los parametros de la data --*/
    /*-----------------------------------------*/
    ApiCtr.dataSitemap = function(data){
        $("#data-sitemap").html(data["valor"]);

        /* validamos si paso la prueba el parametro */
        ToolsCtr.validarPaso("#seo-sitemap",data["paso"]);
    };

    //========= PR =========//
    /*-------------------------------*/
    /*-- Consultamos el PAGE RANK. --*/
    /*-------------------------------*/
    ApiCtr.getGooglePR = function(){
        $.getJSON('/analizar/getGooglePR/', function(data){
            /* validamos los parametros */
            ApiCtr.dataGooglePR(data);
            ToolsCtr.animarBarra(VALOR_ANIMAR_BAR);

            /* Llamamos a la otra peticion */
            ApiCtr.getBacklinks();
        });
    };

    /*-----------------------------------------*/
    /*-- Validamos los parametros de la data --*/
    /*-----------------------------------------*/
    ApiCtr.dataGooglePR = function(data){
        $("#data-pr").text(data["valor"]["pr"]);
        ToolsCtr.validarPaso("#google-pr",data["paso"]);
    };

    //========= INDEX PAGES BROWSER =========//
    /*-------------------------------------------------*/
    /*-- Consultamos el numero de paginas indexadas. --*/
    /*-------------------------------------------------*/
    ApiCtr.getIndexBrowser = function(){
        $.getJSON('/analizar/getIndexBrowser/', function(data){
            /* validamos los parametros */
            ApiCtr.dataIndexBrowser(data);
            ToolsCtr.animarBarra(VALOR_ANIMAR_BAR);

            /* Llamamos a la otra peticion */
            ApiCtr.getEnlaces();
        });
    };

    /*-----------------------------------------*/
    /*-- Validamos los parametros de la data --*/
    /*-----------------------------------------*/
    ApiCtr.dataIndexBrowser = function(data){
        var google = parseInt(data["valor"]["google"]);
        var yahoo = parseInt(data["valor"]["yahoo"]);
        var bing = parseInt(data["valor"]["bing"]);

        ToolsCtr.dibujarGraficoIndex(google,yahoo,bing);
        $("#esencial .loader").hide();
    };

    /***************************************/
    /* ======== SECCION ENLACES  ========  */
    /***************************************/

    //========= ENLACES =========//
    /*---------------------------------------*/
    /*-- Consultamos el numero de enlaces. --*/
    /*---------------------------------------*/
    ApiCtr.getEnlaces = function(){
        $.getJSON('/analizar/getEnlaces/', function(data){
            /* validamos los parametros */
            ApiCtr.dataEnlaces(data);
            ToolsCtr.animarBarra(VALOR_ANIMAR_BAR);

            /* Llamamos a la otra peticion */
            ApiCtr.getMetaTags();
        });
    };

    /*-----------------------------------------*/
    /*-- Validamos los parametros de la data --*/
    /*-----------------------------------------*/
    ApiCtr.dataEnlaces = function(data){
        var nInternos = parseInt(data["valor"]["nInternos"]);
        var nNoFollow = parseInt(data["valor"]["nNoFollow"]);
        var nFollow = parseInt(data["valor"]["nFollow"]);

        $("#data-enlaces").text(data["valor"]["text"]);
        ToolsCtr.dibujarGraficoEnlaces(nInternos, nNoFollow, nFollow);

        $("#enlaces-seo .loader").hide();
    };

    //========= BACKLINKS =========//
    /*-------------------------------*/
    /*-- Consultamos el PAGE RANK. --*/
    /*-------------------------------*/
    ApiCtr.getBacklinks = function(){
        $.getJSON('/analizar/getBacklinks/', function(data) {
            /* validamos los parametros */
            ApiCtr.dataBacklinks(data);
            ToolsCtr.animarBarra(VALOR_ANIMAR_BAR);

            /* Llamamos a la otra peticion */
            ApiCtr.getTagsContenido()
        });
    };

    /*-----------------------------------------*/
    /*-- Validamos los parametros de la data --*/
    /*-----------------------------------------*/
    ApiCtr.dataBacklinks = function(data){
        var data_google = parseInt(data["valor"]["google"]);
        var data_alexa = parseInt(data["valor"]["alexa"]);

        ToolsCtr.dibujarGraficoBacklinks(data_alexa, data_google);
    };

    /********************************************/
    /* ======== SECCION CONTENIDO SEO ========  */
    /********************************************/

    //========= META TAGS =========//
    /*----------------------------------------------*/
    /*-- Consultamos los valores de los META TAG. --*/
    /*----------------------------------------------*/
    ApiCtr.getMetaTags = function(){
        $.getJSON('/analizar/getMetaTags/', function(data) {
            /* validamos los parametros */
            ApiCtr.dataMetaTags(data);
            ToolsCtr.animarBarra(VALOR_ANIMAR_BAR);

            /* Llamamos a la otra peticion */
            ApiCtr.getMetaMovil();
        });
    };

    /*-----------------------------------------*/
    /*-- Validamos los parametros de la data --*/
    /*-----------------------------------------*/
    ApiCtr.dataMetaTags = function(data){
        $("#data-title").text(data["valor"]["title"]);
        var title_size = data["valor"]["size-title"];
        $("#data-title-size").text(title_size);
        ToolsCtr.validarPasoMetaTags("#seo-meta-title",title_size,10,70 );

        $("#data-description").text(data["valor"]["description"]);
        var description_size = data["valor"]["size-description"];
        $("#data-description-size").text(description_size);
        ToolsCtr.validarPasoMetaTags("#seo-meta-description",description_size,70,160 );

        $("#data-keywords").text(data["valor"]["keywords"]);
        var keywords_size = data["valor"]["size-keywords"];
        $("#data-keywords-size").text(keywords_size);
        ToolsCtr.validarPasoMetaTags("#seo-meta-keywords",keywords_size,10,70 );
    };

    //========= CONTENIDO =========//
    /*------------------------------------------*/
    /*-- Consultamos los datos del contenido. --*/
    /*------------------------------------------*/
    ApiCtr.getTagsContenido = function(){
        $.getJSON('/analizar/getTagsContenido/', function(data) {
            /* validamos los parametros */
            ApiCtr.dataTagsContenido(data);
            ToolsCtr.animarBarra(VALOR_ANIMAR_BAR);

            /* Llamamos a la otra peticion */
            ApiCtr.getSocial();
        });
    };

    /*-----------------------------------------*/
    /*-- Validamos los parametros de la data --*/
    /*-----------------------------------------*/
    ApiCtr.dataTagsContenido = function(data){
        var encabezados = data["valor"]["encabezados"];
        var img = data["valor"]["imagenes"];

        $("#data-h1").text(encabezados["h1"][0]);
        $("#data-h2").text(encabezados["h2"][0]);
        $("#data-h3").text(encabezados["h3"][0]);
        $("#data-h4").text(encabezados["h4"][0]);
        $("#data-h5").text(encabezados["h5"][0]);

        $("#data-list-encabezados").html("");
        ToolsCtr.addListItem("#data-list-encabezados","h1",encabezados);
        ToolsCtr.addListItem("#data-list-encabezados","h2",encabezados);
        ToolsCtr.addListItem("#data-list-encabezados","h3",encabezados);
        ToolsCtr.addListItem("#data-list-encabezados","h4",encabezados);
        ToolsCtr.addListItem("#data-list-encabezados","h5",encabezados);

        $("#data-img-total").text(img["img"]);
        $("#data-alt-vacios").text(img["alt_vacios"]);

        if(img["alt_vacios"] != 0){
             ToolsCtr.validarPaso("#contenido-img",3);
        }else{
             ToolsCtr.validarPaso("#contenido-img",1);
        }

        if(data["valor"]["flash"] != false){
            $("#data-flash").text("Si");
             ToolsCtr.validarPaso("#contenido-flash",3);
        }else{
            $("#data-flash").text("No");
             ToolsCtr.validarPaso("#contenido-flash",1);
        }

        if(data["valor"]["iframe"] != false){
            $("#data-iframe").text("Si");
             ToolsCtr.validarPaso("#contenido-iframe",3);
        }else{
            $("#data-iframe").text("No");
             ToolsCtr.validarPaso("#contenido-iframe",1);
        }

        $("#data-size").text(data["valor"]["size"]);
        $("#data-text-ratio").text(data["valor"]["text_ratio"]);

        $("#contenido .loader").hide();
    };

    /*****************************************************/
    /* ======== SECCION MOBIL Y REDES SOCIALES ========  */
    /*****************************************************/

    //========= MOVIL =========//
    /*------------------------------------------*/
    /*-- Consultamos la imegen del sitio web. --*/
    /*------------------------------------------*/
    ApiCtr.getScreenshotWebsite = function(){
        $.getJSON('/analizar/getScreenshotWebsite/', function(data) {
            /* validamos los parametros */
            ApiCtr.dataScreenshotWebsite(data);
            ToolsCtr.animarBarra(VALOR_ANIMAR_BAR);

            /* Llamamos a la otra peticion */
            ApiCtr.getScreenshotWebsiteMovil();
        });
    };

    /*-----------------------------------------*/
    /*-- Validamos los parametros de la data --*/
    /*-----------------------------------------*/
    ApiCtr.dataScreenshotWebsite = function(data){
        var img = data["valor"];
        if(img != ""){
            $("#screenshot-website div img").removeClass("camera_loader")
            $("#screenshot-website div img").addClass("img-website")
            $("#screenshot-website div img").attr("src",img);
        }
    };

    /*-----------------------------------------------------------*/
    /*-- Consultamos la imegen del sitio web en version movil. --*/
    /*-----------------------------------------------------------*/
    ApiCtr.getScreenshotWebsiteMovil = function(){
        $.getJSON('/analizar/getScreenshotWebsiteMovil/', function(data) {
            /* validamos los parametros */
            ApiCtr.dataScreenshotWebsiteMovil(data);
            ToolsCtr.animarBarra(VALOR_ANIMAR_BAR);
        });
    }

    /*-----------------------------------------*/
    /*-- Validamos los parametros de la data --*/
    /*-----------------------------------------*/
    ApiCtr.dataScreenshotWebsiteMovil = function(data){
        var img_smartphone = data["valor"]["smartphone"];
        var img_tablet = data["valor"]["tablet"];

        if(img_smartphone != ""){
            //$("#visualizacion-movil img").removeClass("camera_loader")
            $("#visualizacion-movil .smartphone img").attr("src",img_smartphone);
        }
        if(img_tablet != ""){
            //$("#visualizacion-movil img").removeClass("camera_loader")
            $("#visualizacion-movil .tablet img").attr("src",img_tablet);
        }
    };


    //========= META VIEWPORT =========//
    /*---------------------------------------------------*/
    /*-- Consultamos los valores de los META VIEWPORT. --*/
    /*---------------------------------------------------*/
    ApiCtr.getMetaMovil = function(){
         $.getJSON('/analizar/getMetaMovil/', function(data) {
            /* validamos los parametros */
            ApiCtr.dataMetaMovil(data);
            ToolsCtr.animarBarra(VALOR_ANIMAR_BAR);

            /* Llamamos a la otra peticion */
            ApiCtr.getFavicon();
        });
    };

    /*-----------------------------------------*/
    /*-- Validamos los parametros de la data --*/
    /*-----------------------------------------*/
    ApiCtr.dataMetaMovil = function(data){
        if(data["valor"] != false){
            $("#data-viewport").text("Si");
        }else{
            $("#data-viewport").text("No");
        }
        ToolsCtr.validarPaso("#viewport",data["paso"]);

        $("#movil .loader").hide();
    };

    //========= REDES SOCIALES =========//
    /*---------------------------------------------------*/
    /*-- Consultamos los valores de los META VIEWPORT. --*/
    /*---------------------------------------------------*/
    ApiCtr.getSocial = function(){
        $.getJSON('/analizar/getSocial/', function(data) {
            /* validamos los parametros */
            ApiCtr.dataSocial(data);
            ToolsCtr.animarBarra(VALOR_ANIMAR_BAR);

            /* Llamamos a la otra peticion */
            ApiCtr.getDC();
        });
    };

    /*-----------------------------------------*/
    /*-- Validamos los parametros de la data --*/
    /*-----------------------------------------*/
    ApiCtr.dataSocial = function(data){
        $("#data-fb-coment").text(data["valor"]["facebook"]["comment"]);
        $("#data-fb-like").text(data["valor"]["facebook"]["like"]);
        $("#data-fb-share").text(data["valor"]["facebook"]["share"]);
        $("#data-twitter").text(data["valor"]["twitter"]);
        $("#data-plus").text(data["valor"]["googlePlus"]);

        $("#redes-sociales .loader").hide();
    };

    /************************************/
    /* ======== USABILIDAD ========  */
    /************************************/

    //========= FICHERO FAVICON =========//
    /*--------------------------------------------*/
    /*-- Consultamos si el sitio tiene favicon. --*/
    /*--------------------------------------------*/
    ApiCtr.getFavicon = function(){
        $.getJSON('/analizar/getFavicon/', function(data) {
            /* validamos los parametros */
            ApiCtr.dataFavicon(data);
            ToolsCtr.animarBarra(VALOR_ANIMAR_BAR);

            /* Llamamos a la otra peticion */
            ApiCtr.getIP();
        });
    };

    /*-----------------------------------------*/
    /*-- Validamos los parametros de la data --*/
    /*-----------------------------------------*/
    ApiCtr.dataFavicon = function(data){
        $("#data-favicon").html(data["valor"]);
        ToolsCtr.validarPaso("#favicon",data["paso"]);
    };

    //========= TAGS DUBLIN CORE =========//
    /*--------------------------------------------*/
    /*-- Consultamos si los tags de DUBLIN CORE. --*/
    /*--------------------------------------------*/
    ApiCtr.getDC = function(){
        $.getJSON('/analizar/getDC/', function(data) {
            /* validamos los parametros */
            ApiCtr.dataDC(data);
            ToolsCtr.animarBarra(VALOR_ANIMAR_BAR);

            /* Llamamos a la otra peticion */
            ApiCtr.getSpanBlock();
        });
    };

    /*-----------------------------------------*/
    /*-- Validamos los parametros de la data --*/
    /*-----------------------------------------*/
    ApiCtr.dataDC = function(data){
        if(data["paso"] == 1){
            $("#data-dc").text("Si");
        }else{
            $("#data-dc").text("No");
        }
        ToolsCtr.validarPaso("#dc",data["paso"]);

        $("#usabilidad .loader").hide();
    };

    /************************************/
    /* ======== SEGURIDAD ========  */
    /************************************/

    //========= IP =========//
    /*------------------------*/
    /*-- Consultamos la IP. --*/
    /*------------------------*/
    ApiCtr.getIP = function(){
        $.getJSON('/analizar/getIp/', function(data) {
            /* validamos los parametros */
            ApiCtr.dataIP(data);
            ToolsCtr.animarBarra(VALOR_ANIMAR_BAR);

            /* Llamamos a la otra peticion */
            ApiCtr.getW3cValidate();
        });
    };

    /*-----------------------------------------*/
    /*-- Validamos los parametros de la data --*/
    /*-----------------------------------------*/
    ApiCtr.dataIP = function(data){
        $("#data-ip").html(data["valor"]);
    };

    //========= BLOQUEAR SPAN =========//
    /*----------------------------------------------------*/
    /*-- Consultamos si el sitio esta el lista de span. --*/
    /*----------------------------------------------------*/
    ApiCtr.getSpanBlock = function(){
        $.getJSON('/analizar/getSpanBlock/', function(data) {
            /* validamos los parametros */
            ApiCtr.dataSpanBlock(data);
            ToolsCtr.animarBarra(VALOR_ANIMAR_BAR);

            /* Llamamos a la otra peticion */
            ApiCtr.getGoogleAnalytics();
        });
    };

    /*-----------------------------------------*/
    /*-- Validamos los parametros de la data --*/
    /*-----------------------------------------*/
    ApiCtr.dataSpanBlock = function(data){
        $("#data-span-block").text(data["valor"]);
        ToolsCtr.validarPaso("#span-block",data["paso"]);

        $("#seguridad .loader").hide();
    };


    /************************************/
    /* ======== TECNOLOGIA ========  */
    /************************************/

    //========= W3C =========//
    /*----------------------------------------------*/
    /*-- Consultamos si esta validado con el W3C. --*/
    /*----------------------------------------------*/
    ApiCtr.getW3cValidate = function(){
        $.getJSON('/analizar/getW3cValidate/', function(data) {
            /* validamos los parametros */
            ApiCtr.dataW3cValidate(data);
            ToolsCtr.animarBarra(VALOR_ANIMAR_BAR);

            /* Llamamos a la otra peticion */
            ApiCtr.getDoctype();
        });
    };

    /*-----------------------------------------*/
    /*-- Validamos los parametros de la data --*/
    /*-----------------------------------------*/
    ApiCtr.dataW3cValidate = function(data){
        $("#data-w3c-status").html(data["valor"]["status"]);
        $("#data-w3c-errors").html(data["valor"]["errors"]);
        $("#data-w3c-warnings").html(data["valor"]["warnings"]);

        ToolsCtr.validarPaso("#w3c",data["paso"]);
    };

    //========= GOOGLE ANALYTICS =========//
    /*---------------------------------------*/
    /*-- Consultamos si el sitio tiene GA. --*/
    /*---------------------------------------*/
    ApiCtr.getGoogleAnalytics = function(){
        $.getJSON('/analizar/getGoogleAnalytics/', function(data) {
            /* validamos los parametros */
            ApiCtr.dataGoogleAnalytics(data);
            ToolsCtr.animarBarra(VALOR_ANIMAR_BAR);
        });
    };

    /*-----------------------------------------*/
    /*-- Validamos los parametros de la data --*/
    /*-----------------------------------------*/
    ApiCtr.dataGoogleAnalytics = function(data){
        if(data["valor"] != false){
            $("#data-googleAnalytics").text("Si");
        }else{
            $("#data-googleAnalytics").text("No");
        }
        ToolsCtr.validarPaso("#googleAnalytics",data["paso"]);
    };

    //========= Doctype =========//
    /*----------------------------------------------------*/
    /*-- Consultamos si el sitio esta el lista de span. --*/
    /*----------------------------------------------------*/
    ApiCtr.getDoctype = function(){
        $.getJSON('/analizar/getDoctype/', function(data) {
            /* validamos los parametros */
            ApiCtr.dataDoctype(data);
            ToolsCtr.animarBarra(VALOR_ANIMAR_BAR);
        });
    };

    /*-----------------------------------------*/
    /*-- Validamos los parametros de la data --*/
    /*-----------------------------------------*/
    ApiCtr.dataDoctype = function(data){
        $("#data-doctype").text(data["valor"]);
        $("#tecnologia .loader").hide();
    };
}( window.ApiCtr = window.ApiCtr || {}, jQuery ));