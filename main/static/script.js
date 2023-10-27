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

let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slide1 = document.getElementById("slide1");
  let slide2 = document.getElementById("slide2");
  let slide3 = document.getElementById("slide3");
  let dots = document.getElementsByClassName("dot");
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  if (n > 3 || n == 1) {
    slideIndex = 1;
    slide1.style.display = "block";
    slide2.style.display = "none";
    slide3.style.display = "none";
    dots[slideIndex-1].className += " active";
  }
  else if (n < 1 || n == 3) {
    slideIndex = 3;
    slide1.style.display = "none";
    slide2.style.display = "none";
    slide3.style.display = "block";
    dots[slideIndex-1].className += " active";
  }
  else {
    slideIndex = 2
    slide1.style.display = "none";
    slide2.style.display = "block";
    slide3.style.display = "none";
    dots[slideIndex-1].className += " active";
  }
}