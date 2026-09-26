/* =====================================================
   CreativeStudio — Premium Animation Script
   ===================================================== */

// ===== INTRO PRELOADER (DISABLED) =====
(() => {
  const preloader = document.getElementById('preloader');
  const body = document.body;
  // Instantly remove preloader and reveal site
  body.classList.remove('preloading');
  body.classList.add('site-ready');
  body.style.overflow = '';
  body.dataset.revealed = '1';
  if (preloader) preloader.remove();
  return;

  // Always clears the intro, even if `load` already fired or never fires.
  const reveal = () => {
    if (body.dataset.revealed) return;
    body.dataset.revealed = '1';

    body.classList.remove('preloading');
    body.classList.add('site-ready');
    body.style.overflow = '';

    if (preloader) {
      preloader.classList.add('done');
      preloader.addEventListener('transitionend', () => preloader.remove(), { once: true });
      setTimeout(() => preloader.remove(), 900); // in case transitionend never lands
    }
  };

  // Skip preloader on any return navigation within same session
  const skipPreloader = sessionStorage.getItem('siteVisited') === '1' ||
                        document.referrer.includes(location.hostname) ||
                        new URLSearchParams(location.search).get('noload') === '1';

  if (skipPreloader) {
    if (preloader) preloader.remove();
    reveal();
    return;
  }

  // Mark as visited so future navigations skip the preloader
  sessionStorage.setItem('siteVisited', '1');

  if (!preloader) { reveal(); return; }

  // Lock scroll while the intro is up, and start from the top on reload
  body.style.overflow = 'hidden';
  if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
  window.scrollTo(0, 0);

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const HOLD = reduceMotion ? 200 : 1500;   // let the logo animation breathe
  const MAX  = 4000;                        // hard cap: never trap the visitor

  if (document.readyState === 'complete') {
    setTimeout(reveal, HOLD);
  } else {
    window.addEventListener('load', () => setTimeout(reveal, HOLD), { once: true });
  }
  setTimeout(reveal, MAX);
})();

// ===== HERO PARTICLE CANVAS =====
(function initParticles() {
  const canvas = document.getElementById('hero-particles');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  function resize() {
    canvas.width  = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
  }
  resize();
  window.addEventListener('resize', resize, { passive: true });

  const COUNT = window.innerWidth < 768 ? 30 : 60;
  const particles = [];

  for (let i = 0; i < COUNT; i++) {
    particles.push({
      x:    Math.random() * canvas.width,
      y:    Math.random() * canvas.height,
      r:    Math.random() * 2 + 0.5,
      dx:   (Math.random() - 0.5) * 0.4,
      dy:   (Math.random() - 0.5) * 0.4,
      alpha: Math.random() * 0.5 + 0.1,
      color: Math.random() > 0.5 ? 'rgba(106,176,76,' : 'rgba(124,58,237,'
    });
  }

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach(p => {
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = p.color + p.alpha + ')';
      ctx.fill();
      p.x += p.dx; p.y += p.dy;
      if (p.x < 0) p.x = canvas.width;
      if (p.x > canvas.width)  p.x = 0;
      if (p.y < 0) p.y = canvas.height;
      if (p.y > canvas.height) p.y = 0;
    });
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 120) {
          ctx.beginPath();
          ctx.strokeStyle = 'rgba(106,176,76,' + (0.06 * (1 - dist / 120)) + ')';
          ctx.lineWidth = 0.5;
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.stroke();
        }
      }
    }
    requestAnimationFrame(draw);
  }
  draw();
})();

// ===== NAVBAR SCROLL + ACTIVE PILL =====
const navbar = document.getElementById('navbar');
const navSections = document.querySelectorAll('section[id]');
const navAnchors  = document.querySelectorAll('.nav-links a[href^="#"]');

window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 50);
  const btt = document.getElementById('back-to-top');
  if (btt) btt.classList.toggle('visible', window.scrollY > 400);

  // Active section pill
  let current = '';
  navSections.forEach(sec => {
    if (window.scrollY >= sec.offsetTop - 140) current = sec.id;
  });
  navAnchors.forEach(a => {
    a.classList.toggle('nav-active', a.getAttribute('href') === '#' + current);
    a.style.color = ''; // clear old inline style
  });
}, { passive: true });

