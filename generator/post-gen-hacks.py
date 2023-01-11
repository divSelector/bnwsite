from pathlib import Path

def get_html(in_file: str):
    raw_html = Path(in_file)
    with raw_html.open() as fo:
        return fo.read()

def output_html(clean_html, out_file):
    with out_file.open('w') as fo:
        fo.write(clean_html)
        print(f"Wrote to {out_file}")


head = get_html("head.txt")
tail = get_html("tail.txt")
raw = get_html("mainTable-raw.html")

#Elements: Fire Ice Bolt Water Earth Wind Dark Holy
# Blind, Zombie, Poison, Imp, Petrify, Death, Mute, Berserk, Muddle, Sap, Sleep, Slow, Stop

string_replace_hacks = [
    ('<tr>', '<tr tabindex="0">'),
    ('[object Object],', ''),
    ('[object Object]', ''),
    ('Spd', 'Speed'),
    ('Vgr', 'Vigor'),
    ('Mag', 'Magic'),
    ('Stam', 'Stamina'),
    ('(All but Sleep)', '(Blind Zombie Poison Imp Petrify Death Mute Berserk Muddle Sap Slow Stop)'),
    ('(All but Death)', '(Blind Zombie Poison Imp Petrify Mute Berserk Muddle Sap Sleep Slow Stop)'),
    ('(All but Dark/Holy)', '(Fire Ice Bolt Water Earth Wind)'),
    ('(All but Blind)', '(Zombie Poison Imp Petrify Death Mute Berserk Muddle Sap Sleep Slow Stop)'),
    ('(All but Death/Stop)', '(Blind Zombie Poison Imp Petrify Mute Berserk Muddle Sap Sleep Slow)'),
    ('<th scope="col">Dance</th>', '<th scope="col">DANCE</th>'),
    ('<th scope="col">DANCE_MODES</th>', '<th scope="col">DANCE</th>'),
    ('<th scope="col">Rage</th>', '<th scope="col">RAGE</th>'),
    ('<th scope="col">Slots</th>', '<th scope="col">SLOTS</th>'),
    ('<th scope="col">Enemy</th>', '<th scope="col">ENEMY</th>'),
    ('<th scope="col">Weapon</th>', '<th scope="col">WEAPON</th>'),
    ('<th scope="col">Legend</th>', '<th scope="col">LEGEND</th>'),
    ('<th scope="col">Armor</th>', '<th scope="col">ARMOR</th>'),
    ('<th scope="col">Item</th>', '<th scope="col">ITEM</th>'),
    ('<th scope="col">Shield</th>', '<th scope="col">SHIELD</th>'),
    ('<th scope="col">Helmet</th>', '<th scope="col">HELMET</th>'),
    ('<th scope="col">Relic</th>', '<th scope="col">RELIC</th>'),
    ('<th scope="col">TOWNS</th>', '<th scope="col">SHOPS</th>'),
    ('<th scope="col">ESPER BOONS</th>', '<th scope="col">ESPER EQUIP BONUS</th>')
]

cleaned = raw
for hack in string_replace_hacks:
    old, new = hack
    cleaned = cleaned.replace(old, new)

html = head + cleaned + tail
output_html(html, Path('../static/static.html'))
