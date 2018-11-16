
var iconuser = document.getElementById('id_nombres_alumno');
var grade = document.getElementById('id_curso_alumno');
var names = document.getElementById('id_nombres_alumno');
var lastname = document.getElementById('id_apellidos_alumno');
var age = document.getElementById('id_edad_alumno');
var talla = document.getElementById('id_talla_alumno');
var weight = document.getElementById('id_peso_alumno');
var perimeter = document.getElementById('id_perimetro_cintura_alumno');
var fpleft = document.getElementById('id_fuerza_prensil_izquierda_alumno');
var fpright = document.getElementById('id_fuerza_prensil_derecha_alumno');
var imc = document.getElementById('id_imc_alumno');
var imccategory = document.getElementById('id_categoria_imc_alumno');

//              contalert.innerHTML =' <div id="alert" class="alert-red"> <span class="closebtn" onclick="closeAlert()">&times;</span> <b>Alerta! </b> El rut ingresado no existe </div>';
function closeAlert(){
    contalert.innerHTML ="";
  
}
var editgrade = document.getElementById('edit-grade');
var editname = document.getElementById('edit-name');
var editlastname = document.getElementById('edit-lastname');
var editage = document.getElementById('edit-age');
var editweight = document.getElementById('edit-weight');
var edittalla = document.getElementById('edit-talla');
var editperimeter = document.getElementById('edit-perimeter');
var edit_fp_left = document.getElementById('edit-fp-left');
var edit_fp_right = document.getElementById('edit-fp-right');

editgrade.addEventListener("click", function (e) {
    grade.readOnly = false;
    var temp = grade.value;
    grade.value = "";
    grade.focus();
    grade.value = temp;
});
editname.addEventListener("click", function (e) {
    names.readOnly = false;
    var temp = names.value;
    names.value = "";
    names.focus();
    names.value = temp;
});
editlastname.addEventListener("click", function (e) {
    lastname.readOnly = false;
    var temp = lastname.value;
    lastname.value = ""
    lastname.focus();
    lastname.value = temp;
});
editage.addEventListener("click", function (e) {
    age.readOnly = false;
    var temp = age.value;
    age.value = "";
    age.focus();
    age.value = temp;
});
editweight.addEventListener("click", function (e) {
    weight.readOnly = false;
    var temp = weight.value;
    weight.value = "";
    weight.focus();
    weight.value = temp;
});
edittalla.addEventListener("click", function (e) {
    talla.readOnly = false;
    var temp = talla.value;
    talla.value = "";
    talla.focus();
    talla.value = temp;
});
editperimeter.addEventListener("click", function (e) {
    perimeter.readOnly = false;
    var temp = perimeter.value;
    perimeter.value ="";
    perimeter.focus();
    perimeter.value =temp;
});
edit_fp_left.addEventListener("click", function (e) {
    fpleft.readOnly = false;
    var temp = fpleft.value;
    fpleft.value ="";
    fpleft.focus();
    fpleft.value = temp;
});
edit_fp_right.addEventListener("click", function (e) {
    fpright.readOnly = false;
    var temp  = fpright.value;
    fpright.value = "";
    fpright.focus();
    fpright.value = temp;
});
