var slideIndex = 1;
var numEntries = 2;
for (i = 1; i <= numEntries; i++) {
    showSlides(slideIndex, i);
}

// Next/previous controls
function plusSlides(n, entry) {
  showSlides(slideIndex += n, entry);
}

// Thumbnail image controls
function currentSlide(n, entry) {
  showSlides(slideIndex = n, entry);
}

function showSlides(n, entry) {
  var i;
  var slides = document.getElementsByClassName(entry);
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}
