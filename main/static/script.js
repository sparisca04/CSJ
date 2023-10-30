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

let slideIndex = 0;
showSlides();

function showSlides() {
  let i;
  let slides = document.getElementsByClassName("slide");
  let dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
  setTimeout(showSlides, 2000); // Change image every 2 seconds
}