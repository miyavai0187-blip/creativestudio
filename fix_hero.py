import re

# ── 1. Update hero HTML ──────────────────────────────────────────────────────
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_hero = '''  <section class="hero" id="home">
    <canvas id="hero-particles"></canvas>
    <!-- Vertical light beams background -->
    <div class="hero-beams" aria-hidden="true">
      <span class="beam"></span><span class="beam"></span><span class="beam"></span>
      <span class="beam"></span><span class="beam"></span><span class="beam"></span>
      <span class="beam"></span><span class="beam"></span><span class="beam"></span>
      <span class="beam"></span><span class="beam"></span><span class="beam"></span>
    </div>
    <div class="hero-center-glow" aria-hidden="true"></div>

    <div class="container hero-inner">
      <!-- Badge -->
      <div class="hero-badge"><span class="badge-dot"></span>Digital Creative Agency</div>

      <!-- Heading -->
      <h1 class="hero-title">
        <span class="hero-title-line1">We Build Brands That</span>
        <em class="hero-title-italic">Dominate Digital.</em>
      </h1>

      <!-- Sub -->
      <p class="hero-sub">CreativeStudio is a full-service digital agency crafting stunning designs,<br>powerful websites and results-driven marketing strategies.</p>

      <!-- Buttons -->
      <div class="hero-btns">
        <a href="#contact" class="btn btn-primary" id="hero-cta">Start a Project</a>
        <a href="#portfolio" class="btn btn-outline" id="hero-portfolio">View Our Work</a>
      </div>

      <!-- Stats -->
      <div class="hero-stats">
        <div class="stat"><span class="stat-num" data-target="250">0</span><span class="stat-plus">+</span><span class="stat-label">Projects Done</span></div>
        <div class="stat-divider"></div>
        <div class="stat"><span class="stat-num" data-target="98">0</span><span class="stat-plus">%</span><span class="stat-label">Client Satisfaction</span></div>
        <div class="stat-divider"></div>
        <div class="stat"><span class="stat-num" data-target="7">0</span><span class="stat-plus">+</span><span class="stat-label">Years Experience</span></div>
      </div>
    </div>

    <div class="hero-scroll-hint"><span>Scroll Down</span><div class="scroll-arrow"></div></div>
  </section>'''

