with open('c:/CreativeStudio/portfolio.html','r',encoding='utf-8') as f:
    c = f.read()

# Replace all index.html links with ?noload=1
replacements = [
    ('href="index.html"', 'href="index.html?noload=1"'),
    ('href="index.html#about"', 'href="index.html?noload=1#about"'),
    ('href="index.html#services"', 'href="index.html?noload=1#services"'),
    ('href="index.html#contact"', 'href="index.html?noload=1#contact"'),
]

for old, new in replacements:
    c = c.replace(old, new)

with open('c:/CreativeStudio/portfolio.html','w',encoding='utf-8') as f:
    f.write(c)
print('Done! noload param added to all home links.')
