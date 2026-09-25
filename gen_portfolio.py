
categories = [
    ("commercial", "🎬", "Commercial Production"),
    ("promo", "📢", "Promotional Videos"),
    ("content", "✨", "Content Creation"),
    ("documentary", "🎞️", "Documentary Production"),
    ("social", "📱", "Social Media Content"),
    ("product", "📸", "Product Video &amp; Photography"),
    ("advertising", "📣", "Advertising Content"),
    ("motion", "⚡", "Motion Graphics"),
    ("creative", "🎨", "Creative Projects"),
]

cats_html = ""
for cat_id, icon, title in categories:
    cats_html += f"""
  <div class="pf-cat visible" data-cat="{cat_id}">
    <div class="pf-cat-header">
      <div class="pf-cat-icon">{icon}</div>
      <div class="pf-cat-title">{title}</div>
      <span class="pf-cat-badge">Coming Soon</span>
    </div>
    <div class="pf-cat-line"></div>
    <div class="pf-cards">
      <div class="pf-placeholder"><span class="pf-badge">Coming Soon</span><div class="pf-picon">{icon}</div><div class="pf-ptext"><strong>{title}</strong>Portfolio item to be added</div></div>
      <div class="pf-placeholder"><span class="pf-badge">Coming Soon</span><div class="pf-picon">{icon}</div><div class="pf-ptext"><strong>{title}</strong>Portfolio item to be added</div></div>
      <div class="pf-placeholder"><span class="pf-badge">Coming Soon</span><div class="pf-picon">{icon}</div><div class="pf-ptext"><strong>{title}</strong>Portfolio item to be added</div></div>
    </div>
  </div>"""

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Portfolio - Creative Studio</title>
  <meta name="description" content="Explore Creative Studio portfolio." />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,700;12..96,800&family=Outfit:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet" />
  <link rel="icon" type="image/png" href="logo.png" />
  <link rel="stylesheet" href="style.css?v=99" />
  <style>
    .pf-page {{ padding-top: 90px; min-height: 100vh; }}
    .pf-hero {{ text-align:center; padding:60px 0 40px; background:radial-gradient(ellipse at 50% 0%,rgba(106,176,76,0.10) 0%,transparent 60%); }}
    .pf-hero-tag {{ display:inline-block; padding:6px 18px; border-radius:50px; background:rgba(106,176,76,0.1); border:1px solid rgba(106,176,76,0.35); color:#6ab04c; font-size:0.82rem; font-weight:600; letter-spacing:1px; text-transform:uppercase; margin-bottom:18px; }}
    .pf-hero h1 {{ font-family:var(--font-heading); font-size:clamp(2rem,5vw,3.5rem); font-weight:800; line-height:1.1; margin-bottom:14px; }}
    .pf-hero p {{ color:var(--text-muted); font-size:1rem; max-width:520px; margin:0 auto; }}
    .pf-filters {{ display:flex; flex-wrap:wrap; gap:10px; justify-content:center; padding:32px 0 36px; }}
    .pf-fbtn {{ padding:7px 18px; border-radius:50px; cursor:pointer; border:1px solid rgba(106,176,76,0.25); background:transparent; color:var(--text-muted); font-family:var(--font); font-size:0.83rem; font-weight:500; transition:all .25s; white-space:nowrap; }}
    .pf-fbtn:hover {{ border-color:rgba(106,176,76,0.6); color:#fff; }}
    .pf-fbtn.active {{ background:linear-gradient(135deg,#79b32b,#a5d44e); border-color:transparent; color:#000; font-weight:700; }}
    .pf-cat {{ margin-bottom:56px; display:none; }}
    .pf-cat.visible {{ display:block; }}
    .pf-cat-header {{ display:flex; align-items:center; gap:14px; margin-bottom:20px; }}
    .pf-cat-icon {{ width:44px; height:44px; border-radius:12px; background:rgba(106,176,76,0.10); border:1px solid rgba(106,176,76,0.25); display:flex; align-items:center; justify-content:center; font-size:1.2rem; flex-shrink:0; }}
    .pf-cat-title {{ font-family:var(--font-heading); font-size:1.3rem; font-weight:700; color:var(--text); }}
    .pf-cat-badge {{ margin-left:auto; font-size:0.76rem; color:rgba(255,255,255,0.3); background:rgba(255,255,255,0.05); padding:3px 12px; border-radius:50px; }}
    .pf-cat-line {{ height:1px; background:linear-gradient(90deg,rgba(106,176,76,0.4),transparent); margin-bottom:20px; }}
    .pf-cards {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(280px,1fr)); gap:16px; }}
    .pf-placeholder {{ aspect-ratio:16/10; border-radius:16px; border:2px dashed rgba(106,176,76,0.2); background:rgba(106,176,76,0.02); display:flex; flex-direction:column; align-items:center; justify-content:center; gap:12px; cursor:pointer; transition:all .3s; position:relative; overflow:hidden; }}
    .pf-placeholder:hover {{ border-color:rgba(106,176,76,0.5); background:rgba(106,176,76,0.06); transform:translateY(-3px); }}
    .pf-picon {{ width:48px; height:48px; border-radius:50%; background:rgba(106,176,76,0.1); border:1px solid rgba(106,176,76,0.3); display:flex; align-items:center; justify-content:center; font-size:1.2rem; }}
    .pf-ptext {{ color:var(--text-muted); font-size:0.8rem; text-align:center; }}
    .pf-ptext strong {{ display:block; color:var(--text); font-size:0.85rem; margin-bottom:2px; }}
    .pf-badge {{ position:absolute; top:10px; right:10px; background:rgba(106,176,76,0.12); border:1px solid rgba(106,176,76,0.3); color:#6ab04c; font-size:0.66rem; font-weight:600; padding:3px 9px; border-radius:50px; text-transform:uppercase; letter-spacing:0.5px; }}
    .nav-links a.active {{ color:var(--primary) !important; }}
    @media(max-width:600px) {{ .pf-cards {{ grid-template-columns:1fr; }} }}
  </style>
</head>
<body>

  <!-- Exact same navbar as main site -->
  <header class="navbar scrolled" id="navbar">
    <div class="nav-top-line"></div>
    <div class="container nav-inner">
      <a href="index.html" class="logo logo-img">
        <img src="logo.png?v=6" alt="CreativeStudio" class="nav-logo-img" width="246" height="74" />
      </a>
      <nav class="nav-links" id="nav-links">
        <a href="index.html">Home</a>
        <a href="index.html#about">About Us</a>
        <a href="index.html#services">Services</a>
        <a href="portfolio.html" class="active">Portfolio</a>
        <a href="index.html#videos">Videos</a>
        <a href="index.html#contact">Contact</a>
      </nav>
      <a href="index.html#contact" class="nav-cta">Get Started</a>
      <button class="hamburger" id="hamburger" aria-label="Toggle menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  <div class="pf-page">
    <div class="container">
      <div class="pf-hero">
        <div class="pf-hero-tag">Our Work</div>
        <h1>Our <span class="gradient-text">Portfolio</span></h1>
        <p>Explore our completed works across Commercial Production, Content Creation, Documentaries, and more.</p>
      </div>
      <div class="pf-filters">
        <button class="pf-fbtn active" data-filter="all">All Work</button>
        <button class="pf-fbtn" data-filter="commercial">Commercial Production</button>
        <button class="pf-fbtn" data-filter="promo">Promotional Videos</button>
        <button class="pf-fbtn" data-filter="content">Content Creation</button>
        <button class="pf-fbtn" data-filter="documentary">Documentary</button>
        <button class="pf-fbtn" data-filter="social">Social Media</button>
        <button class="pf-fbtn" data-filter="product">Product &amp; Photography</button>
        <button class="pf-fbtn" data-filter="advertising">Advertising</button>
        <button class="pf-fbtn" data-filter="motion">Motion Graphics</button>
        <button class="pf-fbtn" data-filter="creative">Creative Projects</button>
      </div>
{cats_html}
    </div>
  </div>

  <script>
    // Hamburger
    const ham = document.getElementById('hamburger');
    const navEl = document.getElementById('nav-links');
    if (ham) ham.addEventListener('click', () => {{
      ham.classList.toggle('open');
      navEl.classList.toggle('open');
    }});
    // Navbar scroll
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {{
      navbar.classList.toggle('scrolled', window.scrollY > 50);
    }});
    // Filter
    document.querySelectorAll('.pf-fbtn').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('.pf-fbtn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const f = btn.dataset.filter;
        document.querySelectorAll('.pf-cat').forEach(c => {{
          c.classList.toggle('visible', f === 'all' || c.dataset.cat === f);
        }});
      }});
    }});
  </script>
</body>
</html>"""

with open("c:/CreativeStudio/portfolio.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Done!")
