with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find ticker closing tag position
ticker_end = content.find('</div></div>\n', content.find('ticker-wrap'))
ticker_end = content.find('\n', ticker_end) + 1  # move past the newline

# Find services section start and end
svc_start = content.find('<section class="section services" id="services">')
svc_end   = content.find('</section>', svc_start) + len('</section>') + 1

# Find about section start and end  
ab_start = content.find('<section class="section about" id="about">')
ab_end   = content.find('</section>', ab_start) + len('</section>') + 1

services_block = content[svc_start:svc_end]
about_block    = content[ab_start:ab_end]

# Build new content:
# everything before services_block + about_block + newline + services_block + everything after original about_block

# Remove services block first (it comes before about)
new_content = content[:svc_start] + content[svc_end:]

# Now find about in new_content and insert services after it
ab_start2 = new_content.find('<section class="section about" id="about">')
ab_end2   = new_content.find('</section>', ab_start2) + len('</section>') + 1

new_content = new_content[:ab_start2] + about_block + '\n' + services_block + new_content[ab_end2:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("DONE")
