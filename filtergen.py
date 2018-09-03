#!/usr/bin/env python3
# vim: set ai et ts=4 sw=4: 

# Butterworth Filter Generator v 0.1
# (c) Aleksander Alekseev 2018
# https://eax.me/

# The algorithm is based on Chapter 9 of Practical Electronics for Inventors,
# 4th Edition by Paul Scherz and Simon Monk

# Here we use PI configuration assumming that load impedance matches source
# impedance. It's better to use T configuration if the load impedance is
# greater than the source impedance.

import math
import sys
import argparse
from typing import Any
from dataclasses import dataclass
from enum import Enum, unique

@unique
class FilterType(Enum):
    LOW_PASS = 'low-pass'
    HIGH_PASS = 'high-pass'
    BAND_PASS = 'band-pass'
    BAND_STOP = 'band-stop'

    def __str__(self):
        return self.value

@unique
class FilterSubtype(Enum):
    REGULAR = 'regular'
    WIDE_BAND = 'wide-band'
    NARROW_BAND = 'narrow-band'

    def __str__(self):
        return self.value

@dataclass
class Filter:
    filter_type: FilterType
    data: Any
    filter_subtype: FilterSubtype = FilterSubtype.REGULAR

# For other values see:
# * https://web.stanford.edu/class/ee133/handouts/labs/EE133filterCookbook.pdf
# * http://files.vlsi.uwindsor.ca/88-521/pdf/chapter3.pdf
butterworth_values = {
  1: { "C" : [2.0], "L": [] },
  2: { "C" : [1.4142], "L": [1.4142] },
  3: { "C" : [1.0, 1.0], "L": [2.0] },
  4: { "C" : [0.7654, 1.8478], "L": [1.8478, 0.7654] },
  5: { "C" : [0.6180, 2.0000, 0.6180], "L": [1.6180, 1.6180] },
  6: { "C" : [0.5176, 1.9319, 1.4142], "L": [1.4142, 1.9319, 0.5176] },
  7: { "C" : [0.4450, 1.8019, 1.8019, 0.4450], "L": [1.2470, 2.0000, 1.2470] }
}

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

def low_pass_filter_schematic():
    return """
Low-pass filter:

           L2
=> ---+--CCCCC--+--- ...etc...
      |         |
    -----     -----
    ----- C1  ----- C3
      |         |
     GND       GND
"""

def high_pass_filter_schematic():
    return """
High-pass filter:

      C1       C3
      | |      | |
=> ---| |--+---| |--- ...etc...
      | |  |   | |
           C
           C L2
           C
           |
          GND
"""

def band_pass_narrow_band_filter_schematic():
    return """
Band-pass narrow-band filter:

              L2     | |
=> --+----+--CCCCC---| |---+----+--- ...etc...
     |    |          | |   |    |
     |    |                |    |
   -----  C              -----  C
C1 -----  C           C3 -----  C
     |    C                |    C
     |    |                |    |
    GND  GND              GND  GND
"""

def band_stop_narrow_band_filter_schematic():
    return """
Band-stop narrow-band filter:

        +--CCCCC--+
        |         |
        |   | |   |
=> ---+-+---| |---+-+--- ...etc...
      |     | |     |
      C     C2      C
   L1 C          L3 C
      C             C
      |             |
    -----         -----
    -----         -----
      |             |
     GND           GND
"""

def print_filter(Filt, show_schematic = False):
    Dat = Filt.data

    # band-pass and band-stop filters may consist
    # of multiple filters
    if type(Dat) is list:
        print("%s %s filter consists of two parts." % (str(Filt.filter_type).capitalize(), Filt.filter_subtype))
        i = 1
        for F in Dat:
            print_filter(F, show_schematic)
            i += 1
        return

    if show_schematic:
        if Filt.filter_type == FilterType.LOW_PASS:
            print(low_pass_filter_schematic())
        elif Filt.filter_type == FilterType.HIGH_PASS:
            print(high_pass_filter_schematic())
        elif Filt.filter_type == FilterType.BAND_PASS: # since type(Dat) != list it's a narrow-band filter
            print(band_pass_narrow_band_filter_schematic())
        else: # BAND_STOP, narrow-band filter
            print(band_stop_narrow_band_filter_schematic())

    Cs, Ls = Dat[0], Dat[1]

    start_i = 1
    if Filt.filter_type == FilterType.BAND_STOP and Filt.filter_subtype == FilterSubtype.NARROW_BAND:
        start_i = 2 # band stop narrow band filters have different schematic
    i, j = start_i, 0
    for C in Cs:
        (C, unit) = scale(C)
        if len(Dat) == 4:
            L = Dat[3][j]
            (L, unitL) = scale(L)
            j += 1
            print("C%d = %.2f %sF, in parallel with %.2f %sH" % (i, C, unit, L, unitL))
        else:
            print("C%d = %.2f %sF" % (i, C, unit))
        i += 2 

    start_i = 2
    if Filt.filter_type == FilterType.BAND_STOP and Filt.filter_subtype == FilterSubtype.NARROW_BAND:
        start_i = 1 # band stop narrow band filters have different schematic
    i, j = start_i, 0
    for L in Ls:
        (L, unit) = scale(L)
        if len(Dat) == 4:
            C = Dat[2][j]
            (C, unitC) = scale(C)
            j += 1
            print("L%d = %.2f %sH, in series with %.2f %sF" % (i, L, unit, C, unitC))
        else:
            print("L%d = %.2f %sH" % (i, L, unit))
        i += 2

