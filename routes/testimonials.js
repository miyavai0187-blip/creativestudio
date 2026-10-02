const express = require('express');
const multer  = require('multer');
const path    = require('path');
const { requireAuth } = require('./auth');

module.exports = function(db, UPLOADS_DIR) {
  const router = express.Router();

  const storage = multer.diskStorage({
    destination: (req, file, cb) => cb(null, UPLOADS_DIR),
    filename:    (req, file, cb) => cb(null, `testi_${Date.now()}${path.extname(file.originalname)}`)
  });
  const upload = multer({ storage, limits: { fileSize: 10 * 1024 * 1024 } });

  // GET all
  router.get('/', (req, res) => {
    const items = db.getAllTestimonials().filter(i => i.visible !== 0);
    res.json(items);
  });

  // GET all (admin - includes hidden)
  router.get('/all', requireAuth, (req, res) => {
    res.json(db.getAllTestimonials());
  });

  // POST create
  router.post('/', requireAuth, upload.single('photo'), (req, res) => {
    const { name, role, review } = req.body;
    const photo = req.file ? `/uploads/${req.file.filename}` : (req.body.photo || '');
    const item = db.createTestimonial({ name, role, review, photo });
    res.json({ success: true, item });
  });

  // PUT update
  router.put('/:id', requireAuth, upload.single('photo'), (req, res) => {
    const id = parseInt(req.params.id);
    const existing = db.getTestimonialById(id);
    if (!existing) return res.status(404).json({ error: 'Not found' });
    const { name, role, review, visible } = req.body;
    const photo = req.file ? `/uploads/${req.file.filename}` : (req.body.photo || existing.photo);
    const item = db.updateTestimonial(id, {
      name, role, review, photo,
      visible: visible !== undefined ? (visible == '1' || visible === true ? 1 : 0) : existing.visible
    });
    res.json({ success: true, item });
  });

  // DELETE
  router.delete('/:id', requireAuth, (req, res) => {
    db.deleteTestimonial(parseInt(req.params.id));
    res.json({ success: true });
  });

  return router;
};
