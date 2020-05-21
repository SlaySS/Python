from collections import namedtuple

Cat = namedtuple('Cat', "name weight color")

cats = [Cat('Barsik', 10, 'black'), Cat('Murzik', 5, 'white'), Cat('Pushok', 15, 'orange')]

print(cats[0].color)