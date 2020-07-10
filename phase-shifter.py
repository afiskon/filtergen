#!/usr/bin/env python3
# based on https://www.microwaves101.com/encyclopedias/high-pass-low-pass-phase-shifters

import sys
from math import pi,sin,cos

if len(sys.argv) < 3:
    print("Usage: " + sys.argv[0] + " frequency[hz] angle [Z=50]")
    sys.exit(1)

F = int(sys.argv[1])
w = 2*pi*F
a = int(sys.argv[2])*pi/180
Z = 50
if len(sys.argv) >= 4:
    Z = int(sys.argv[2])

print("""
High pass tee:

   C1       C2
   ||       ||
---||---+---||---
   ||   |   ||
        C
        C L1
        C
        |
        V
""")
L = Z / (w*sin(a))
C = sin(a)/(w*Z*(1-cos(a)))
print("C1 = C2 = {:.4f} pF".format(C*1000*1000*1000*1000))
print("L1 = {:.4f} uH".format(L*1000*1000))


print("""
Low pass tee:

    L1         L2
---CCCC---+---CCCC---
          |
        -----
        ----- C1
          |
          V
""")
L = Z*(1-cos(a))/(w*sin(a))
C = sin(a)/(w*Z)
print("L1 = L2 = {:.4f} uH".format(L*1000*1000))
print("C1 = {:.4f} pF".format(C*1000*1000*1000*1000))


print("""
High pass pi:

       C1
       ||
---+---||---+---
   |   ||   |
   C        C
   C L1     C L2
   C        C
   |        |
   V        V
""")
C = 1/(w*Z*sin(a))
L = Z*sin(a)/(w*(1-cos(a)))
print("C1 = {:.4f} pF".format(C*1000*1000*1000*1000))
print("L1 = L2 = {:.4f} uH".format(L*1000*1000))

print("""
Low pass pi:

        L1
---+---CCCC---+---
   |          |
 ----- C1   ----- C2
 -----      -----
   |          |
   V          V
""")
C = (1-cos(a))/(w*Z*sin(a))
L = Z*sin(a)/w
print("L1 = {:.4f} uH".format(L*1000*1000))
print("C1 = C2 = {:.4f} pF".format(C*1000*1000*1000*1000))


