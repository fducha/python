from xml.etree import ElementTree

root = ElementTree.fromstring(input())
values = {'red': 0, 'green': 0, 'blue': 0}
level = 0


def do_level(level_root, lev):
    lev += 1
    color = level_root.attrib['color']
    if color == 'blue':
        values['blue'] += lev
    elif color == 'red':
        values['red'] += lev
    else:
        values['green'] += lev
    for child in level_root:
        do_level(child, lev)


do_level(root, 0)
print(values['red'], values['green'], values['blue'])
