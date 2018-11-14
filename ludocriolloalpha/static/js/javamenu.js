var btnmenu = document.getElementById("btn-menu");
var navega = document.getElementById("navegador");
var submenuu = document.getElementsByClassName("submenu");

btnmenu.addEventListener('click', function () {
    navega.classList.toggle('move');
})


$(".submenu").click(function () {
    $(this).children("ul").slideToggle();
})


$("ul").click(function (p) {
    p.stopPropagation();
})