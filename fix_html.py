
import re

html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>CreativeStudio - Premium Digital Agency</title>
  <meta name="description" content="CreativeStudio is a premium digital agency offering Graphic Design, Web Development, Digital Marketing, Video Editing, and UI/UX Design." />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <header class="navbar" id="navbar">
    <div class="container nav-inner">
      <a href="#" class="logo" id="logo-link">
        <span class="logo-icon">&#10022;</span>
        <span class="logo-text">Creative<span class="logo-accent">Studio</span></span>
      </a>
      <nav class="nav-links" id="nav-links">
        <a href="#services" id="nav-services">Services</a>
        <a href="#about" id="nav-about">About</a>
        <a href="#portfolio" id="nav-portfolio">Portfolio</a>
        <a href="#testimonials" id="nav-testi">Testimonials</a>
        <a href="#faq" id="nav-faq">FAQ</a>
        <a href="#contact" id="nav-contact" class="nav-cta">Get Started</a>
      </nav>
      <button class="hamburger" id="hamburger" aria-label="Toggle menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  <section class="hero" id="home">
    <div class="hero-bg"></div>
    <div class="container hero-inner">
      <div class="hero-content">
        <div class="hero-badge"><span class="badge-dot"></span>Available for new projects</div>
        <h1 class="hero-title">We Build Brands That <span class="gradient-text">Dominate</span> The Digital World</h1>
        <p class="hero-sub">CreativeStudio is a full-service digital agency crafting stunning designs, powerful websites and results-driven marketing strategies that set your brand apart.</p>
        <div class="hero-btns">
          <a href="#contact" class="btn btn-primary" id="hero-cta">Start a Project</a>
          <a href="#portfolio" class="btn btn-outline" id="hero-portfolio">View Our Work</a>
        </div>
        <div class="hero-stats">
          <div class="stat"><span class="stat-num" data-target="250">0</span><span class="stat-plus">+</span><span class="stat-label">Projects Done</span></div>
          <div class="stat-divider"></div>
          <div class="stat"><span class="stat-num" data-target="98">0</span><span class="stat-plus">%</span><span class="stat-label">Client Satisfaction</span></div>
          <div class="stat-divider"></div>
          <div class="stat"><span class="stat-num" data-target="7">0</span><span class="stat-plus">+</span><span class="stat-label">Years Experience</span></div>
        </div>
      </div>
      <div class="hero-image">
        <div class="hero-img-glow"></div>
        <img src="team_illustration.jpg" alt="CreativeStudio team" id="hero-img" />
        <div class="hero-float-card card-1"><span class="card-emoji">&#127912;</span><span>Brand Identity</span></div>
        <div class="hero-float-card card-2"><span class="card-emoji">&#128640;</span><span>500% ROI Growth</span></div>
      </div>
    </div>
    <div class="hero-scroll-hint"><span>Scroll Down</span><div class="scroll-arrow"></div></div>
  </section>

  <div class="ticker-wrap">
    <div class="ticker-track">
      <span>Graphic Design</span><span class="sep">&#10022;</span>
      <span>Web Development</span><span class="sep">&#10022;</span>
      <span>Digital Marketing</span><span class="sep">&#10022;</span>
      <span>Video Editing</span><span class="sep">&#10022;</span>
      <span>UI/UX Design</span><span class="sep">&#10022;</span>
      <span>Brand Strategy</span><span class="sep">&#10022;</span>
      <span>SEO Optimization</span><span class="sep">&#10022;</span>
      <span>Social Media</span><span class="sep">&#10022;</span>
      <span>Graphic Design</span><span class="sep">&#10022;</span>
      <span>Web Development</span><span class="sep">&#10022;</span>
      <span>Digital Marketing</span><span class="sep">&#10022;</span>
      <span>Video Editing</span><span class="sep">&#10022;</span>
    </div>
  </div>

  <section class="section services" id="services">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">What We Do</span>
        <h2 class="section-title">Services That <span class="gradient-text">Scale</span> Your Brand</h2>
        <p class="section-sub">From concept to launch &mdash; we handle every pixel, every line of code, every campaign.</p>
      </div>
      <div class="services-grid">
        <div class="service-card" id="svc-graphic">
          <div class="service-icon svc-icon-graphic"></div>
          <h3>Graphic Design</h3>
          <p>Stunning visuals that tell your brand story &mdash; logos, branding, social graphics, and print materials that leave a lasting impression.</p>
          <a href="#contact" class="service-link">Get Started &rarr;</a>
          <div class="service-card-glow"></div>
        </div>
        <div class="service-card featured" id="svc-web">
          <div class="service-badge">Most Popular</div>
          <div class="service-icon svc-icon-web"></div>
          <h3>Web Development</h3>
          <p>Fast, responsive, stunning websites built with modern tech. From landing pages to full e-commerce platforms tailored to convert.</p>
          <a href="#contact" class="service-link">Get Started &rarr;</a>
          <div class="service-card-glow"></div>
        </div>
        <div class="service-card" id="svc-marketing">
          <div class="service-icon svc-icon-mkt"></div>
          <h3>Digital Marketing</h3>
          <p>Data-driven campaigns that generate real results. SEO, PPC, email marketing, and social media strategies that grow your revenue.</p>
          <a href="#contact" class="service-link">Get Started &rarr;</a>
          <div class="service-card-glow"></div>
        </div>
        <div class="service-card" id="svc-video">
          <div class="service-icon svc-icon-video"></div>
          <h3>Video Editing</h3>
          <p>Cinematic brand videos, reels, ads, and YouTube content edited to perfection. Keep your audience hooked every second.</p>
          <a href="#contact" class="service-link">Get Started &rarr;</a>
          <div class="service-card-glow"></div>
        </div>
        <div class="service-card" id="svc-uiux">
          <div class="service-icon svc-icon-ui"></div>
          <h3>UI/UX Design</h3>
          <p>User-first designs that look beautiful and feel intuitive. Wireframes, prototypes, and polished interfaces your users will love.</p>
          <a href="#contact" class="service-link">Get Started &rarr;</a>
          <div class="service-card-glow"></div>
        </div>
        <div class="service-card" id="svc-seo">
          <div class="service-icon svc-icon-seo"></div>
          <h3>SEO &amp; Strategy</h3>
          <p>Rank higher, get found faster. Our SEO specialists optimize your online presence with proven tactics that drive organic traffic.</p>
          <a href="#contact" class="service-link">Get Started &rarr;</a>
          <div class="service-card-glow"></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section about" id="about">
    <div class="container about-inner">
      <div class="about-image-wrap">
        <div class="about-img-bg"></div>
        <img src="team_illustration.jpg" alt="About CreativeStudio" id="about-img" />
        <div class="about-exp-badge">
          <span class="exp-num">7+</span>
          <span class="exp-label">Years of Excellence</span>
        </div>
      </div>
      <div class="about-content">
        <span class="section-tag">About Us</span>
        <h2 class="section-title">We Are <span class="gradient-text">CreativeStudio</span></h2>
        <p class="about-desc">Born from passion, driven by results. CreativeStudio is a team of designers, developers, and digital marketers who believe every brand deserves world-class creative work.</p>
        <p class="about-desc">We combine bold creativity with data-backed strategy to build brands that perform exceptionally in the digital world.</p>
        <div class="about-features">
          <div class="feature-item"><span class="feature-check">&#10003;</span><span>Results-oriented approach to every project</span></div>
          <div class="feature-item"><span class="feature-check">&#10003;</span><span>Dedicated project manager for each client</span></div>
          <div class="feature-item"><span class="feature-check">&#10003;</span><span>Transparent reporting and real-time analytics</span></div>
          <div class="feature-item"><span class="feature-check">&#10003;</span><span>Flexible packages for startups to enterprises</span></div>
        </div>
        <a href="#contact" class="btn btn-primary" id="about-cta">Work With Us</a>
      </div>
    </div>
  </section>

  <section class="section process" id="process">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">How We Work</span>
        <h2 class="section-title">Our <span class="gradient-text">Process</span></h2>
        <p class="section-sub">A streamlined workflow designed to deliver results on time, every time.</p>
      </div>
      <div class="process-steps">
        <div class="process-step" id="step-1">
          <div class="step-num">01</div>
          <div class="step-icon step-icon-1"></div>
          <h3>Discovery</h3>
          <p>We deep-dive into your brand, audience, goals, and competitors to build a clear strategic foundation.</p>
        </div>
        <div class="process-arrow">&rarr;</div>
        <div class="process-step" id="step-2">
          <div class="step-num">02</div>
          <div class="step-icon step-icon-2"></div>
          <h3>Strategy</h3>
          <p>We craft a custom roadmap &mdash; creative direction, tech stack, campaign plan &mdash; aligned to your objectives.</p>
        </div>
        <div class="process-arrow">&rarr;</div>
        <div class="process-step" id="step-3">
          <div class="step-num">03</div>
          <div class="step-icon step-icon-3"></div>
          <h3>Execution</h3>
          <p>Our team brings the strategy to life with precision, creativity, and speed &mdash; keeping you in the loop.</p>
        </div>
        <div class="process-arrow">&rarr;</div>
        <div class="process-step" id="step-4">
          <div class="step-num">04</div>
          <div class="step-icon step-icon-4"></div>
          <h3>Domination</h3>
          <p>We launch, measure, optimize, and scale &mdash; turning your brand into an industry leader.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section portfolio" id="portfolio">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Our Work</span>
        <h2 class="section-title">Featured <span class="gradient-text">Portfolio</span></h2>
        <p class="section-sub">A glimpse of the brands we have helped transform and grow.</p>
      </div>
      <div class="portfolio-filter">
        <button class="filter-btn active" data-filter="all" id="filter-all">All</button>
        <button class="filter-btn" data-filter="design" id="filter-design">Design</button>
        <button class="filter-btn" data-filter="web" id="filter-web">Web</button>
        <button class="filter-btn" data-filter="marketing" id="filter-marketing">Marketing</button>
      </div>
      <div class="portfolio-grid" id="portfolio-grid">
        <div class="portfolio-item" data-category="design">
          <div class="portfolio-img-wrap">
            <div class="portfolio-placeholder p1"><span class="p-icon p-icon-1"></span><p>Brand Identity</p></div>
            <div class="portfolio-overlay">
              <span class="portfolio-tag">Graphic Design</span>
              <h4>Luxe Cosmetics Brand</h4>
              <p>Full brand identity including logo, palette and packaging</p>
              <a href="#contact" class="btn btn-sm" id="p-item-1">View Project</a>
            </div>
          </div>
        </div>
        <div class="portfolio-item" data-category="web">
          <div class="portfolio-img-wrap">
            <div class="portfolio-placeholder p2"><span class="p-icon p-icon-2"></span><p>E-Commerce Platform</p></div>
            <div class="portfolio-overlay">
              <span class="portfolio-tag">Web Development</span>
              <h4>ShopNow Platform</h4>
              <p>High-converting e-commerce store with 3x sales increase</p>
              <a href="#contact" class="btn btn-sm" id="p-item-2">View Project</a>
            </div>
          </div>
        </div>
        <div class="portfolio-item" data-category="marketing">
          <div class="portfolio-img-wrap">
            <div class="portfolio-placeholder p3"><span class="p-icon p-icon-3"></span><p>Digital Campaign</p></div>
            <div class="portfolio-overlay">
              <span class="portfolio-tag">Digital Marketing</span>
              <h4>TechStart Growth</h4>
              <p>500% ROI increase via targeted social and PPC campaigns</p>
              <a href="#contact" class="btn btn-sm" id="p-item-3">View Project</a>
            </div>
          </div>
        </div>
        <div class="portfolio-item" data-category="design">
          <div class="portfolio-img-wrap">
            <div class="portfolio-placeholder p4"><span class="p-icon p-icon-4"></span><p>UI/UX Design</p></div>
            <div class="portfolio-overlay">
              <span class="portfolio-tag">UI/UX Design</span>
              <h4>FinTrack App</h4>
              <p>Finance app UI with 4.8 star user satisfaction rating</p>
              <a href="#contact" class="btn btn-sm" id="p-item-4">View Project</a>
            </div>
          </div>
        </div>
        <div class="portfolio-item" data-category="web">
          <div class="portfolio-img-wrap">
            <div class="portfolio-placeholder p5"><span class="p-icon p-icon-5"></span><p>Corporate Website</p></div>
            <div class="portfolio-overlay">
              <span class="portfolio-tag">Web Development</span>
              <h4>Global Corp Site</h4>
              <p>Multi-language corporate website with CMS integration</p>
              <a href="#contact" class="btn btn-sm" id="p-item-5">View Project</a>
            </div>
          </div>
        </div>
        <div class="portfolio-item" data-category="marketing">
          <div class="portfolio-img-wrap">
            <div class="portfolio-placeholder p6"><span class="p-icon p-icon-6"></span><p>Video Campaign</p></div>
            <div class="portfolio-overlay">
              <span class="portfolio-tag">Video Editing</span>
              <h4>ViralBoost Campaign</h4>
              <p>2M+ views brand video with cinematic production quality</p>
              <a href="#contact" class="btn btn-sm" id="p-item-6">View Project</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section testimonials" id="testimonials">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">Testimonials</span>
        <h2 class="section-title">What Our Clients <span class="gradient-text">Say</span></h2>
        <p class="section-sub">Don't take our word for it &mdash; hear from the brands we have helped grow.</p>
      </div>
      <div class="testimonials-wrapper">
        <div class="testimonials-track" id="testi-track">
          <div class="testimonial-card active" id="testi-1">
            <div class="testi-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
            <p class="testi-text">"CreativeStudio transformed our brand completely. Their design team is world-class and the results speak for themselves. Website traffic tripled within 60 days!"</p>
            <div class="testi-author">
              <div class="testi-avatar" style="background:linear-gradient(135deg,#7c3aed,#a78bfa)">IJ</div>
              <div><strong>Iraj Janali</strong><span>Founder at Janco</span></div>
            </div>
          </div>
          <div class="testimonial-card" id="testi-2">
            <div class="testi-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
            <p class="testi-text">"I worked with CreativeStudio on our visual design and I am blown away by the attention to detail. Their creativity is unmatched and the team is incredibly responsive!"</p>
            <div class="testi-author">
              <div class="testi-avatar" style="background:linear-gradient(135deg,#0891b2,#67e8f9)">RT</div>
              <div><strong>Randy Taggart</strong><span>Sr. Photographer at WACC</span></div>
            </div>
          </div>
          <div class="testimonial-card" id="testi-3">
            <div class="testi-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
            <p class="testi-text">"They handle all our design needs and recently developed our website. Excellent services, outstanding after-sales support, and budget-friendly. Best agency ever!"</p>
            <div class="testi-author">
              <div class="testi-avatar" style="background:linear-gradient(135deg,#d97706,#fbbf24)">NM</div>
              <div><strong>Nayeem Mia</strong><span>Founder at HNS TECH</span></div>
            </div>
          </div>
          <div class="testimonial-card" id="testi-4">
            <div class="testi-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
            <p class="testi-text">"Working with CreativeStudio was the best business decision this year. Their strategic approach delivered 400% ROI. Absolutely phenomenal team!"</p>
            <div class="testi-author">
              <div class="testi-avatar" style="background:linear-gradient(135deg,#059669,#6ee7b7)">SK</div>
              <div><strong>Sarah Kim</strong><span>CEO at GreenTech Solutions</span></div>
            </div>
          </div>
        </div>
        <div class="testi-controls">
          <button class="testi-btn" id="testi-prev">&#8249;</button>
          <div class="testi-dots" id="testi-dots">
            <span class="testi-dot active" data-idx="0"></span>
            <span class="testi-dot" data-idx="1"></span>
            <span class="testi-dot" data-idx="2"></span>
            <span class="testi-dot" data-idx="3"></span>
          </div>
          <button class="testi-btn" id="testi-next">&#8250;</button>
        </div>
      </div>
    </div>
  </section>

  <section class="section faq" id="faq">
    <div class="container faq-inner">
      <div class="faq-left">
        <span class="section-tag">FAQ</span>
        <h2 class="section-title">Frequently <span class="gradient-text">Asked</span> Questions</h2>
        <p class="faq-desc">Got questions? We have answers. If you don't see yours here, just reach out!</p>
        <div class="faq-contact-box">
          <div class="faq-contact-avatar">&#128075;</div>
          <div><p>Still have questions?</p><a href="#contact" class="btn btn-primary btn-sm" id="faq-cta">Ask Us Anything</a></div>
        </div>
      </div>
      <div class="faq-right">
        <div class="faq-item" id="faq-1">
          <button class="faq-question">What services does CreativeStudio offer?<span class="faq-icon">+</span></button>
          <div class="faq-answer"><p>We specialize in Graphic Design, Web Development, Digital Marketing, Video Editing, UI/UX Design &mdash; all tailored to help your brand dominate the industry.</p></div>
        </div>
        <div class="faq-item" id="faq-2">
          <button class="faq-question">Why choose CreativeStudio over competitors?<span class="faq-icon">+</span></button>
          <div class="faq-answer"><p>Our team combines data-driven strategies, bold creative storytelling, and relentless execution. We deliver results that make your brand stand out and scale fast.</p></div>
        </div>
        <div class="faq-item" id="faq-3">
          <button class="faq-question">How do you measure campaign success?<span class="faq-icon">+</span></button>
          <div class="faq-answer"><p>Through real-time analytics (ROI, engagement, conversions) and transparent reports &mdash; because we believe in results, not just activity.</p></div>
        </div>
        <div class="faq-item" id="faq-4">
          <button class="faq-question">What is your pricing structure?<span class="faq-icon">+</span></button>
          <div class="faq-answer"><p>We offer customized packages based on your goals and budget. Book a free consultation to get a tailored quote for your project!</p></div>
        </div>
        <div class="faq-item" id="faq-5">
          <button class="faq-question">How long before we see results?<span class="faq-icon">+</span></button>
          <div class="faq-answer"><p>Most clients see traction within 30&ndash;60 days, but we optimize continuously for long-term growth and sustained performance.</p></div>
        </div>
        <div class="faq-item" id="faq-6">
          <button class="faq-question">Do you work with startups and SMEs?<span class="faq-icon">+</span></button>
          <div class="faq-answer"><p>Absolutely! We help businesses of all sizes &mdash; from local startups to global brands &mdash; punch above their weight in the digital space.</p></div>
        </div>
        <div class="faq-item" id="faq-7">
          <button class="faq-question">What is your client onboarding process?<span class="faq-icon">+</span></button>
          <div class="faq-answer"><p>Simple: Discovery &rarr; Strategy &rarr; Execution &rarr; Domination. We keep you in the loop at every single step of the journey.</p></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section contact" id="contact">
    <div class="container contact-inner">
      <div class="contact-left">
        <span class="section-tag">Contact Us</span>
        <h2 class="section-title">Have a Great <span class="gradient-text">Idea?</span></h2>
        <p class="contact-desc">Let us turn it into something amazing. Drop us a message and we will get back to you within 24 hours.</p>
        <div class="contact-info">
          <div class="contact-info-item" id="contact-email">
            <span class="contact-info-icon">&#128231;</span>
            <div><strong>Email Us</strong><a href="mailto:hello@creativestudio.com">hello@creativestudio.com</a></div>
          </div>
          <div class="contact-info-item" id="contact-phone">
            <span class="contact-info-icon">&#128222;</span>
            <div><strong>Call Us</strong><a href="tel:+8801700000000">+880 1700 000 000</a></div>
          </div>
          <div class="contact-info-item" id="contact-wa">
            <span class="contact-info-icon">&#128172;</span>
            <div><strong>WhatsApp</strong><a href="https://wa.me/8801700000000" target="_blank" rel="noopener">Chat Now</a></div>
          </div>
        </div>
        <div class="contact-socials">
          <a href="#" class="social-link" id="social-fb" aria-label="Facebook">FB</a>
          <a href="#" class="social-link" id="social-ig" aria-label="Instagram">IG</a>
          <a href="#" class="social-link" id="social-li" aria-label="LinkedIn">LI</a>
          <a href="#" class="social-link" id="social-yt" aria-label="YouTube">YT</a>
        </div>
      </div>
      <div class="contact-right">
        <form class="contact-form" id="contact-form" novalidate>
          <div class="form-row">
            <div class="form-group">
              <label for="form-name">Your Name</label>
              <input type="text" id="form-name" name="name" placeholder="John Doe" required />
            </div>
            <div class="form-group">
              <label for="form-email">Email Address</label>
              <input type="email" id="form-email" name="email" placeholder="john@example.com" required />
            </div>
          </div>
          <div class="form-group">
            <label for="form-service">Service Needed</label>
            <select id="form-service" name="service">
              <option value="">Select a service...</option>
              <option value="graphic">Graphic Design</option>
              <option value="web">Web Development</option>
              <option value="marketing">Digital Marketing</option>
              <option value="video">Video Editing</option>
              <option value="uiux">UI/UX Design</option>
              <option value="seo">SEO and Strategy</option>
              <option value="other">Other</option>
            </select>
          </div>
          <div class="form-group">
            <label for="form-budget">Budget Range</label>
            <select id="form-budget" name="budget">
              <option value="">Select budget...</option>
              <option value="500">$500 - $1,000</option>
              <option value="1000">$1,000 - $5,000</option>
              <option value="5000">$5,000 - $10,000</option>
              <option value="10000">$10,000+</option>
            </select>
          </div>
          <div class="form-group">
            <label for="form-message">Project Details</label>
            <textarea id="form-message" name="message" rows="4" placeholder="Tell us about your project, goals, and timeline..." required></textarea>
          </div>
          <button type="submit" class="btn btn-primary btn-full" id="form-submit">Send Message &#128640;</button>
          <div class="form-success" id="form-success" style="display:none">&#9989; Thank you! We will be in touch within 24 hours.</div>
        </form>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="footer-top">
      <div class="container footer-grid">
        <div class="footer-brand">
          <a href="#" class="logo"><span class="logo-icon">&#10022;</span><span class="logo-text">Creative<span class="logo-accent">Studio</span></span></a>
          <p>Crafting digital experiences that dominate industries and transform brands worldwide.</p>
        </div>
        <div class="footer-links">
          <h4>Services</h4>
          <a href="#services">Graphic Design</a>
          <a href="#services">Web Development</a>
          <a href="#services">Digital Marketing</a>
          <a href="#services">Video Editing</a>
          <a href="#services">UI/UX Design</a>
        </div>
        <div class="footer-links">
          <h4>Company</h4>
          <a href="#about">About Us</a>
          <a href="#portfolio">Portfolio</a>
          <a href="#testimonials">Testimonials</a>
          <a href="#faq">FAQ</a>
          <a href="#contact">Contact</a>
        </div>
        <div class="footer-newsletter">
          <h4>Stay Updated</h4>
          <p>Subscribe for tips, case studies and exclusive offers.</p>
          <form class="newsletter-form" id="newsletter-form">
            <input type="email" id="nl-email" placeholder="your@email.com" aria-label="Newsletter email" />
            <button type="submit" id="nl-submit">&rarr;</button>
          </form>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="container footer-bottom-inner">
        <p>&copy; 2026 CreativeStudio. All rights reserved.</p>
        <div class="footer-bottom-links">
          <a href="#">Privacy Policy</a>
          <a href="#">Terms of Service</a>
        </div>
      </div>
    </div>
  </footer>

  <a href="#home" class="back-to-top" id="back-to-top" aria-label="Back to top">&#8679;</a>
  <script src="script.js"></script>
</body>
</html>'''

with open('c:/CreativeStudio/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('index.html written successfully')
