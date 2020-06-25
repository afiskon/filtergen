#!/usr/bin/env python3

import argparse
from math import pow, log10

parser = argparse.ArgumentParser(
    description='Atteenuator calculator'
    )
parser.add_argument(
    '-i', '--impedance', type=float, default = 50, metavar='IMP',
    help='Impedance (default 50 Ohm)')
parser.add_argument(
    '-a', '--attenuation', type=float, required=True, metavar='ATT',
    help='Target attenuation in dB')
args = parser.parse_args()

Z0 = args.impedance
N = pow(10, args.attenuation/20)
R1 = R2 = Z0*(N+1)/(N-1)
R3 = Z0*(pow(N,2)-1)/(2*N)
R4 = R5 = Z0*(N-1)/(N+1)
R6 = Z0*(2*N)/(pow(N,2)-1)

print("""
PI-network:             T-network:
>---+--- R3 ---+---<    >--- R4 ---+--- R5 ---<
    |          |                   |
    R1         R2                  R6
    |          |                   |
    V          V                   V

""")

print("R1 = R2 = {:.2f} Ohm".format(R1))
print("R3 = {:.2f} Ohm".format(R3))
print(" ")
print("R4 = R5 = {:.2f} Ohm".format(R4))
print("R6 = {:.2f} Ohm".format(R6))
