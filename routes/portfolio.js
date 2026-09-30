const express = require('express');
const multer  = require('multer');
const path    = require('path');
const fs      = require('fs');
const { requireAuth } = require('./auth');

module.exports = function(db, uploadsDir) {
  const router = express.Router();

  const storage = multer.diskStorage({
    destination: (req, file, cb) => cb(null, uploadsDir),
    filename:    (req, file, cb) => {
      const ext = path.extname(file.originalname);
      cb(null, 'pf-' + Date.now() + ext);
    }
  });
  const upload = multer({ storage, limits: { fileSize: 200 * 1024 * 1024 } });

  // ── Get all ────────────────────────────────────────────────────────────
  router.get('/', (req, res) => {
    const items = db.getAllPortfolio().sort((a,b) => (a.sort_order||0) - (b.sort_order||0));
    res.json(items);
  });

  // ── Create ─────────────────────────────────────────────────────────────
  router.post('/', requireAuth, upload.fields([{name:'thumbnail',maxCount:1},{name:'media',maxCount:1}]), (req, res) => {
    const { title, category, description, media_type, youtube_url } = req.body;
    const thumbnail = req.files?.thumbnail?.[0] ? `/uploads/${req.files.thumbnail[0].filename}` : null;
    const media_url = youtube_url || (req.files?.media?.[0] ? `/uploads/${req.files.media[0].filename}` : null);
    const item = db.createPortfolio({ title, category, description, thumbnail, media_url, media_type: media_type||'image' });
    res.json({ success: true, item });
  });

  // ── Update ─────────────────────────────────────────────────────────────
  router.put('/:id', requireAuth, upload.fields([{name:'thumbnail',maxCount:1},{name:'media',maxCount:1}]), (req, res) => {
    const id       = parseInt(req.params.id);
    const existing = db.getPortfolioById(id);
    if (!existing) return res.status(404).json({ error: 'Not found' });

    const { title, category, description, media_type, youtube_url, visible, sort_order } = req.body;
    const thumbnail = req.files?.thumbnail?.[0] ? `/uploads/${req.files.thumbnail[0].filename}` : existing.thumbnail;
    const media_url = youtube_url || (req.files?.media?.[0] ? `/uploads/${req.files.media[0].filename}` : existing.media_url);

    const item = db.updatePortfolio(id, {
      title, category, description, thumbnail, media_url,
      media_type: media_type || existing.media_type,
      visible: visible !== undefined ? (visible == '1' || visible === true ? 1 : 0) : existing.visible,
      sort_order: sort_order !== undefined ? parseInt(sort_order) : existing.sort_order
    });
    res.json({ success: true, item });
  });

  // ── Toggle visibility ──────────────────────────────────────────────────
  router.patch('/:id/toggle', requireAuth, (req, res) => {
    const id   = parseInt(req.params.id);
    const item = db.getPortfolioById(id);
    if (!item) return res.status(404).json({ error: 'Not found' });
    db.updatePortfolio(id, { visible: item.visible ? 0 : 1 });
    res.json({ success: true, visible: !item.visible });
  });

  // ── Reorder ────────────────────────────────────────────────────────────
  router.post('/reorder', requireAuth, (req, res) => {
    db.reorderPortfolio(req.body.ids.map(Number));
    res.json({ success: true });
  });

  // ── Delete ─────────────────────────────────────────────────────────────
  router.delete('/:id', requireAuth, (req, res) => {
    const id   = parseInt(req.params.id);
    const item = db.getPortfolioById(id);
    if (!item) return res.status(404).json({ error: 'Not found' });
    [item.thumbnail, item.media_url].forEach(url => {
      if (url?.startsWith('/uploads/')) {
        const fp = path.join(uploadsDir, path.basename(url));
        if (fs.existsSync(fp)) fs.unlinkSync(fp);
      }
    });
    db.deletePortfolio(id);
    res.json({ success: true });
  });

  return router;
};
