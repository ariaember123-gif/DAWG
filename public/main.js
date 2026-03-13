// $DAWG — shared utilities

function copyCA() {
  const ca = '6dKMmBzboiytxnKqAzUpSiarK7LWoFWicq5T8ZEZpump';
  if (navigator.clipboard) {
    navigator.clipboard.writeText(ca).then(() => toast('✅ CA Copied!'));
  } else {
    const el = document.createElement('textarea');
    el.value = ca;
    document.body.appendChild(el);
    el.select();
    document.execCommand('copy');
    document.body.removeChild(el);
    toast('✅ CA Copied!');
  }
}

function toast(msg) {
  const el = document.getElementById('toast');
  if (!el) return;
  el.textContent = msg;
  el.classList.add('show');
  setTimeout(() => el.classList.remove('show'), 2400);
}

function toggleMenu() {
  document.getElementById('mobileMenu')?.classList.toggle('open');
}

// scroll-reveal
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.mobile-menu a').forEach(a =>
    a.addEventListener('click', () => document.getElementById('mobileMenu')?.classList.remove('open'))
  );

  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
  }, { threshold: 0.08 });

  document.querySelectorAll('.reveal').forEach(el => io.observe(el));
});