# Replace old hero section
html = re.sub(
    r'<section class="hero" id="home">.*?</section>',
    new_hero,
    html,
    flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML: Hero section replaced!")

# ── 2. Update hero CSS ───────────────────────────────────────────────────────
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_hero_css = '''/* ===== HERO ===== */
.hero {
  min-height: 100vh;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top: 90px;
  overflow: hidden;
  text-align: center;
}

/* Vertical light beams */
.hero-beams {
  position: absolute;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  display: flex;
  justify-content: center;
  gap: 0;
  overflow: hidden;
}
.beam {
  display: block;
  flex: 1;
  height: 100%;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    rgba(121,179,43,0.13) 30%,
    rgba(121,179,43,0.22) 55%,
    rgba(121,179,43,0.10) 75%,
    transparent 100%
  );
  transform-origin: bottom center;
  animation: beamPulse 4s ease-in-out infinite;
  border-radius: 50% 50% 0 0 / 20% 20% 0 0;
}
.beam:nth-child(1)  { animation-delay: 0s;    opacity: 0.5; }
.beam:nth-child(2)  { animation-delay: 0.3s;  opacity: 0.8; }
.beam:nth-child(3)  { animation-delay: 0.6s;  opacity: 0.6; }
.beam:nth-child(4)  { animation-delay: 0.9s;  opacity: 1.0; }
.beam:nth-child(5)  { animation-delay: 1.2s;  opacity: 0.7; }
.beam:nth-child(6)  { animation-delay: 1.5s;  opacity: 0.9; }
.beam:nth-child(7)  { animation-delay: 1.8s;  opacity: 0.6; }
.beam:nth-child(8)  { animation-delay: 2.1s;  opacity: 1.0; }
.beam:nth-child(9)  { animation-delay: 2.4s;  opacity: 0.7; }
.beam:nth-child(10) { animation-delay: 2.7s;  opacity: 0.5; }
.beam:nth-child(11) { animation-delay: 3.0s;  opacity: 0.8; }
.beam:nth-child(12) { animation-delay: 3.3s;  opacity: 0.6; }

@keyframes beamPulse {
  0%, 100% { transform: scaleY(1);    opacity: var(--op, 0.7); }
  50%       { transform: scaleY(1.08); opacity: 1; }
}

/* Center bottom glow pool */
.hero-center-glow {
  position: absolute;
  bottom: -10%;
  left: 50%;
  transform: translateX(-50%);
  width: 80%;
  height: 60%;
  background: radial-gradient(ellipse at 50% 100%, rgba(121,179,43,0.30) 0%, transparent 65%);
  z-index: 0;
  pointer-events: none;
  filter: blur(20px);
}

/* Particle canvas */
#hero-particles {
  position: absolute; inset: 0; z-index: 0;
  pointer-events: none; opacity: 0.35;
}

/* Hero content — centered */
.hero-inner {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  z-index: 1;
  padding: 40px 0 80px;
  max-width: 860px;
  margin: 0 auto;
}

/* Badge */
.hero-badge {
  display: inline-flex; align-items: center; gap: 8px;
  padding: 8px 20px; border-radius: 50px; margin-bottom: 32px;
  background: rgba(121,179,43,0.10);
  border: 1px solid rgba(121,179,43,0.35);
  font-size: 0.88rem; color: var(--text-muted);
  letter-spacing: 0.5px;
}
.badge-dot {
  width: 7px; height: 7px; border-radius: 50%;
  background: var(--primary); box-shadow: 0 0 8px var(--primary);
  animation: pulse 2s infinite;
}
@keyframes pulse { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:0.6;transform:scale(0.9)} }

/* Title */
.hero-title {
  margin-bottom: 28px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
}
.hero-title-line1 {
  font-family: var(--font-heading);
  font-weight: 800;
  font-size: clamp(2.6rem, 6vw, 5rem);
  color: var(--primary);
  line-height: 1.05;
  letter-spacing: -0.03em;
  display: block;
}
.hero-title-italic {
  font-family: Georgia, 'Times New Roman', serif;
  font-style: italic;
  font-weight: 400;
  font-size: clamp(2.2rem, 5.2vw, 4.4rem);
  color: #fff;
  line-height: 1.1;
  letter-spacing: -0.02em;
  display: block;
}

/* Sub */
.hero-sub {
  font-size: 1.05rem;
  line-height: 1.75;
  margin-bottom: 40px;
  max-width: 600px;
  color: var(--text-muted);
}

/* Buttons */
.hero-btns {
  display: flex; gap: 16px; flex-wrap: wrap;
  justify-content: center; margin-bottom: 56px;
}

/* Stats */
.hero-stats { display: flex; align-items: center; gap: 32px; justify-content: center; }
.stat { text-align: center; }
.stat-num  { font-size: 2.2rem; font-weight: 800; color: var(--primary); font-family: var(--font-heading); }
.stat-plus { font-size: 1.5rem; font-weight: 800; color: var(--primary); }
.stat-label { display: block; font-size: 0.8rem; color: var(--text-muted); margin-top: 2px; }
.stat-divider { width: 1px; height: 44px; background: var(--border); }

/* Scroll hint */
.hero-scroll-hint {
  position: absolute; bottom: 30px; left: 50%; transform: translateX(-50%);
  display: flex; flex-direction: column; align-items: center; gap: 8px;
  color: var(--text-muted); font-size: 0.8rem; z-index: 1;
}
.scroll-arrow {
  width: 20px; height: 30px; border: 2px solid var(--border);
  border-radius: 10px; position: relative;
}
.scroll-arrow::after {
  content: ''; position: absolute; top: 6px; left: 50%; transform: translateX(-50%);
  width: 4px; height: 4px; border-radius: 50%; background: var(--primary);
  animation: scrollDown 2s infinite;
}
@keyframes scrollDown { 0%{top:6px;opacity:1} 100%{top:16px;opacity:0} }

/* Mobile */
@media (max-width: 768px) {
  .hero { padding-top: 90px; }
  .hero-title-line1 { font-size: 2.2rem; }
  .hero-title-italic { font-size: 1.9rem; }
  .hero-sub { font-size: 0.95rem; }
  .hero-stats { gap: 16px; flex-wrap: wrap; }
  .stat-num { font-size: 1.7rem; }
  .beam { opacity: 0.5; }
}
'''

# Replace old hero CSS block (from .hero { to scroll-arrow keyframe)
css = re.sub(
    r'/\* ===== HERO =====.*?@keyframes scrollDown \{[^}]+\}',
    new_hero_css.strip(),
    css,
    flags=re.DOTALL
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS: Hero styles replaced!")
print("DONE!")
