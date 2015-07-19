var NUM_INTERACCIONES = 20;
var VALOR_ANIMAR_BAR = 0;
var VALOR_MAX_BAR = 0;
var PROGRESS_BAR = 0;

(function( ToolsCtr, $, undefined ){

	/*------------------------------------------------------------------*/
	ToolsCtr.validarPaso = function(id,valor){
        if(valor == 1){
            $(id + " .status").addClass("good");
        }else if(valor == 2){
            $(id + " .status").addClass("warming");
        }else{
            $(id + " .status").addClass("danger");
        }
    };

    /*------------------------------------------------------------------*/
	ToolsCtr.validarPasoMetaTags = function(id,valor,min,max){
        if( valor == 0 ){
            $(id + " .status").addClass("danger");
        }else if( (valor >= min) && (valor <= max) ){
            $(id + " .status").addClass("good");
        }else if( (valor < min) || (valor > max) ){
            $(id + " .status").addClass("warming");
        }
    };

     /*------------------------------------------------------------------*/
	ToolsCtr.addListItem = function(id,h,encabezados){
        $.each(encabezados[h][1], function(i, item) {
            var tmp = "[" + h +"] " + item;
            $(id).append("<li>" + tmp + "</li>");
        });
    };

    /*------------------------------------------------------------------*/
	ToolsCtr.toggleMenu = function(valor){
        $(".menu").stop().delay(200).animate({width: valor}, 250);
        $(".menu ul").stop().delay(200).animate({width: valor}, 250);
    };

    /*------------------------------------------------------------------*/
	ToolsCtr.activarMenu = function(){
        $(".menu ul li").removeClass("menu-activo");
        $(this).addClass("menu-activo");
    };

    /*------------------------------------------------------------------*/
	ToolsCtr.mostrarInfo = function(){
       $(this).toggleClass("fila-up");
       $(this).find(".box-info").slideToggle();
    };

    /*------------------------------------------------------------------*/
	ToolsCtr.dibujarGraficoIndex = function(data_google, data_yahoo, data_bing){
        $("#graficoIndex").highcharts({
                chart: {
                    type: "bar"
                },
                title: {
                    text: null
                },
                subtitle: {
                    text: null
                },
                xAxis: {
                    categories: ["Index"],
                    title: {
                        text: null
                    },
                    labels: {
                        enabled: false
                    }
                },
                yAxis: {
                    min: 0,
                    gridLineWidth: 1,
                    title: {
                        text: null
                    }
                },
                tooltip: {
                    formatter: function() {
                        return this.series.name +": <strong>"+ this.point.y + "</strong>";
                    }
                },
                plotOptions: {
                    bar: {
                        dataLabels: {
                            enabled: true
                        }
                    }
                },
                legend: {
                    borderWidth: 0,
                    backgroundColor: "#FFFFFF",
                    shadow: false
                },
                credits: {
                    enabled: false
                },
                colors: [
                    "#FFA614",
                    "#7A0097",
                    "#3E78FD",
                ],
                series: [{
                    name: "Bing",
                    data: [data_bing]
                }, {
                    name: "Yahoo!",
                    data: [data_yahoo]
                }, {
                    name: "Google",
                    data: [data_google]
                }]
        });
    };

    /*------------------------------------------------------------------*/
	ToolsCtr.dibujarGraficoBacklinks = function(data_alexa, data_google){
        $("#graficoBacklinks").highcharts({
                chart: {
                    type: "bar"
                },
                title: {
                    text: null
                },
                subtitle: {
                    text: null
                },
                xAxis: {
                    categories: ["Backlinks"],
                    title: {
                        text: null
                    },
                    labels: {
                        enabled: false
                    }
                },
                yAxis: {
                    min: 0,
                    gridLineWidth: 1,
                    title: {
                        text: null
                    }
                },
                tooltip: {
                    formatter: function() {
                        return this.series.name +": <strong>"+ this.point.y + "</strong>";
                    }
                },
                plotOptions: {
                    bar: {
                        dataLabels: {
                            enabled: true
                        }
                    }
                },
                legend: {
                    borderWidth: 0,
                    backgroundColor: "#FFFFFF",
                    shadow: false
                },
                credits: {
                    enabled: false
                },
                colors: [
                    "#FFA614",
                    "#3E78FD",
                ],
                series: [{
                    name: "Alexa",
                    data: [data_alexa]
                }, {
                    name: "Google",
                    data: [data_google]
                }]
        });
    };

    /*------------------------------------------------------------------*/
	ToolsCtr.dibujarGraficoEnlaces = function(nInternos, nNoFollow, nFollow){
        $(document).ready(function () {
            $("#graficoEnlaces").highcharts({
                chart: {
                    plotBackgroundColor: null,
                    plotBorderWidth: null,
                    plotShadow: false
                },
                title: {
                    text: null
                },
                tooltip: {
                    formatter: function() {
                        return this.point.name +": <strong>"+ this.point.y + "</strong>";
                    }
                },
                credits: {
                    enabled: false
                },
                legend: {
                    layout: "vertical",
                    align: "right",
                    verticalAlign: "top",
                    borderWidth: 0
                },
                plotOptions: {
                    pie: {
                        allowPointSelect: true,
                        cursor: "pointer",
                        dataLabels: {
                            enabled: false
                        },
                        showInLegend: true
                    }
                },
                series: [{
                    type: "pie",
                    name: "",
                    data: [
                        ["Enlaces Internos",   nInternos],
                        ["Enlaces Extrernos: NoFollow",   nNoFollow],
                        ["Enlaces Extrernos: traspaso de link juice",   nFollow],
                    ]
                }]
            });
        });
    };
    /*------------------------------------------------------------------*/
	ToolsCtr.animarBarra = function(progress){
        PROGRESS_BAR += progress;
        $("#bar").animate(
            {width: PROGRESS_BAR + "px"},
            {easing: "swing",
             duration: 800,
             complete: function() {
                var tmp_width = $("#bar").css("width").replace("px","");
                if( tmp_width >= VALOR_MAX_BAR){
                    $(".bar-progress").hide(800);
                }
            }}
        );
    };

}( window.ToolsCtr = window.ToolsCtr || {}, jQuery ));