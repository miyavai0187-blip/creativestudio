
with open('c:/CreativeStudio/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace navbar logo (text-based) with actual logo image
html = html.replace(
    '<a href="#" class="logo logo-img" id="logo-link">\n        <img src="logo.jpg" alt="CreativeStudio" class="nav-logo-img" />\n      </a>',
    '<a href="#" class="logo logo-img" id="logo-link"><img src="logo.jpg" alt="CreativeStudio" class="nav-logo-img" /></a>'
)

# If not already replaced, do the text-logo replacement
if 'logo-icon' in html:
    # Navbar logo
    import re
    html = re.sub(
        r'<a href="#" class="logo" id="logo-link">.*?</a>',
        '<a href="#" class="logo logo-img" id="logo-link"><img src="logo.jpg" alt="CreativeStudio" class="nav-logo-img" /></a>',
        html, flags=re.DOTALL, count=1
    )
    # Footer logo
    html = re.sub(
        r'<a href="#" class="logo"><span class="logo-icon">.*?</a>',
        '<a href="#" class="logo logo-img"><img src="logo.jpg" alt="CreativeStudio" class="footer-logo-img" /></a>',
        html, flags=re.DOTALL, count=1
    )

with open('c:/CreativeStudio/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Logo replaced in HTML')
