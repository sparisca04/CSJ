function toggleMenu(){
    var navLinks = document.getElementById('nav-items');
    navLinks.classList.toggle('navbar-nav-active');
}
window.onscroll = function(){
  var logo = document.getElementById('logo');
  var logoSmall = document.getElementById('logo-pequeño');
  if(window.scrollY >= 50){
    logo.classList.add('hidden');
    logoSmall.classList.remove('hidden');
  } else {
    logo.classList.remove('hidden');
    logoSmall.classList.add('hidden');
  }
}

function isVisible(element) {
    var rect = element.getBoundingClientRect();
    var viewHeight = Math.max(document.documentElement.clientHeight, window.innerHeight);
    return !(rect.bottom < 0 || rect.top - viewHeight >= 0);
  }
  
  var contador = document.getElementById("contador");
  
  window.addEventListener("scroll", function() {
    if (isVisible(contador)) {
      contador.classList.add("animar");
    } else {
      contador.classList.remove("animar");
    }
  });