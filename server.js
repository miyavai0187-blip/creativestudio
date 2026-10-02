require('dotenv').config();
const express    = require('express');
const path       = require('path');
const cookieParser = require('cookie-parser');
const cors       = require('cors');
const fs         = require('fs');

const app  = express();
const PORT = process.env.PORT || 3000;

// ── Ensure data dir exists (Railway persistent volume mount) ──────────────
const DATA_DIR    = process.env.DATA_DIR || path.join(__dirname, 'data');
const UPLOADS_DIR = path.join(DATA_DIR, 'uploads');
[DATA_DIR, UPLOADS_DIR].forEach(d => { if (!fs.existsSync(d)) fs.mkdirSync(d, { recursive: true }); });

// ── DB & routes ────────────────────────────────────────────────────────────
const db           = require('./database')(DATA_DIR);
const authRouter          = require('./routes/auth')(db);
const contentRouter       = require('./routes/content')(db);
const mediaRouter         = require('./routes/media')(db, UPLOADS_DIR);
const portfolioRouter     = require('./routes/portfolio')(db, UPLOADS_DIR);
const messagesRouter      = require('./routes/messages')(db);
const testimonialsRouter  = require('./routes/testimonials')(db, UPLOADS_DIR);

// ── Middleware ─────────────────────────────────────────────────────────────
app.use(cors({ origin: true, credentials: true }));
app.use(express.json({ limit: '50mb' }));
app.use(express.urlencoded({ extended: true, limit: '50mb' }));
app.use(cookieParser());

// ── Static: uploads & site files ──────────────────────────────────────────
app.use('/uploads', express.static(UPLOADS_DIR));
app.use(express.static(__dirname));          // serves index.html, style.css etc.

// ── API routes ─────────────────────────────────────────────────────────────
app.use('/api/auth',          authRouter);
app.use('/api/content',       contentRouter);
app.use('/api/media',         mediaRouter);
app.use('/api/portfolio',     portfolioRouter);
app.use('/api/messages',      messagesRouter);
app.use('/api/testimonials',  testimonialsRouter);

// ── Admin panel (SPA) ─────────────────────────────────────────────────────
app.get('/admin', (req, res) => res.sendFile(path.join(__dirname, 'admin', 'index.html')));
app.get('/admin/*', (req, res) => res.sendFile(path.join(__dirname, 'admin', 'index.html')));

// ── Content API: serve dynamic site data for frontend ────────────────────
app.get('/site-data.json', (req, res) => {
  try {
    const data = db.getSiteData();
    res.json(data);
  } catch(e) {
    res.status(500).json({ error: e.message });
  }
});

app.listen(PORT, () => console.log(`✅ CreativeStudio CMS running on port ${PORT}`));