// ===== HAMBURGER MENU =====
const hamburger = document.getElementById('hamburger');
const navLinks  = document.getElementById('nav-links');
hamburger.addEventListener('click', () => {
  navLinks.classList.toggle('open');
  const spans = hamburger.querySelectorAll('span');
  if (navLinks.classList.contains('open')) {
    spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
    spans[1].style.opacity   = '0';
    spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
  } else {
    spans.forEach(s => { s.style.transform = ''; s.style.opacity = ''; });
  }
});
navLinks.querySelectorAll('a').forEach(a => {
  a.addEventListener('click', () => {
    navLinks.classList.remove('open');
    hamburger.querySelectorAll('span').forEach(s => { s.style.transform = ''; s.style.opacity = ''; });
  });
});

// ===== COUNTER ANIMATION =====
function animateCounter(el) {
  const target = parseInt(el.dataset.target);
  const duration = 2000;
  const start = performance.now();
  const update = (now) => {
    const elapsed  = now - start;
    const progress = Math.min(elapsed / duration, 1);
    const eased    = 1 - Math.pow(1 - progress, 3);
    el.textContent = Math.round(eased * target);
    if (progress < 1) requestAnimationFrame(update);
  };
  requestAnimationFrame(update);
}

// ===== INTERSECTION OBSERVER =====
const observerOpts = { threshold: 0.12, rootMargin: '0px 0px -60px 0px' };
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const el    = entry.target;
      const delay = parseInt(el.dataset.delay || 0);
      setTimeout(() => {
        el.classList.add('animated');
        el.querySelectorAll('.stat-num[data-target]').forEach(animateCounter);
      }, delay);
      observer.unobserve(el);
    }
  });
}, observerOpts);

// Section headers animation
const headerObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('animated');
      headerObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.3, rootMargin: '0px 0px -40px 0px' });
document.querySelectorAll('.section-header').forEach(el => headerObserver.observe(el));

document.querySelectorAll('[data-animate]').forEach(el => observer.observe(el));

// Immediately animate elements already in viewport on load
function triggerVisibleAnimations() {
  document.querySelectorAll('[data-animate]:not(.animated)').forEach(el => {
    const rect = el.getBoundingClientRect();
    if (rect.top < window.innerHeight && rect.bottom > 0) {
      const delay = parseInt(el.dataset.delay || 0);
      setTimeout(() => {
        el.classList.add('animated');
        el.querySelectorAll('.stat-num[data-target]').forEach(animateCounter);
      }, delay);
    }
  });
  document.querySelectorAll('.section-header:not(.animated)').forEach(el => {
    const rect = el.getBoundingClientRect();
    if (rect.top < window.innerHeight && rect.bottom > 0) {
      el.classList.add('animated');
    }
  });
}
// Run on load and after a short delay (for slow renders)
triggerVisibleAnimations();
setTimeout(triggerVisibleAnimations, 300);

// Hero counter observer
const heroObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      document.querySelectorAll('.stat-num[data-target]').forEach(animateCounter);
      heroObserver.disconnect();
    }
  });
}, { threshold: 0.5 });
const heroEl = document.getElementById('home');
if (heroEl) heroObserver.observe(heroEl);

// Stagger animate cards / steps / portfolio
document.querySelectorAll('.service-card').forEach((el, i) => {
  el.setAttribute('data-animate', 'fadeUp');
  el.setAttribute('data-delay', i * 90);
  observer.observe(el);
});
document.querySelectorAll('.process-step').forEach((el, i) => {
  el.setAttribute('data-animate', 'fadeUp');
  el.setAttribute('data-delay', i * 110);
  observer.observe(el);
});
document.querySelectorAll('.portfolio-item').forEach((el, i) => {
  el.setAttribute('data-animate', 'fadeScale');
  el.setAttribute('data-delay', i * 80);
  observer.observe(el);
});
document.querySelectorAll('.about-image-wrap, .about-content').forEach((el, i) => {
  el.setAttribute('data-animate', i === 0 ? 'fadeLeft' : 'fadeRight');
  observer.observe(el);
});
document.querySelectorAll('.faq-left, .faq-right, .contact-left, .contact-right').forEach((el, i) => {
  el.setAttribute('data-animate', i % 2 === 0 ? 'fadeLeft' : 'fadeRight');
  observer.observe(el);
});
const testiWrapper = document.querySelector('.testimonials-wrapper');
if (testiWrapper) {
  testiWrapper.setAttribute('data-animate', 'fadeUp');
  observer.observe(testiWrapper);
}

