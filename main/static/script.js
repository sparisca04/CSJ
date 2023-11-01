function toggleMenu(){
    var navLinks = document.getElementById('nav-items');
    navLinks.classList.toggle('navbar-nav-active');
}
window.onscroll = function(){
  var logo = document.getElementById('logo');
  var logoSmall = document.getElementById('logo-pequeño');
  var linkLogo = document.getElementById('link-logo');
  if(window.scrollY >= 50){
    logo.classList.add('hidden');
    linkLogo.classList.add('link-logo-pequeño');
    logoSmall.classList.remove('hidden');
  } else {
    logo.classList.remove('hidden');
    linkLogo.classList.remove('link-logo-pequeño');
    logoSmall.classList.add('hidden');
  }
}
addEventListener("DOMContentLoaded", () => {
  const contadores = document.querySelectorAll(".contador-cantidad");
  const velocidad = 1000;
  const animarContadores = () => {
    for(const contador of contadores) {
      const actualizar_contador = () => {
        let cantidad_maxima = +contador.dataset.cantidadTotal,
          valor_actual = +contador.innerText,
          incremento = cantidad_maxima / velocidad;
      
        if(valor_actual < cantidad_maxima) {
          contador.innerText = Math.ceil(valor_actual + incremento);
          setTimeout(actualizar_contador, 5);
        } else {
          contador.innerText = "+" + cantidad_maxima;
        }
      }
      "+" + actualizar_contador();
    }
  }
 
  const mostrarIconos = (e) => {
    e.forEach(element => {
      if(element.isIntersecting) {
        element.target.classList.add('animate');
        element.target.classList.remove('disguise');
        setTimeout(animarContadores, 300);
      }
    });
  }
  const observer = new IntersectionObserver(mostrarIconos, {
    threshold: 0.75
  })
  const elementosHTML = document.querySelectorAll('.contador');
  elementosHTML.forEach(elementHTML => {
    observer.observe(elementHTML);
  });
})