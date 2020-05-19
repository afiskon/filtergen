#!/usr/bin/env python3
# vim: set ai et ts=4 sw=4: 

# Diplexer Generator v 0.1
# (c) Aleksander Alekseev 2020
# https://eax.me/

# The algorithm is based on Chapter 11 of The ARRL Handbook 2020

from math import pi
import sys
import argparse

def scale(x):
    unit = ""
    if x < 1:
        x *= 1000
        unit = "m"
        if x < 1:
            x *= 1000
            unit = "u"
            if x < 1:
                x *= 1000
                unit = "n"
                if x < 1:
                    x *= 1000
                    unit = "p"
    return (x, unit)

def diplexer_schematic():
    return """
Diplexer schematic:


      +--- L1 ---+--- L2 ---+--- L3 ---+
      |          |          |          |
      |          C1         C2        Rlp
      |          |          |          |
Src --+          V          V          V
      |
      |
      +--- C3 ---+--- C4 ---+--- C5 ---+
                 |          |          |
                 L4         L5        Rhp
                 |          |          |
                 V          V          V

"""

parser = argparse.ArgumentParser(
    description = 'Generate a diplexer',
    formatter_class = argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-f', '--frequency', metavar='F', type=float, default=0,
                    help='Cutoff frequency, Hz')
parser.add_argument('-i', '--impedance', metavar='R', type=float, default=50,
                    help='Source and load impedance in Ohm')
args = parser.parse_args()

if args.frequency == 0:
    parser.print_help()
    sys.exit(1)

F = args.frequency
R = args.impedance
K = 1.005

data = [
# Low pass inductance:
("L1", 1.5613*K*R/(2*pi*F), "H"),
("L2", 1.7659*K*R/(2*pi*F), "H"),
("L3", 0.6507*K*R/(2*pi*F), "H"),

# Low pass capacitance
("C1", 1.8069*K/(2*pi*R*F), "F"),
("C2", 1.4173*K/(2*pi*R*F), "F"),

# High pass inductance:
("L4", 0.5534*R/(2*pi*F*K), "H"),
("L5", 0.7056*R/(2*pi*F*K), "H"),

# High pass capacitance
("C3", 0.6405/(2*pi*F*R*K), "F"),
("C4", 0.5563/(2*pi*F*R*K), "F"),
("C5", 1.5368/(2*pi*F*R*K), "F")
]

print(diplexer_schematic())

for (name, value, unit) in data:
    (x, s) = scale(value)
    print("{} = {:.2f} {}{}".format(name, x, s, unit))
