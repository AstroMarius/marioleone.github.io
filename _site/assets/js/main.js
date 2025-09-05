// JavaScript per menu mobile toggle
document.addEventListener('DOMContentLoaded', function() {
  const navToggle = document.querySelector('.nav-toggle');
  const navbar = document.querySelector('.navbar');
  navToggle.addEventListener('click', function() {
    navbar.classList.toggle('active');
  });
});
