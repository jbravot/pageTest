$(document).ready(function() {
    $(document).on("mouseenter", ".menu", function (e) { ToolsCtr.toggleMenu("163px"); });
    $(document).on("mouseleave", ".menu", function (e) { ToolsCtr.toggleMenu("36px"); });
    $(document).on("click", ".menu ul li", ToolsCtr.activarMenu);
    //$(document).on("click", ".fila", ToolsCtr.mostrarInfo);

	ApiCtr.getTrafic();
    ApiCtr.getRedireccionWWW();
    //ApiCtr.getScreenshotWebsite();

    VALOR_MAX_BAR = $(".bar-progress").css("width").replace("px","");
    VALOR_ANIMAR_BAR = (VALOR_MAX_BAR/NUM_INTERACCIONES);

    $("#menu").scrollspy({
        clase_active: "menu-activo",
        selector: "#menu ul"
    });
});
