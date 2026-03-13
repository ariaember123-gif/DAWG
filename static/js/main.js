// $DAWG — Main JS

function copyCA() {
  const ca = '6dKMmBzboiytxnKqAzUpSiarK7LWoFWicq5T8ZEZpump';
  navigator.clipboard.writeText(ca).then(() => {
    showToast('✅ CA Copied!');
  }).catch(() => {
    // fallback
    const el = document.createElement('textarea');
    el.value = ca;
    document.body.appendChild(el);
    el.select();
    document.execCommand('copy');
    document.body.removeChild(el);
    showToast('✅ CA Copied!');
  });
}

function showToast(msg) {
  const toast = document.getElementById('toast');
  if (!toast) return;
  toast.textContent = msg;
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 2500);
}

function toggleMenu() {
  const menu = document.getElementById('mobileMenu');
  if (menu) menu.classList.toggle('open');
}

// Close mobile menu on link click
document.addEventListener('DOMContentLoaded', () => {
  const links = document.querySelectorAll('.mobile-menu a');
  links.forEach(l => l.addEventListener('click', () => {
    document.getElementById('mobileMenu').classList.remove('open');
  }));

  // Scroll reveal
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.style.opacity = '1';
        e.target.style.transform = 'translateY(0)';
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.about-card, .toke-card, .step-card, .social-card, .example-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    observer.observe(el);
  });
});
