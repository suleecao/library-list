const headerLogoContainer = document.querySelector('.header-logo-container');
let lastScrollTop = 0;
const scrollThreshold = 50; // Adjust this as neeced

window.addEventListener('scroll', function() {
  const scrollTop = window.scrollY || document.documentElement.scrollTop;

  // Scrolling down
  if (scrollTop > lastScrollTop && scrollTop > scrollThreshold) {
    headerLogoContainer.classList.add('hidden');
  }
  // Scrolling up
  else if (scrollTop < lastScrollTop) {
    headerLogoContainer.classList.remove('hidden');
  }

  lastScrollTop = scrollTop;
});