import sys

import oisin

filename = "input/wine.txt"
try:
    filename = sys.argv[1]
except IndexError:
    pass

oisin.balladize(
    oisin.load(filename),
    meter=oisin.iambic(6, 'aabbcc'),
    step=13,
    order=3)