// ===== BUTTON RIPPLE =====
document.querySelectorAll('.btn').forEach(btn => {
  btn.addEventListener('click', function(e) {
    const ripple = document.createElement('span');
    ripple.classList.add('btn-ripple');
    const rect = btn.getBoundingClientRect();
    ripple.style.left = (e.clientX - rect.left) + 'px';
    ripple.style.top  = (e.clientY - rect.top) + 'px';
    btn.appendChild(ripple);
    setTimeout(() => ripple.remove(), 700);
  });
});

// ===== PORTFOLIO FILTER =====
const filterBtns     = document.querySelectorAll('.filter-btn');
const portfolioItems = document.querySelectorAll('.portfolio-item');
filterBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    filterBtns.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const filter = btn.dataset.filter;
    let visibleIdx = 0;
    portfolioItems.forEach((item) => {
      const match = filter === 'all' || item.dataset.category === filter;
      if (match) {
        const delay = visibleIdx * 70;
        visibleIdx++;
        item.style.display   = 'block';
        item.style.opacity   = '0';
        item.style.transform = 'translateY(20px) scale(0.97)';
        setTimeout(() => {
          item.style.transition = 'opacity 0.4s ease, transform 0.4s cubic-bezier(0.34,1.2,0.64,1)';
          item.style.opacity    = '1';
          item.style.transform  = 'translateY(0) scale(1)';
        }, delay);
      } else {
        item.style.opacity   = '0';
        item.style.transform = 'scale(0.95)';
        setTimeout(() => { item.style.display = 'none'; }, 280);
      }
    });
  });
});

// ===== TESTIMONIALS SLIDER =====
let currentTesti = 0;
const testiCards = document.querySelectorAll('.testimonial-card');
const testiDots  = document.querySelectorAll('.testi-dot');
const totalTesti = testiCards.length;

function showTesti(idx) {
  testiCards.forEach(c => c.classList.remove('active'));
  testiDots.forEach(d  => d.classList.remove('active'));
  testiCards[idx].classList.add('active');
  testiDots[idx].classList.add('active');
  currentTesti = idx;
}
showTesti(0);
document.getElementById('testi-next').addEventListener('click', () => showTesti((currentTesti + 1) % totalTesti));
document.getElementById('testi-prev').addEventListener('click', () => showTesti((currentTesti - 1 + totalTesti) % totalTesti));
testiDots.forEach(dot => dot.addEventListener('click', () => showTesti(parseInt(dot.dataset.idx))));
setInterval(() => showTesti((currentTesti + 1) % totalTesti), 5000);

// ===== FAQ ACCORDION =====
document.querySelectorAll('.faq-question').forEach(btn => {
  btn.addEventListener('click', () => {
    const item   = btn.parentElement;
    const isOpen = item.classList.contains('open');
    document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
    if (!isOpen) item.classList.add('open');
  });
});

// ===== CONTACT FORM =====
document.getElementById('contact-form').addEventListener('submit', (e) => {
  e.preventDefault();
  const btn     = document.getElementById('form-submit');
  const success = document.getElementById('form-success');
  btn.textContent = 'Sending...';
  btn.disabled    = true;
  btn.style.opacity = '0.75';
  setTimeout(() => {
    btn.textContent   = 'Send Message 🚀';
    btn.disabled      = false;
    btn.style.opacity = '1';
    success.style.display = 'block';
    e.target.reset();
    setTimeout(() => { success.style.display = 'none'; }, 5000);
  }, 1500);
});

