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
      const ext  = path.extname(file.originalname);
      const name = Date.now() + '-' + Math.round(Math.random() * 1e6) + ext;
      cb(null, name);
    }
  });
  const upload = multer({
    storage,
    limits: { fileSize: 100 * 1024 * 1024 },
    fileFilter: (req, file, cb) => {
      const allowed = /jpeg|jpg|png|gif|webp|svg|mp4|webm|mov/;
      const ok = allowed.test(path.extname(file.originalname).toLowerCase());
      ok ? cb(null, true) : cb(new Error('File type not allowed'));
    }
  });

  // ── Upload single ──────────────────────────────────────────────────────
  router.post('/upload', requireAuth, upload.single('file'), (req, res) => {
    if (!req.file) return res.status(400).json({ error: 'No file uploaded' });
    const url   = `/uploads/${req.file.filename}`;
    const media = db.addMedia({ filename: req.file.filename, original_name: req.file.originalname, mime_type: req.file.mimetype, size: req.file.size, url });
    res.json({ success: true, ...media });
  });

  // ── Upload multiple ────────────────────────────────────────────────────
  router.post('/upload-multiple', requireAuth, upload.array('files', 20), (req, res) => {
    if (!req.files?.length) return res.status(400).json({ error: 'No files' });
    const results = req.files.map(file => {
      const url = `/uploads/${file.filename}`;
      return db.addMedia({ filename: file.filename, original_name: file.originalname, mime_type: file.mimetype, size: file.size, url });
    });
    res.json({ success: true, files: results });
  });

  // ── Get all media ──────────────────────────────────────────────────────
  router.get('/', requireAuth, (req, res) => {
    const page  = parseInt(req.query.page)  || 1;
    const limit = parseInt(req.query.limit) || 30;
    const type  = req.query.type;
    const offset = (page - 1) * limit;
    res.json(db.getAllMedia(type, limit, offset));
  });

  // ── Delete media ───────────────────────────────────────────────────────
  router.delete('/:id', requireAuth, (req, res) => {
    const id    = parseInt(req.params.id);
    const media = db.deleteMedia(id);
    if (!media) return res.status(404).json({ error: 'Not found' });
    const fp = path.join(uploadsDir, media.filename);
    if (fs.existsSync(fp)) fs.unlinkSync(fp);
    res.json({ success: true });
  });

  return router;
};
