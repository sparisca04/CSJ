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

