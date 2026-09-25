import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find ticker section
ticker_start = content.find('class="ticker-wrap"')
if ticker_start == -1:
    print("ERROR: ticker-wrap not found")
    exit()

# Check if ticker-band already exists
if 'ticker-band' in content:
    print("ticker-band already exists — skipping")
    exit()

# Wrap: replace <div class="ticker-wrap"> with <div class="ticker-wrap"><div class="ticker-band">
content = content.replace('class="ticker-wrap">', 'class="ticker-wrap"><div class="ticker-band">', 1)

# Now find the closing </div> of ticker-wrap and insert </div> before it
# Find the ticker-track closing tag, then find next </div>
track_end = content.find('</div>', content.find('ticker-track'))
# Find next </div> after ticker-track closes (that's ticker-wrap close)
wrap_end = content.find('</div>', track_end + 6)

# Insert </div> (for ticker-band) before the ticker-wrap closing </div>
content = content[:wrap_end] + '</div>' + content[wrap_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: ticker-band wrapper added!")
