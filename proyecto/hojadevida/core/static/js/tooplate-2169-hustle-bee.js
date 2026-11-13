/*

    Tooplate 2169 Hustle Bee

    https://www.tooplate.com/view/2169-hustle-bee

    Free HTML CSS Template

*/

// ===== NAV =====
const nav = document.getElementById('nav');
const navToggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');
window.addEventListener('scroll', () => nav.classList.toggle('scrolled', window.scrollY > 40));
navToggle.addEventListener('click', () => { navToggle.classList.toggle('active'); navLinks.classList.toggle('open'); });
navLinks.querySelectorAll('a').forEach(l => l.addEventListener('click', () => { navToggle.classList.remove('active'); navLinks.classList.remove('open'); }));

// ===== SCROLL REVEAL =====
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0.12, rootMargin: '0px 0px -30px 0px' });
document.querySelectorAll('.reveal, .reveal-scale').forEach(el => observer.observe(el));

// ===== ACTIVE NAV LINK =====
const sections = document.querySelectorAll('section[id]');
const navLinkList = document.querySelectorAll('.nav-links a');
window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(s => { if (scrollY >= s.offsetTop - 120) current = s.id; });
  navLinkList.forEach(link => {
    link.style.color = ''; link.style.background = '';
    if (link.getAttribute('href') === '#' + current && !link.classList.contains('nav-cta')) {
      link.style.color = 'var(--dark)'; link.style.background = 'var(--honey-glow)';
    }
  });
});