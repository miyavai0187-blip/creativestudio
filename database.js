const fs    = require('fs');
const path  = require('path');
const bcrypt = require('bcryptjs');

// ── Default site content ───────────────────────────────────────────────────
const DEFAULT_CONTENT = {
  navbar: {
    logo: 'logo.png',
    links: [
      { label: 'Home', href: '#home' },
      { label: 'About Us', href: '#about' },
      { label: 'Services', href: '#services' },
      { label: 'Portfolio', href: 'portfolio.html' },
      { label: 'Videos', href: '#videos' },
      { label: 'Contact', href: '#contact' }
    ],
    ctaText: 'Get Started',
    ctaHref: '#contact'
  },
  hero: {
    badge: 'Digital Creative Agency',
    titleLine1: 'YOUR BUSINESS,',
    titleLine2: 'OUR RESPONSIBILITY',
    subtitle: 'Creative Media & Digital Solutions for Businesses, Brands & Professionals.',
    btn1Text: 'Book Now', btn1Href: '#contact',
    btn2Text: 'View Work', btn2Href: 'portfolio.html',
    whatsappText: 'WhatsApp Live Chat', whatsappNumber: '8801613595594',
    backgroundVideo: '', backgroundImage: 'hero_bg.jpg',
    stats: [
      { number: '250', suffix: '+', label: 'Projects Done' },
      { number: '98',  suffix: '%', label: 'Client Satisfaction' },
      { number: '7',   suffix: '+', label: 'Years Experience' }
    ]
  },
  ticker: {
    visible: true,
    items: ['Commercial Production','Content Creation','Documentary Production','Advertising','Motion Graphics','Graphic Design','Website Development']
  },
  about: {
    tag: 'About Us',
    heading: 'We craft digital experiences that',
    headingHighlight: 'elevate brands',
    text: 'CreativeStudio is a full-service digital creative agency specializing in commercial production, content creation, and brand strategy.',
    videoUrl: 'https://www.youtube.com/embed/dQw4w9WgXcQ',
    teamImage: 'team_illustration.jpg',
    stats: [
      { number: '250+', label: 'Projects' },
      { number: '98%',  label: 'Satisfaction' },
      { number: '50+',  label: 'Clients' },
      { number: '7+',   label: 'Years' }
    ]
  },
  services: {
    tag: 'Our Services', heading: 'What We', headingHighlight: 'Offer',
    subtitle: 'End-to-end creative solutions tailored for your brand.',
    items: [
      { icon: '🎬', title: 'Commercial Production', desc: 'High-quality commercial videos that captivate audiences and drive results.' },
      { icon: '📱', title: 'Content Creation',      desc: 'Engaging social media content, reels, and digital assets.' },
      { icon: '🎨', title: 'Graphic Design',        desc: 'Stunning visuals, brand identity, and marketing materials.' },
      { icon: '💻', title: 'Website Development',   desc: 'Modern, responsive websites that convert visitors into customers.' },
      { icon: '📢', title: 'Digital Marketing',     desc: 'Strategic campaigns across social media and search engines.' },
      { icon: '🎭', title: 'Motion Graphics',       desc: 'Dynamic animations that bring your brand story to life.' }
    ]
  },
  testimonials: {
    tag: 'Testimonials', heading: "Don't take our word for it",
    items: [
      { name: 'Iraj Janali',    role: 'Founder at Janco',          text: 'CreativeStudio transformed our brand completely. Website traffic tripled within 60 days!', initials: 'IJ', color: '#7c3aed' },
      { name: 'Randy Taggart', role: 'Sr. Photographer at WACC',  text: 'Their creativity is unmatched!', initials: 'RT', color: '#0891b2' },
      { name: 'Nayeem Mia',    role: 'Founder at HNS TECH',       text: 'Excellent services and budget-friendly.', initials: 'NM', color: '#d97706' },
      { name: 'Sarah Kim',     role: 'CEO at GreenTech Solutions', text: 'Their strategic approach delivered 400% ROI.', initials: 'SK', color: '#059669' }
    ]
  },
  contact: {
    tag: 'Contact Us', heading: "Let's Work", headingHighlight: 'Together',
    subtitle: 'Ready to elevate your brand? Get in touch today.',
    phone: '+880 161 359 5594', email: 'hello@creativestudio.com',
    address: 'Dhaka, Bangladesh', whatsapp: '8801613595594',
    socials: [
      { platform: 'Facebook',  url: '#', icon: 'fb' },
      { platform: 'Instagram', url: '#', icon: 'ig' },
      { platform: 'YouTube',   url: '#', icon: 'yt' },
      { platform: 'LinkedIn',  url: '#', icon: 'li' }
    ]
  },
  footer: {
    tagline: 'Crafting digital experiences that elevate brands and drive results.',
    copyright: '© 2026 Creative Studio. All rights reserved.'
  },
  portfolioPage: {
    tag: 'Our Work',
    titleMain: 'Our',
    titleHighlight: 'Portfolio',
    subtitle: 'Explore our completed works across Commercial Production, Content Creation, Documentaries, and more.'
  },
  sections: {
    order: ['hero','ticker','about','services','portfolio','videos','testimonials','contact'],
    visibility: { hero:true, ticker:true, about:true, services:true, portfolio:true, videos:true, testimonials:true, contact:true }
  }
};

