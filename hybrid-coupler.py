#!/usr/bin/env python3

import sys
from math import pi

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " frequency[hz] [Z=50]")
    sys.exit(1)

F = int(sys.argv[1])
Z = 50
if len(sys.argv) >= 3:
    Z = int(sys.argv[2])

L = Z / (2*pi*F)
C = 1 / (4*pi*F*Z)

print("""
             L1
IN   ---+---CCCC---+--- OUT1
        |          |
    C1 ---     C2 ---
       ---        ---
        |          |
OUT2 ---+---CCCC---+--- DUMP
             L2

L1 = L2 = L
C1 = C2 = C
""")

print("C = {:.4f} pF".format(C*1000*1000*1000*1000))
print("L = {:.4f} uH".format(L*1000*1000))
