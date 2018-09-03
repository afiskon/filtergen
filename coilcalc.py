#!/usr/bin/env python3
# vim: set ai et ts=4 sw=4:

# Coil Calculator v0.1
# coded by Aleksander Alekseev, 2018

# Based on algorithms used by Coil32 online calculator:
# http://coil32.ru/calc/one-layer.html

import sys
import math
import argparse

def rosa_ks(x):
	return 1.25 - math.log(2*x)

def rosa_km(n):
    n2=n*n
    n3=n2*n
    n5=n3*n2
    n7=n5*n2
    n9=n7*n2
    return math.log(2*math.pi)-1.5-math.log(n)/(6*n)-0.33084236/n-1/(120*n3)+1/(504*n5)-0.0011923/n7+0.0005068/n9

# Input:
#     I - target inductance [uH]
#     D - carcass diameter [mm]
#     d - wire diameter without insulation [mm]
#     p - wire diameter with insulation [mm]
# Outout:
#     (w, l), where
#     w - number of turns
#     l - winding length [mm]
# Example:
#     calc_turns_and_length(72 * 0.001, 7, 0.644, 1.4) = (2.806, 3.928)
def calc_turns_and_length(I, D, d, p):
    w = 0
    l = 0
    i = 0
    Dk = 0

    Ks = rosa_ks(p/d)
    Dk = D + p
    while(i <= I):
        w = w + 0.001
        l = w*p
        k = l/Dk
        i = 0.0002*math.pi*Dk*w*w*(math.log(1+math.pi/(2*k))+1/(2.3004+3.437*k+1.763*k*k-0.47/math.pow((0.755+1/k),1.44)))
        Km = rosa_km(w);
        Lcor = 0.0002*math.pi*Dk*w*(Ks+Km)
        i = i - Lcor
    return (w, l)

# Input:
#   w - number of turns
#   D - carcass diameter [mm]
#   l - winding length [mm]
# Output:
#   inductance [uH]
# Example:
#   calc_inductance(3, 7, 3.9) = 0.07
def calc_inductance(w, D, l):
    p = l/w
    Ks = rosa_ks(1.07)
    Dk = D + p
    k = l/Dk
    L = 0.0002*math.pi*Dk*w*w*(math.log(1+math.pi/(2*k))+1/(2.3004+3.437*k+1.763*k*k-0.47/math.pow((0.755+1/k),1.44)))
    Km = rosa_km(w)
    Lcor = 0.0002*math.pi*Dk*w*(Ks+Km)
    L = L - Lcor
    return L

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = 'Calculate number of turns and winding length for a given coil inductance, or do a reverse calculation',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--inductance', type=float, default=0,
                        help='Target inductance in uH')
    parser.add_argument('-c', '--carcass-diameter', type=float, default=0,
                        help='Carcass diameter in mm')
    parser.add_argument('-d1', '--diameter1', type=float, default=0,
                        help='Wire diameter without insulation in mm')
    parser.add_argument('-d2', '--diameter2', type=float, default=0,
                        help='Wire diameter with insulation in mm')
    parser.add_argument('-t', '--turns', type=float, default=0,
                        help='Number of turns (only for --reverse)')
    parser.add_argument('-l', '--length', type=float, default=0,
                        help='Winding length in mm (only for --reverse)')
    parser.add_argument('-r', '--reverse', dest='reverse', action='store_true',
                        help='Reverse calculation: calculate inductance of a given coil. Requires -c, -t, -l.')
    args = parser.parse_args()

    if args.carcass_diameter == 0:
        parser.print_help()
        sys.exit(1)

    if args.reverse:
        print("Input:")
        print("    Carcass diameter:                 %.06f mm" % (args.carcass_diameter))
        print("    Number of turns:                  %.06f" % (args.turns))
        print("    Winding length:                   %.06f mm" % (args.length))
        L = calc_inductance(args.turns, args.carcass_diameter, args.length);
        print("Output:")
        print("    Inducatance:                      %.06f uH" % (L))
    else:
        print("Input:")
        print("    Carcass diameter:                 %.06f mm" % (args.carcass_diameter))
        print("    Wire diameter without insulation: %.06f mm" % (args.diameter1))
        print("    Wire diameter with insulation:    %.06f mm" % (args.diameter2))
        print("    Target inductance:                %.06f uH" % (args.inductance))
        w, l = calc_turns_and_length(args.inductance, args.carcass_diameter, args.diameter1, args.diameter2)
        print("Output:")
        print("    Number of turns:                  %.06f" % (w))
        print("    Winding length:                   %.06f mm" % (l))
