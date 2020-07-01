#!/usr/bin/env python3
# based on https://leleivre.com/rf_lcmatch.html
# see also https://en.wikipedia.org/wiki/Antenna_tuner#Types_of_L-networks_and_their_uses

import argparse
from math import pi, sqrt

def div(a, b):
    if b == 0:
        return float('Inf')
    else:
        return a / b

def LP(rs,xs,rl,xl,f):
    w = 2*pi*f
    qs = div(-xs, rs)
    ql = div(xl, rl)
    rp = rs*(1+qs*qs)
    c1 = div(div(qs, rp), w)
    l1 = div(xl, w)
    if rl>rp:
        return (None, None)
    Q = sqrt(div(rp, rl)-1)
    cp = div(div(Q, rp), w)
    c = (cp-c1)
    ls = div(Q*rl, w)
    l = (ls-l1)
    return (c, l)

def HP(rs,xs,rl,xl,f):
    w = 2*pi*f
    ql = div(-xl, rl)
    qs = div(xs, rs)
    c1 = div(div(-1, w), xl)
    l1 = div(div(div((1+qs*qs)*xs, w), qs), qs)
    rp = (1+qs*qs)*rs
    rs = rl
    if rs>rp:
        return (None, None)
    Q = sqrt(div(rp, rs)-1)
    lp = div(div(rp, w), Q)
    cs = div(div(div(1, Q), w), rs)
    c = cs if xl == 0 else div(c1*cs, c1-cs)
    l = lp if xs == 0 else div(lp*l1, l1-lp)
    return (c, l)

parser = argparse.ArgumentParser(
    description='LC-match calculator'
    )
parser.add_argument(
    '-rs', type=float, required=True,
    help='Source resistance')
parser.add_argument(
    '-xs', type=float, required=True,
    help='Source reactance')
parser.add_argument(
    '-rl', type=float, required=True,
    help='Load resistance')
parser.add_argument(
    '-xl', type=float, required=True,
    help='Load reactance')
parser.add_argument(
    '-f', type=float, required=True,
    help="Frequency, MHh")
args = parser.parse_args()

def frmt(x, unit):
    if x is None:
        return None
    suffix = ""
    suffixes = ["m", "u", "n", "p"]
    for i in range(0, len(suffixes)):
        if x >= 1:
            break
        x *= 1000
        suffix = suffixes[i]
    return "{:.3f} {}{}".format(x, suffix, unit)

rs = args.rs
xs = args.xs
rl = args.rl
xl = args.xl
f = args.f * 1000_000

(c, l) = LP(rl, xl, rs, xs, f)
if c is not None and c >= 0 and l >= 0:
    print("""
+---CCCC---+---+
|    L     |   |
Zs      C ---  Zl
|         ---  |
|          |   |
V          V   V
L = {}, C = {}""".format(frmt(l, "H"), frmt(c, "F")))

(c, l) = LP(rs, xs, rl, xl, f)
if c is not None and c >= 0 and l >= 0:
    print("""
+------+--CCCC-+
|      |   L   |
Zs  C ---      Zl
|     ---      |
|      |       |
V      V       V
L = {}, C = {}""".format(frmt(l, "H"), frmt(c, "F")))

(c, l) = HP(rl, xl, rs, xs, f)
if c is not None and c >= 0 and l >= 0:
    print("""
 C ||
+--||-----+----+
|  ||     |    |
Zs        C    Zl
|       L C    |
|         C    |
|         |    |
V         V    V
L = {}, C = {}""".format(frmt(l, "H"), frmt(c, "F")))

(c, l) = HP(rs, xs, rl, xl, f)
if c is not None and c >= 0 and l >= 0:
    print("""
         C || 
+----+-----||--+
|    |     ||  |
Zs   C         Zl
|  L C         |
|    C         |
|    |         |
V    V         V
L = {}, C = {}""".format(frmt(l, "H"), frmt(c, "F")))