// ===== NEWSLETTER FORM =====
const nlForm = document.getElementById('newsletter-form');
if (nlForm) {
  nlForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const input = document.getElementById('nl-email');
    const btn   = document.getElementById('nl-submit');
    btn.textContent      = '✓';
    btn.style.background = '#22c55e';
    btn.style.transform  = 'scale(1.15)';
    input.value = '';
    setTimeout(() => {
      btn.textContent      = '→';
      btn.style.background = '';
      btn.style.transform  = '';
    }, 3000);
  });
}

// NOTE: active-nav-on-scroll is handled by the navbar scroll handler above
// (it toggles .nav-active). A second duplicate block used to live here and
// redeclared `navAnchors`, which threw a SyntaxError and killed this whole file.

// ===== ABOUT FEATURES STAGGER =====
const featureObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.querySelectorAll('.feature-item').forEach((item, i) => {
        item.style.opacity   = '0';
        item.style.transform = 'translateX(-20px)';
        setTimeout(() => {
          item.style.transition = 'opacity 0.4s ease, transform 0.4s cubic-bezier(0.34,1.2,0.64,1)';
          item.style.opacity    = '1';
          item.style.transform  = 'translateX(0)';
        }, 300 + i * 100);
      });
      featureObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.3 });
const aboutFeatures = document.querySelector('.about-features');
if (aboutFeatures) featureObserver.observe(aboutFeatures);

// ===== FOOTER LINKS STAGGER =====
const footerObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.querySelectorAll('a').forEach((a, i) => {
        a.style.opacity   = '0';
        a.style.transform = 'translateY(10px)';
        setTimeout(() => {
          a.style.transition = 'opacity 0.35s ease, transform 0.35s ease, color 0.25s ease, padding-left 0.25s ease';
          a.style.opacity    = '1';
          a.style.transform  = 'translateY(0)';
        }, i * 60);
      });
      footerObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.3 });
document.querySelectorAll('.footer-links').forEach(el => footerObserver.observe(el));

// ===== VIDEO LIGHTBOX =====
// The iframe is created on click and destroyed on close, so no third-party
// player is requested until the visitor actually asks for one.
(() => {
  const modal   = document.getElementById('video-modal');
  const frame   = document.getElementById('video-modal-frame');
  const closeEl = document.getElementById('video-modal-close');
  const backdrop = document.getElementById('video-modal-backdrop');
  if (!modal || !frame) return;

  let lastFocused = null;

  const openModal = (card) => {
    const id    = (card.dataset.yt || '').trim();
    const title = card.querySelector('h4')?.textContent || 'Video';

    if (id) {
      const iframe = document.createElement('iframe');
      iframe.src = `https://www.youtube-nocookie.com/embed/${encodeURIComponent(id)}?autoplay=1&rel=0`;
      iframe.title = title;
      iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture';
      iframe.allowFullscreen = true;
      frame.replaceChildren(iframe);
    } else {
      const msg = document.createElement('p');
      msg.className = 'video-modal-msg';
      msg.innerHTML = `<strong>${title}</strong><br />No video is linked to this card yet. ` +
                      `Add a YouTube ID to its <code>data-yt</code> attribute in index.html to make it playable.`;
      frame.replaceChildren(msg);
    }

    lastFocused = document.activeElement;
    modal.hidden = false;
    document.body.style.overflow = 'hidden';
    closeEl?.focus();
  };

  const closeModal = () => {
    modal.hidden = true;
    frame.replaceChildren();          // stops playback
    document.body.style.overflow = '';
    lastFocused?.focus();
  };

  document.querySelectorAll('.video-card').forEach(card => {
    const btn = card.querySelector('.video-play');
    btn?.addEventListener('click', () => openModal(card));
  });

  closeEl?.addEventListener('click', closeModal);
  backdrop?.addEventListener('click', closeModal);
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !modal.hidden) closeModal();
  });
})();


// ===== CUSTOM BUDGET TOGGLE =====
function toggleCustomBudget(select) {
  const customGroup = document.getElementById('custom-budget-group');
  const customInput = document.getElementById('form-budget-custom');
  if (select.value === 'custom') {
    customGroup.style.display = 'block';
    customInput.setAttribute('required', 'required');
    customInput.focus();
  } else {
    customGroup.style.display = 'none';
    customInput.removeAttribute('required');
    customInput.value = '';
  }
}
