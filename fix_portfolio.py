import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_section = '''  <section class="section portfolio" id="portfolio">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Our Work</span>
        <h2 class="section-title">Featured <span class="gradient-text">Portfolio</span></h2>
        <p class="section-sub">A glimpse of the brands we have helped transform and grow.</p>
      </div>
    </div>

    <!-- ROW 1: RIGHT -->
    <div class="pf-marquee-wrap">
      <div class="pf-marquee pf-row-right">
        <div class="pf-card"><div class="pf-card-inner p1"><span class="p-icon p-icon-1"></span><div class="pf-card-info"><span class="pf-tag">Graphic Design</span><h4>Luxe Cosmetics Brand</h4><p>Full brand identity &mdash; logo, palette &amp; packaging</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p2"><span class="p-icon p-icon-2"></span><div class="pf-card-info"><span class="pf-tag">Web Development</span><h4>ShopNow Platform</h4><p>High-converting e-commerce with 3x sales increase</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p3"><span class="p-icon p-icon-3"></span><div class="pf-card-info"><span class="pf-tag">Digital Marketing</span><h4>TechStart Growth</h4><p>500% ROI via targeted social and PPC campaigns</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p4"><span class="p-icon p-icon-4"></span><div class="pf-card-info"><span class="pf-tag">UI/UX Design</span><h4>FinTrack App</h4><p>Finance app UI with 4.8&#9733; user satisfaction</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p5"><span class="p-icon p-icon-5"></span><div class="pf-card-info"><span class="pf-tag">Web Development</span><h4>Global Corp Site</h4><p>Multi-language corporate website with CMS</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p6"><span class="p-icon p-icon-6"></span><div class="pf-card-info"><span class="pf-tag">Video Editing</span><h4>ViralBoost Campaign</h4><p>2M+ views brand video &mdash; cinematic quality</p></div></div></div>
        <!-- duplicate for seamless loop -->
        <div class="pf-card"><div class="pf-card-inner p1"><span class="p-icon p-icon-1"></span><div class="pf-card-info"><span class="pf-tag">Graphic Design</span><h4>Luxe Cosmetics Brand</h4><p>Full brand identity &mdash; logo, palette &amp; packaging</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p2"><span class="p-icon p-icon-2"></span><div class="pf-card-info"><span class="pf-tag">Web Development</span><h4>ShopNow Platform</h4><p>High-converting e-commerce with 3x sales increase</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p3"><span class="p-icon p-icon-3"></span><div class="pf-card-info"><span class="pf-tag">Digital Marketing</span><h4>TechStart Growth</h4><p>500% ROI via targeted social and PPC campaigns</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p4"><span class="p-icon p-icon-4"></span><div class="pf-card-info"><span class="pf-tag">UI/UX Design</span><h4>FinTrack App</h4><p>Finance app UI with 4.8&#9733; user satisfaction</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p5"><span class="p-icon p-icon-5"></span><div class="pf-card-info"><span class="pf-tag">Web Development</span><h4>Global Corp Site</h4><p>Multi-language corporate website with CMS</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p6"><span class="p-icon p-icon-6"></span><div class="pf-card-info"><span class="pf-tag">Video Editing</span><h4>ViralBoost Campaign</h4><p>2M+ views brand video &mdash; cinematic quality</p></div></div></div>
      </div>
    </div>

    <!-- ROW 2: LEFT -->
    <div class="pf-marquee-wrap">
      <div class="pf-marquee pf-row-left">
        <div class="pf-card"><div class="pf-card-inner p4"><span class="p-icon p-icon-4"></span><div class="pf-card-info"><span class="pf-tag">UI/UX Design</span><h4>FinTrack App</h4><p>Finance app UI with 4.8&#9733; user satisfaction</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p5"><span class="p-icon p-icon-5"></span><div class="pf-card-info"><span class="pf-tag">Web Development</span><h4>Global Corp Site</h4><p>Multi-language corporate website with CMS</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p6"><span class="p-icon p-icon-6"></span><div class="pf-card-info"><span class="pf-tag">Video Editing</span><h4>ViralBoost Campaign</h4><p>2M+ views brand video &mdash; cinematic quality</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p1"><span class="p-icon p-icon-1"></span><div class="pf-card-info"><span class="pf-tag">Graphic Design</span><h4>Luxe Cosmetics Brand</h4><p>Full brand identity &mdash; logo, palette &amp; packaging</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p2"><span class="p-icon p-icon-2"></span><div class="pf-card-info"><span class="pf-tag">Web Development</span><h4>ShopNow Platform</h4><p>High-converting e-commerce with 3x sales increase</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p3"><span class="p-icon p-icon-3"></span><div class="pf-card-info"><span class="pf-tag">Digital Marketing</span><h4>TechStart Growth</h4><p>500% ROI via targeted social and PPC campaigns</p></div></div></div>
        <!-- duplicate -->
        <div class="pf-card"><div class="pf-card-inner p4"><span class="p-icon p-icon-4"></span><div class="pf-card-info"><span class="pf-tag">UI/UX Design</span><h4>FinTrack App</h4><p>Finance app UI with 4.8&#9733; user satisfaction</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p5"><span class="p-icon p-icon-5"></span><div class="pf-card-info"><span class="pf-tag">Web Development</span><h4>Global Corp Site</h4><p>Multi-language corporate website with CMS</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p6"><span class="p-icon p-icon-6"></span><div class="pf-card-info"><span class="pf-tag">Video Editing</span><h4>ViralBoost Campaign</h4><p>2M+ views brand video &mdash; cinematic quality</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p1"><span class="p-icon p-icon-1"></span><div class="pf-card-info"><span class="pf-tag">Graphic Design</span><h4>Luxe Cosmetics Brand</h4><p>Full brand identity &mdash; logo, palette &amp; packaging</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p2"><span class="p-icon p-icon-2"></span><div class="pf-card-info"><span class="pf-tag">Web Development</span><h4>ShopNow Platform</h4><p>High-converting e-commerce with 3x sales increase</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p3"><span class="p-icon p-icon-3"></span><div class="pf-card-info"><span class="pf-tag">Digital Marketing</span><h4>TechStart Growth</h4><p>500% ROI via targeted social and PPC campaigns</p></div></div></div>
      </div>
    </div>

    <!-- ROW 3: RIGHT (slower) -->
    <div class="pf-marquee-wrap">
      <div class="pf-marquee pf-row-right pf-row-slower">
        <div class="pf-card"><div class="pf-card-inner p3"><span class="p-icon p-icon-3"></span><div class="pf-card-info"><span class="pf-tag">Digital Marketing</span><h4>TechStart Growth</h4><p>500% ROI via targeted social and PPC campaigns</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p6"><span class="p-icon p-icon-6"></span><div class="pf-card-info"><span class="pf-tag">Video Editing</span><h4>ViralBoost Campaign</h4><p>2M+ views brand video &mdash; cinematic quality</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p1"><span class="p-icon p-icon-1"></span><div class="pf-card-info"><span class="pf-tag">Graphic Design</span><h4>Luxe Cosmetics Brand</h4><p>Full brand identity &mdash; logo, palette &amp; packaging</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p4"><span class="p-icon p-icon-4"></span><div class="pf-card-info"><span class="pf-tag">UI/UX Design</span><h4>FinTrack App</h4><p>Finance app UI with 4.8&#9733; user satisfaction</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p2"><span class="p-icon p-icon-2"></span><div class="pf-card-info"><span class="pf-tag">Web Development</span><h4>ShopNow Platform</h4><p>High-converting e-commerce with 3x sales increase</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p5"><span class="p-icon p-icon-5"></span><div class="pf-card-info"><span class="pf-tag">Web Development</span><h4>Global Corp Site</h4><p>Multi-language corporate website with CMS</p></div></div></div>
        <!-- duplicate -->
        <div class="pf-card"><div class="pf-card-inner p3"><span class="p-icon p-icon-3"></span><div class="pf-card-info"><span class="pf-tag">Digital Marketing</span><h4>TechStart Growth</h4><p>500% ROI via targeted social and PPC campaigns</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p6"><span class="p-icon p-icon-6"></span><div class="pf-card-info"><span class="pf-tag">Video Editing</span><h4>ViralBoost Campaign</h4><p>2M+ views brand video &mdash; cinematic quality</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p1"><span class="p-icon p-icon-1"></span><div class="pf-card-info"><span class="pf-tag">Graphic Design</span><h4>Luxe Cosmetics Brand</h4><p>Full brand identity &mdash; logo, palette &amp; packaging</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p4"><span class="p-icon p-icon-4"></span><div class="pf-card-info"><span class="pf-tag">UI/UX Design</span><h4>FinTrack App</h4><p>Finance app UI with 4.8&#9733; user satisfaction</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p2"><span class="p-icon p-icon-2"></span><div class="pf-card-info"><span class="pf-tag">Web Development</span><h4>ShopNow Platform</h4><p>High-converting e-commerce with 3x sales increase</p></div></div></div>
        <div class="pf-card"><div class="pf-card-inner p5"><span class="p-icon p-icon-5"></span><div class="pf-card-info"><span class="pf-tag">Web Development</span><h4>Global Corp Site</h4><p>Multi-language corporate website with CMS</p></div></div></div>
      </div>
    </div>
  </section>'''

# Use regex to replace the entire portfolio section
result = re.sub(
    r'<section class="section portfolio" id="portfolio">.*?</section>',
    new_section,
    content,
    flags=re.DOTALL
)

if result == content:
    print("ERROR: No replacement made!")
else:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(result)
    print("SUCCESS: Portfolio section replaced!")
