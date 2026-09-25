with open('c:/CreativeStudio/portfolio.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix 1: Remove 'scrolled' from initial navbar class
c = c.replace('class="navbar scrolled"', 'class="navbar"')

# Fix 2: Add Get Started button if missing
if 'nav-cta' not in c:
    c = c.replace(
        '</nav>\n      <button class="hamburger"',
        '</nav>\n      <a href="index.html#contact" class="nav-cta">Get Started</a>\n      <button class="hamburger"'
    )

# Fix 3: Override active style to match main site pill style
old_style = '.nav-links a.active { color:var(--primary) !important; }'
new_style = '''.nav-links a.active {
      background: rgba(255,255,255,0.1) !important;
      color: #fff !important;
      padding: 6px 16px;
      border-radius: 50px;
      border-bottom: none !important;
    }'''
if old_style in c:
    c = c.replace(old_style, new_style)
elif '.nav-links a.active' not in c:
    c = c.replace('</style>', '    .nav-links a.active { background:rgba(255,255,255,0.1)!important; color:#fff!important; padding:6px 16px; border-radius:50px; border-bottom:none!important; }\n  </style>')

with open('c:/CreativeStudio/portfolio.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('nav-cta present:', 'nav-cta' in c)
print('scrolled removed:', 'navbar scrolled' not in c)
print('Done!')