// ── JSON DB class ─────────────────────────────────────────────────────────
class JsonDB {
  constructor(dataDir) {
    this.dataDir = dataDir;
    this.contentFile       = path.join(dataDir, 'content.json');
    this.portfolioFile     = path.join(dataDir, 'portfolio.json');
    this.mediaFile         = path.join(dataDir, 'media.json');
    this.usersFile         = path.join(dataDir, 'users.json');
    this.messagesFile      = path.join(dataDir, 'messages.json');
    this.testimonialsFile  = path.join(dataDir, 'testimonials.json');
    this._init();
  }

  _init() {
    // Seed content
    if (!fs.existsSync(this.contentFile)) {
      this._write(this.contentFile, DEFAULT_CONTENT);
      console.log('✅ Default content seeded');
    }
    // Seed portfolio
    if (!fs.existsSync(this.portfolioFile)) this._write(this.portfolioFile, []);
    // Seed media
    if (!fs.existsSync(this.mediaFile))     this._write(this.mediaFile, []);
    // Seed messages
    if (!fs.existsSync(this.messagesFile))  this._write(this.messagesFile, []);
    // Seed testimonials
    if (!fs.existsSync(this.testimonialsFile)) {
      this._write(this.testimonialsFile, [
        { id:1, name:'Iraj Janali', role:'Founder at Janco', review:'I worked with CreativeStudio, their visual design teams did an excellent job on my project. I am currently working with them and look forward to collaborating on more projects in the future. Their creativity and attention just wow. I highly recommend their services!', photo:'', visible:1, sort_order:1 },
        { id:2, name:'Randy Taggart', role:'Sr. Photographer at WACC', review:'I worked with CreativeStudio on our visual design and I am blown away by the attention to detail. Their creativity is unmatched and the team is incredibly responsive. Highly recommend!', photo:'', visible:1, sort_order:2 },
        { id:3, name:'Nayeem Mia', role:'Founder at HNS TECH', review:'They handle all our design needs and recently developed our website. Excellent services, outstanding after-sales support, and budget-friendly. The best agency we have ever worked with!', photo:'', visible:1, sort_order:3 },
        { id:4, name:'Sarah Kim', role:'CEO at GreenTech Solutions', review:'Working with CreativeStudio was the best business decision this year. Their strategic approach and creative vision delivered amazing results. Absolutely phenomenal team!', photo:'', visible:1, sort_order:4 }
      ]);
    }
    // Seed admin user
    if (!fs.existsSync(this.usersFile)) {
      const hash = bcrypt.hashSync(process.env.ADMIN_PASSWORD || 'admin123', 10);
      this._write(this.usersFile, [{ id: 1, username: 'admin', password: hash }]);
      console.log('✅ Default admin: admin / admin123');
    }
  }

  _read(file)       { return JSON.parse(fs.readFileSync(file, 'utf8')); }
  _write(file, data){ fs.writeFileSync(file, JSON.stringify(data, null, 2), 'utf8'); }

  // ── Content ────────────────────────────────────────────────────────────
  getSiteData()      { return this._read(this.contentFile); }
  getContent(key)    { const d = this._read(this.contentFile); return d[key] ?? null; }
  setContent(key, value) {
    const d = this._read(this.contentFile);
    d[key] = value;
    this._write(this.contentFile, d);
  }
  setAllContent(data) { this._write(this.contentFile, data); }

  // ── Users ──────────────────────────────────────────────────────────────
  getUserByUsername(username) { return this._read(this.usersFile).find(u => u.username === username) || null; }
  getUserById(id)             { return this._read(this.usersFile).find(u => u.id === id) || null; }
  updateUserPassword(id, hash) {
    const users = this._read(this.usersFile);
    const u = users.find(u => u.id === id);
    if (u) { u.password = hash; this._write(this.usersFile, users); }
  }

