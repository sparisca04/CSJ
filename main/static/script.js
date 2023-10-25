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

