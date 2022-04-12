#!/usr/bin/env python3
# vim: set ai et ts=4 sw=4:

# based on https://coil32.ru/calc/ferrite-permeability.html

import argparse
from math import log

parser = argparse.ArgumentParser(
    description='Ferrite core permeability calculator'
    )
parser.add_argument(
    '-t', metavar='T', type=float, required=True,
    help='Core thickness, mm')
parser.add_argument(
    '-di', metavar='Di', type=float, required=True,
    help='Core internal diameter, mm')
parser.add_argument(
    '-de', metavar='De', type=float, required=True,
    help='Core external diameter, mm')
parser.add_argument(
    '-n', metavar='N', type=float, required=True,
    help="Number of turns (10-15 should be fine)")
parser.add_argument(
    '-l', metavar='L', type=float, required=True,
    help='Meadured inducatence, uH')
args = parser.parse_args()

T = args.t
Di = args.di
De = args.de
N = args.n
L = args.l

if De/Di >= 1.75:
    u = L / (0.0002*T*N*N*log(De/Di))
else:
    u = (L * (De + Di)) / (0.0004*T*N*N*(De-Di))

Al = 1000*L/(N*N)

print("Initial magnetic permeability: {}".format(u))
print("Inductance factor of the core (Al): {}".format(Al))