  // ── Portfolio ──────────────────────────────────────────────────────────
  getAllPortfolio()   { return this._read(this.portfolioFile); }
  getPortfolioById(id) { return this._read(this.portfolioFile).find(i => i.id === id) || null; }
  createPortfolio(data) {
    const items = this._read(this.portfolioFile);
    const maxId = items.reduce((m, i) => Math.max(m, i.id || 0), 0);
    const maxOrder = items.reduce((m, i) => Math.max(m, i.sort_order || 0), 0);
    const item = { id: maxId+1, sort_order: maxOrder+1, visible: 1, created_at: new Date().toISOString(), updated_at: new Date().toISOString(), ...data };
    items.push(item);
    this._write(this.portfolioFile, items);
    return item;
  }
  updatePortfolio(id, data) {
    const items = this._read(this.portfolioFile);
    const idx = items.findIndex(i => i.id === id);
    if (idx === -1) return null;
    items[idx] = { ...items[idx], ...data, updated_at: new Date().toISOString() };
    this._write(this.portfolioFile, items);
    return items[idx];
  }
  deletePortfolio(id) {
    const items = this._read(this.portfolioFile).filter(i => i.id !== id);
    this._write(this.portfolioFile, items);
  }
  reorderPortfolio(ids) {
    const items = this._read(this.portfolioFile);
    ids.forEach((id, idx) => { const item = items.find(i => i.id === id); if (item) item.sort_order = idx; });
    this._write(this.portfolioFile, items);
  }

  // ── Testimonials ───────────────────────────────────────────────────────
  getAllTestimonials()  { return this._read(this.testimonialsFile); }
  getTestimonialById(id) { return this._read(this.testimonialsFile).find(i => i.id === id) || null; }
  createTestimonial(data) {
    const items = this._read(this.testimonialsFile);
    const maxId = items.reduce((m, i) => Math.max(m, i.id || 0), 0);
    const maxOrder = items.reduce((m, i) => Math.max(m, i.sort_order || 0), 0);
    const item = { id: maxId+1, sort_order: maxOrder+1, visible: 1, ...data };
    items.push(item);
    this._write(this.testimonialsFile, items);
    return item;
  }
  updateTestimonial(id, data) {
    const items = this._read(this.testimonialsFile);
    const idx = items.findIndex(i => i.id === id);
    if (idx === -1) return null;
    items[idx] = { ...items[idx], ...data };
    this._write(this.testimonialsFile, items);
    return items[idx];
  }
  deleteTestimonial(id) {
    const items = this._read(this.testimonialsFile).filter(i => i.id !== id);
    this._write(this.testimonialsFile, items);
  }

  // ── Media ──────────────────────────────────────────────────────────────
  getAllMedia(type, limit=30, offset=0) {
    let items = this._read(this.mediaFile).reverse();
    if (type === 'image') items = items.filter(m => m.mime_type?.startsWith('image/'));
    if (type === 'video') items = items.filter(m => m.mime_type?.startsWith('video/'));
    return { items: items.slice(offset, offset+limit), total: items.length };
  }
  addMedia(data) {
    const items = this._read(this.mediaFile);
    const maxId = items.reduce((m, i) => Math.max(m, i.id || 0), 0);
    const item  = { id: maxId+1, created_at: new Date().toISOString(), ...data };
    items.push(item);
    this._write(this.mediaFile, items);
    return item;
  }
  deleteMedia(id) {
    const items = this._read(this.mediaFile);
    const item  = items.find(i => i.id === id);
    const rest  = items.filter(i => i.id !== id);
    this._write(this.mediaFile, rest);
    return item;
  }

  // ── Messages ────────────────────────────────────────────────────────────
  getAllMessages() {
    return this._read(this.messagesFile).reverse();
  }
  addMessage(data) {
    const items = this._read(this.messagesFile);
    const maxId = items.reduce((m, i) => Math.max(m, i.id || 0), 0);
    const item  = { id: maxId+1, read: false, created_at: new Date().toISOString(), ...data };
    items.push(item);
    this._write(this.messagesFile, items);
    return item;
  }
  markMessageRead(id) {
    const items = this._read(this.messagesFile);
    const item  = items.find(i => i.id === id);
    if (item) { item.read = true; this._write(this.messagesFile, items); }
    return item;
  }
  deleteMessage(id) {
    const items = this._read(this.messagesFile).filter(i => i.id !== id);
    this._write(this.messagesFile, items);
  }
  getUnreadCount() {
    return this._read(this.messagesFile).filter(m => !m.read).length;
  }
}

module.exports = function(dataDir) {
  return new JsonDB(dataDir);
};

