const express = require('express');
const { requireAuth } = require('./auth');

module.exports = function(db) {
  const router = express.Router();

  // ── Public: Submit message from contact form ───────────────────────────
  router.post('/', (req, res) => {
    const { name, email, service, budget, budget_custom, message } = req.body;
    if (!name || !email || !message) {
      return res.status(400).json({ error: 'Name, email and message are required' });
    }
    const item = db.addMessage({
      name: name.trim(),
      email: email.trim(),
      service: service || '',
      budget: budget === 'custom' ? (budget_custom || 'Custom') : (budget || ''),
      message: message.trim(),
      ip: req.ip
    });
    res.json({ success: true, id: item.id });
  });

  // ── Admin: Get all messages ────────────────────────────────────────────
  router.get('/', requireAuth, (req, res) => {
    const messages = db.getAllMessages();
    res.json({ messages, unread: db.getUnreadCount() });
  });

  // ── Admin: Get unread count only ───────────────────────────────────────
  router.get('/unread-count', requireAuth, (req, res) => {
    res.json({ count: db.getUnreadCount() });
  });

  // ── Admin: Mark as read ────────────────────────────────────────────────
  router.patch('/:id/read', requireAuth, (req, res) => {
    const item = db.markMessageRead(parseInt(req.params.id));
    if (!item) return res.status(404).json({ error: 'Not found' });
    res.json({ success: true });
  });

  // ── Admin: Delete message ──────────────────────────────────────────────
  router.delete('/:id', requireAuth, (req, res) => {
    db.deleteMessage(parseInt(req.params.id));
    res.json({ success: true });
  });

  return router;
};
