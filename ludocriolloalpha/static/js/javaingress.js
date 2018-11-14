/*RUT*/
function modifyText() {
    var letters = [
                    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                    "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u",
                    "v", "w", "x", "y", "z", ",", ".", "!", "'", "$", "%", "&",
                    "/", "(", ")", "=", "?", "¿", "¡", ".", ","
                ]

    var txtrut = document.getElementById("txtrut")
    txtrut.value = txtrut.value.toLowerCase()

    for (let i in letters) {
        txtrut.value = txtrut.value.replace(letters[i], "")
    }

    if (txtrut.value.includes("-")) {
        txtrut.value = txtrut.value.replace(/-/g, "")
        txtrut.value = txtrut.value.slice(0, txtrut.value.length - 1) + "-" + txtrut.value.slice(txtrut.value.length - 1)
    } else {
        txtrut.value = txtrut.value.slice(0, txtrut.value.length - 1) + "-" + txtrut.value.slice(txtrut.value.length - 1)
    }

    if (txtrut.value.includes("k")) {
        txtrut.value = txtrut.value.replace(/k/g, "")
        txtrut.value += "k"
    }
}


function validarForm() {
    var nombres = document.getElementById("txtname").value;
    var apellidos = document.getElementById("txtlastname").value;
    var fecha = document.getElementById("txtage").value;
    var altura = document.getElementById("txtweight").value;
    var peso = document.getElementById("txtweight").value;
    var talla = document.getElementById("txttalla").value;
    var cintura = document.getElementById("txtperimeter").value;
    var cadera = document.getElementById("txtcadera").value;


  

    /*Altura*/
     if (altura < 0) {
        alert("ERROR: Debe ingresar una cantidad valida");
        return false;
    }

    /*Peso*/
    else if (peso < 0) {
        alert("ERROR: Debe ingresar una cantidad valida");
        return false;
    }

    /*Talla*/
    else if (talla < 0) {
        alert("ERROR: Debe ingresar una cantidad valida");
        return false;
    }

    /*Cintura*/
    else if (cintura < 0) {
        alert("ERROR: Debe ingresar una cantidad valida");
        return false;
    }

    /*Cadera*/
    else if (cadera < 0) {
        alert("ERROR: Debe ingresar una cantidad valida");
        return false;
    }



}