def calc_filter_internal(freq_3db, number_of_poles, high_pass = False, alt_schematic = False, Rl = 50):
    if number_of_poles < min(butterworth_values.keys()) or number_of_poles > max(butterworth_values.keys()):
        raise ValueError("Invalid number_of_poles: %d" % (number_of_poles))

    Cs = butterworth_values[number_of_poles]["C"]
    Ls = butterworth_values[number_of_poles]["L"]

    if high_pass:
        Cs = [ 1 / C for C in Cs ]
        Ls = [ 1 / L for L in Ls ]

    if alt_schematic:
        Cs, Ls = Ls, Cs

    Cs = [ C / (2*math.pi*freq_3db*Rl) for C in Cs]
    Ls = [ (Rl * L) / (2*math.pi*freq_3db) for L in Ls]
    return (Cs, Ls)


def calc_low_pass_filter(freq_3db, number_of_poles, Rl = 50):
    return Filter(
        filter_type = FilterType.LOW_PASS,
        data = calc_filter_internal(freq_3db, number_of_poles, Rl = Rl)
    )

def calc_high_pass_filter(freq_3db, number_of_poles, Rl = 50):
    return Filter(
        filter_type = FilterType.HIGH_PASS,
        data = calc_filter_internal(freq_3db, number_of_poles, high_pass = True, Rl = Rl)
    )

def calc_band_pass_filter(freq1, freq2, number_of_poles, pass_band_scale_factor = 2.0, Rl = 50):
    if freq2 <= freq1:
        raise ValueError("freq2 (%d) supposed to be larger than freq1 (%d)" % (freq2, freq1))

    if freq2/freq1 > 1.5: # wide-band
        HighPass = calc_high_pass_filter(freq1, number_of_poles, Rl)
        LowPass = calc_low_pass_filter(freq2, number_of_poles, Rl)
        return Filter(filter_type = FilterType.BAND_PASS, filter_subtype = FilterSubtype.WIDE_BAND, data = [LowPass, HighPass])
    else: # narrow-band
        center_freq = math.sqrt(freq1*freq2)
        delta = (freq2 - freq1) * pass_band_scale_factor;
        freq_a = center_freq - delta/2;
        freq_b = center_freq + delta/2;
        stop_band_bandwidth_a = math.pow(center_freq, 2) / freq_a - freq_a
        stop_band_bandwidth_b = freq_b - math.pow(center_freq, 2) / freq_b
        stop_band_bandwidth = min(stop_band_bandwidth_a, stop_band_bandwidth_b)
        (Cs, Ls) = calc_filter_internal(freq2 - freq1, number_of_poles, Rl = Rl)
        # C series with Ls
        C2s = [ 1 / (math.pow((2*math.pi*center_freq), 2)*L) for L in Ls ]
        # Ls parallel with Cs
        L2s = [ 1 / (math.pow((2*math.pi*center_freq), 2)*C) for C in Cs ]
        return Filter(filter_type = FilterType.BAND_PASS, filter_subtype = FilterSubtype.NARROW_BAND, data = (Cs, Ls, C2s, L2s))

