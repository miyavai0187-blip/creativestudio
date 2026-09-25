with open('style.css', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Primary brand color — old #6AB04C → new #79b32b
    ('#6AB04C', '#79b32b'),
    ('#6ab04c', '#79b32b'),
    ('106,176,76', '121,179,43'),   # rgba values for old primary
    ('#5a9a3c', '#629025'),         # primary-dark
    ('#52943a', '#629025'),         # darker green in ticker
    ('#80cb5e', '#90c94a'),         # lighter green top in ticker
    ('#559c3a', '#629025'),         # medium green in ticker
    ('#3dd68c', '#a5d44e'),         # gradient end color
    ('#3d7029', '#4a7a1a'),         # ribbon thickness dark
    ('#2a4f1a', '#345710'),         # ribbon thickness darker
    ('#7bc55a', '#8cca3a'),         # ribbon top light

    # Background colors — old darks → new #000205 variants
    ('#050510', '#000205'),
    ('#07070f', '#000205'),
    ('#0d0d1f', '#060d02'),         # bg-card: very dark green-tinted
    ('#111128', '#0a110a'),         # bg-card2
]

for old, new in replacements:
    content = content.replace(old, new)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Colors updated!")
print(f"  Background: #000205")
print(f"  Brand:      #79b32b")
