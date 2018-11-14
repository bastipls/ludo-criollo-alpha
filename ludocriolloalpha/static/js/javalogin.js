var user = new Array ();
var usertxt = document.getElementById('txtuser');
var alerta  = document.getElementById('alert');

function redirect(){

var urlteacher = "profesor/ingresa_alumnos/";
var urladmin = "operador/ingresa_pruebas/";

    if(usertxt.value.toLowerCase() == "admin"){
        
         window.location.href = urladmin;
          
    } else if(usertxt.value.toLowerCase() == "profesor"){
        window.location.href = urlteacher; 
    }else{

        alerta.style.transform ="scale(1.0)";
       

    }
}
//for (var i = 0 ;i<user.length;i++){
//}