def calc_band_stop_filter(freq1, freq2, number_of_poles, stop_band_scale_factor = 2.0, Rl = 50):
    if freq2 <= freq1:
        raise ValueError("freq2 (%d) supposed to be larger than freq1 (%d)" % (freq2, freq1))

    if False: # freq2/freq1 > 1.5: # such filters will not work, checked with SPICE simulation
        HighPass = calc_high_pass_filter(freq2, number_of_poles, Rl)
        LowPass = calc_low_pass_filter(freq1, number_of_poles, Rl)
        return Filter(filter_type = FilterType.BAND_STOP, filter_subtype = FilterSubtype.WIDE_BAND, data = [LowPass, HighPass])
    else: # narrow-band
        center_freq = math.sqrt(freq1*freq2)
        delta = (freq2 - freq1) * stop_band_scale_factor;
        freq_a = center_freq - delta/2;
        freq_b = center_freq + delta/2;
        stop_band_bandwidth_a = math.pow(center_freq, 2) / freq_a - freq_a
        stop_band_bandwidth_b = freq_b - math.pow(center_freq, 2) / freq_b
        stop_band_bandwidth = min(stop_band_bandwidth_a, stop_band_bandwidth_b)
        (Cs, Ls) = calc_filter_internal(freq2 - freq1, number_of_poles, high_pass = True, alt_schematic = True, Rl = Rl)
        # C series with Ls
        C2s = [ 1 / (math.pow((2*math.pi*center_freq), 2)*L) for L in Ls ]
        # Ls parallel with Cs
        L2s = [ 1 / (math.pow((2*math.pi*center_freq), 2)*C) for C in Cs ]
        return Filter(filter_type = FilterType.BAND_STOP, filter_subtype = FilterSubtype.NARROW_BAND, data = (Cs, Ls, C2s, L2s))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = 'Calculate component values for a passive Butterworth filters',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-f', '--frequency', type=float, default=0,
                        help='Frequency for low-pass or high-pass filter in Hz')
    parser.add_argument('-f1', '--frequency1', type=float, default=0,
                        help='First -3 dB frequency for band-pass or band-stop filter in Hz')
    parser.add_argument('-f2', '--frequency2', type=float, default=0,
                        help='Second -3 dB frequency for band-pass or band-stop filter in Hz')
    parser.add_argument('-p', '--poles', type=int, default=3,
                        choices=range(min(butterworth_values.keys()), max(butterworth_values.keys())+1),
                        help='Number of poles')
    parser.add_argument('-i', '--impedance', type=float, default=50,
                        help='Source and load impedance in Ohm')
    parser.add_argument('-t', '--type', type=FilterType, choices=list(FilterType),
                        help='Type of filter')
    parser.add_argument('-c', '--check', dest='check', action='store_true',
                        help=argparse.SUPPRESS)
    args = parser.parse_args()

    if args.check:
        print("RUNNING CHECK (-c or --check option was privided)")
        print("=================================================")
        # Here we can check that results match expected values from the book.
        print_filter(calc_low_pass_filter(3000, 3))
        # Figure 9.9: C[1] = 1.06 uF, L[2] = 5.31 mH, C[3] = 1.06 uF

        print_filter(calc_high_pass_filter(1000, 5))
        # Figure 9.10: C[1] = 5.1 uF, C[3] = 1.6 uF, C[5] = 5.1 uF
        #              L[2] = 4.9 mH, L[4] = 4.9 mH

        print_filter(calc_band_pass_filter(1000, 1501, 4))
        # There is no such filter in the book. We only have to check that
        # a pair of filters was returned: one low-pass and one high-pass

        print_filter(calc_band_pass_filter(900, 1100, 3))
        # Figure 9.12:
        # C[1] = 15.92 uF, in parallel with 1.61 mH
        # C[3] = 15.92 uF, in parallel with 1.61 mH
        # L[2] = 79.6 mH, in series with 320 nF

        print_filter(calc_band_stop_filter(800, 1200, 3))
        # There is no such filter in the book, however the result was
        # checked using SPICE simulator.
        # C[2] = 3.98 uF, in parallel with 6.63 mH
        # L[1] = 19.89 mH, in series with 1.33 uF
        # L[3] = 19.89 mH, in series with 1.33 uF
        sys.exit(0)

    if args.frequency == 0 and args.frequency1 == 0 and args.frequency2 == 0:
        parser.print_help()
        sys.exit(1)

    if args.type == FilterType.LOW_PASS:
        Filt = calc_low_pass_filter(args.frequency, args.poles, Rl = args.impedance)
    elif args.type == FilterType.HIGH_PASS:
        Filt = calc_high_pass_filter(args.frequency, args.poles, Rl = args.impedance)
    elif args.type == FilterType.BAND_PASS:
        Filt = calc_band_pass_filter(args.frequency1, args.frequency2, args.poles, Rl = args.impedance)
    else: # BAND_STOP
        Filt = calc_band_stop_filter(args.frequency1, args.frequency2, args.poles, Rl = args.impedance)

    print_filter(Filt, True)
