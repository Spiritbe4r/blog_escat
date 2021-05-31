
document.getElementById("icon-menu").addEventListener("click", mostrar_menu);

function mostrar_menu() {

    document.getElementById("move-content").classList.toggle('move-container-all');
    document.getElementById("show-menu").classList.toggle('show-lateral');
}


// Scroll up //

document.getElementById("button-up").addEventListener("click", scrollUp);

function scrollUp() {

    const currentScroll = document.documentElement.scrollTop || document.body.scrollTop;
    if (currentScroll > 0) {
        window.requestAnimationFrame(scrollUp);
        window.scrollTo(0, currentScroll - (currentScroll / 10));
        buttonUp.style.transform = "scale(0)";
    }
}
///   ///

buttonUp = document.getElementById("button-up");

window.onscroll = function () {

    const scroll = document.documentElement.scrollTop;
    if (scroll > 500) {
        buttonUp.style.transform = "scale(1)";
    } else if (scroll < 500) {
        buttonUp.style.transform = "scale(0)";
    }
}






//Buscador de contenido


//Ejecutando funciones
document.getElementById("icon-search").addEventListener("click", mostrar_buscador);
document.getElementById("cover-ctn-search").addEventListener("click", ocultar_buscador);

//Declarando variables
bars_search = document.getElementById("ctn-bars-search");
cover_ctn_search = document.getElementById("cover-ctn-search");
inputSearch = document.getElementById("inputSearch");
box_search = document.getElementById("box-search");


//Funcion para mostrar el buscador
function mostrar_buscador() {

    bars_search.style.top = "80px";
    cover_ctn_search.style.display = "block";
    inputSearch.focus();

    if (inputSearch.value === "") {
        box_search.style.display = "none";
    }

}



//Funcion para ocultar el buscador
function ocultar_buscador() {

    bars_search.style.top = "-10px";
    cover_ctn_search.style.display = "none";
    inputSearch.value = "";
    box_search.style.display = "none";

}


// ejecucion de codigo al presionar una tecla //

function presionar_tecla() {

    let tecla_esc = event.keyCode;

    if (tecla_esc === 27) {

        return ocultar_buscador();


    }

}

window.onkeydown = presionar_tecla;

//Creando filtrado de busqueda

document.getElementById("inputSearch").addEventListener("keyup", buscador_interno);

function buscador_interno() {


    let filter = inputSearch.value.toUpperCase();
    let li = box_search.getElementsByTagName("li");

    //Recorriendo elementos a filtrar mediante los "li"
    let a;
    let textValue;
    for (let i = 0; i < li.length; i++) {

        a = li[i].getElementsByTagName("a")[0];
        textValue = a.textContent || a.innerText;

        if (textValue.toUpperCase().indexOf(filter) > -1) {

            li[i].style.display = "";
            box_search.style.display = "block";

            if (inputSearch.value === "") {
                box_search.style.display = "none";
            }

        } else {
            li[i].style.display = "none";
        }

    }



}
/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function (event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("submenu");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

/* scroll

ScrollReveal().reveal('.container-content');
ScrollReveal().reveal('.article-container-cover', { delay:500 });
ScrollReveal().reveal('.articulos', { delay:500 });
ScrollReveal().reveal('.container-aside', { delay:500 });
ScrollReveal().reveal('.articulos', { delay:500 }); */



