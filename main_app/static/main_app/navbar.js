let lastScrollY = window.scrollY;

window.addEventListener('scroll', function () {
  const navbar = document.getElementById('navbar');
  
  if (window.scrollY === 0) {
    navbar.classList.remove('hidden'); 
  } else if (window.scrollY > lastScrollY) {
    navbar.classList.add('hidden'); 
  } else {
    navbar.classList.remove('hidden'); 
  }
  
  lastScrollY = window.scrollY;
});