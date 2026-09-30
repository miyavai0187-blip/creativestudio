const express = require('express');
const bcrypt  = require('bcryptjs');
const jwt     = require('jsonwebtoken');

const SECRET = process.env.JWT_SECRET || 'creativestudio-secret-2026';

module.exports = function(db) {
  const router = express.Router();

  router.post('/login', (req, res) => {
    const { username, password } = req.body;
    if (!username || !password) return res.status(400).json({ error: 'Missing credentials' });
    const user = db.getUserByUsername(username);
    if (!user || !bcrypt.compareSync(password, user.password)) {
      return res.status(401).json({ error: 'Invalid username or password' });
    }
    const token = jwt.sign({ id: user.id, username: user.username }, SECRET, { expiresIn: '7d' });
    res.cookie('admin_token', token, {
      httpOnly: true,
      secure: process.env.NODE_ENV === 'production',
      sameSite: 'lax',
      maxAge: 7 * 24 * 60 * 60 * 1000
    }).json({ success: true, username: user.username });
  });

  router.post('/logout', (req, res) => {
    res.clearCookie('admin_token').json({ success: true });
  });

  router.get('/verify', (req, res) => {
    const token = req.cookies.admin_token || (req.headers.authorization||'').replace('Bearer ','');
    if (!token) return res.status(401).json({ error: 'Not authenticated' });
    try {
      const payload = jwt.verify(token, SECRET);
      res.json({ success: true, username: payload.username });
    } catch { res.status(401).json({ error: 'Token expired' }); }
  });

  router.post('/change-password', requireAuth, (req, res) => {
    const { currentPassword, newPassword } = req.body;
    const user = db.getUserById(req.user.id);
    if (!bcrypt.compareSync(currentPassword, user.password)) {
      return res.status(400).json({ error: 'Current password incorrect' });
    }
    db.updateUserPassword(req.user.id, bcrypt.hashSync(newPassword, 10));
    res.json({ success: true });
  });

  return router;
};

function requireAuth(req, res, next) {
  const token = req.cookies?.admin_token || (req.headers.authorization||'').replace('Bearer ','');
  if (!token) return res.status(401).json({ error: 'Not authenticated' });
  try {
    const SECRET = process.env.JWT_SECRET || 'creativestudio-secret-2026';
    req.user = jwt.verify(token, SECRET);
    next();
  } catch { res.status(401).json({ error: 'Token expired' }); }
}

module.exports.requireAuth = requireAuth;
