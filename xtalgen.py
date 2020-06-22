#!/usr/bin/env python3

import sys
from math import pi, sqrt

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " frequency[hz] [Q=7000]")
    sys.exit(1)

Cp = 4/1000/1000/1000/1000 # max - 10 pF
Cs = Cp/100 # Cs >> Cp
freq = int(sys.argv[1])
Q = 7000 # no less than 5000
if len(sys.argv) >= 3:
    Q = int(sys.argv[2])

# series resonant frequency
# Fs = 1/(2*pi*sqrt(Ls*Cs))
Ls = pow(1/(2*pi*freq), 2)/Cs
# parallel resonant frequency
Fp = 1/(2*pi*sqrt((Ls*Cs*Cp)/(Cs+Cp)))
Rs = (2*pi*freq*Ls)/Q

print("Cp = {:.4f} pF".format(Cp*1000*1000*1000*1000))
print("Cs = {:.4f} pF".format(Cs*1000*1000*1000*1000))
print("Ls = {:.4f} mH".format(Ls*1000))
print("Rs = {:.4f} Ohm".format(Rs))
print("Fp = {:.4f}".format(Fp))
