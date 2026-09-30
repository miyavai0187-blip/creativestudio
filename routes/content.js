const express = require('express');
const { requireAuth } = require('./auth');

module.exports = function(db) {
  const router = express.Router();

  // ── GET all site content (public - for frontend) ───────────────────────
  router.get('/', (req, res) => {
    const data = db.getSiteData();
    res.json(data);
  });

  // ── GET single section ─────────────────────────────────────────────────
  router.get('/:key', (req, res) => {
    const data = db.getContent(req.params.key);
    if (!data) return res.status(404).json({ error: 'Section not found' });
    res.json(data);
  });

  // ── UPDATE single section (admin only) ────────────────────────────────
  router.put('/:key', requireAuth, (req, res) => {
    const { key } = req.params;
    const value = req.body;
    if (!value) return res.status(400).json({ error: 'No data provided' });
    db.setContent(key, value);
    res.json({ success: true, key, data: value });
  });

  // ── PATCH: merge update a section ─────────────────────────────────────
  router.patch('/:key', requireAuth, (req, res) => {
    const { key } = req.params;
    const existing = db.getContent(key) || {};
    const merged = { ...existing, ...req.body };
    db.setContent(key, merged);
    res.json({ success: true, key, data: merged });
  });

  // ── Publish: save all sections at once ────────────────────────────────
  router.post('/publish', requireAuth, (req, res) => {
    const sections = req.body; // { hero: {...}, about: {...}, ... }
    Object.entries(sections).forEach(([key, val]) => {
      db.setContent(key, val);
    });
    res.json({ success: true, message: 'Published successfully!' });
  });

  return router;
};
