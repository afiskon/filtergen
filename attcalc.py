#!/usr/bin/env python3

import argparse
from math import pow, log10

# standard 1% resistors values (Ohm)
std_values = [
    1, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2, 2.2, 2.4, 2.7, 3, 3.3, 3.6, 3.9, 4.3, 4.7,
    5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1,
    10,11,12,13,15,16,18,20,22,24,27,30,33,36,39,43,47,51,56,62,68,75,82,91,
    100,110,120,130,150,160,180,200,220,240,270,300,330,360,390,430,470,
    510,560,620,680,750,820,910,
    1000,1100,1200,1300,1500,1600,1800,2000,2200,2400,2700,3000,3300,3600,3900,
    4300,4700,4750,5100,5600,6200,6800,7500,8200,9100,
    10000,11000,12000,13000,15000,16000,18000,20000,22000,24000,27000,
    30000,33000,36000,39000,43000,47000,51000,56000,62000,68000,75000,
    82000,91000,
    100000,110000,120000,130000,150000,160000,180000,200000,220000,240000,270000,
    300000,330000,360000,390000,430000,470000,510000,560000,620000,680000,750000,
    820000,910000,
    1_000_000,1_100_000,1_200_000,1_500_000,1_600_000,1_800_000,2_000_000,
    2_200_000,2_400_000,2_700_000,3_000_000,3_300_000,5_100_000,
]


def closest(val):
    diffs = [ (str(x)+" Ohm", abs(x-val)) for x in std_values ]
    sorted_vals = sorted(diffs, key = lambda a: a[1])
    return sorted_vals[0][0]

parallel_values = [ 
    ("{}||{}={:.2f} Ohm".format(r1, r2, p), p) 
        for r1 in std_values
        for r2 in std_values
        for p in [ r1*r2/(r1+r2) ]
]

def closest_parallel(val):
    diffs = [ (desc, abs(p-val)) for (desc, p) in parallel_values ]
    sorted_vals = sorted(diffs, key = lambda a: a[1])
    return sorted_vals[0][0]

parser = argparse.ArgumentParser(
    description='Attenuator calculator'
    )
parser.add_argument(
    '-i', '--impedance', type=float, default = 50, metavar='I',
    help='impedance (default 50 Ohm)')
parser.add_argument(
    '-p', '--parallel', action="store_true",
    help='suggest closest resistor values connected in parallel')
parser.add_argument(
    '-a', '--att', type=float, required=True, metavar='A',
    help='target attenuation in dB')
args = parser.parse_args()

Z0 = args.impedance
N = pow(10, args.att/20)
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

if args.parallel:
    print("R1 = R2 = {:.2f} Ohm, closest: {} & {}".format(R1, closest(R1), closest_parallel(R1)))
    print("R3 = {:.2f} Ohm, closest: {} & {}".format(R3, closest(R3), closest_parallel(R3)))
    print(" ")
    print("R4 = R5 = {:.2f} Ohm, closest: {} & {}".format(R4, closest(R4), closest_parallel(R4)))
    print("R6 = {:.2f} Ohm, closest: {} & {}".format(R6, closest(R6), closest_parallel(R6)))
else:
    print("R1 = R2 = {:.2f} Ohm, closest: {}".format(R1, closest(R1)))
    print("R3 = {:.2f} Ohm, closest: {}".format(R3, closest(R3)))
    print(" ")
    print("R4 = R5 = {:.2f} Ohm, closest: {}".format(R4, closest(R4)))
    print("R6 = {:.2f} Ohm, closest: {}".format(R6, closest(R6)))
