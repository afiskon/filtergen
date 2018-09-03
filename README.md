# Butterworth Filter Generator

Usage:

```
usage: filtergen.py [-h] [-f FREQUENCY] [-f1 FREQUENCY1] [-f2 FREQUENCY2]
                    [-p {1,2,3,4,5,6,7}] [-i IMPEDANCE]
                    [-t {low-pass,high-pass,band-pass,band-stop}]

Calculate component values for a passive Butterworth filters

optional arguments:
  -h, --help            show this help message and exit
  -f FREQUENCY, --frequency FREQUENCY
                        Frequency for low-pass or high-pass filter in Hz
                        (default: 0)
  -f1 FREQUENCY1, --frequency1 FREQUENCY1
                        First -3 dB frequency for band-pass or band-stop
                        filter in Hz (default: 0)
  -f2 FREQUENCY2, --frequency2 FREQUENCY2
                        Second -3 dB frequency for band-pass or band-stop
                        filter in Hz (default: 0)
  -p {1,2,3,4,5,6,7}, --poles {1,2,3,4,5,6,7}
                        Number of poles (default: 3)
  -i IMPEDANCE, --impedance IMPEDANCE
                        Source and load impedance in Ohm (default: 50)
  -t {low-pass,high-pass,band-pass,band-stop}, --type {low-pass,high-pass,band-pass,band-stop}
                        Type of filter (default: None)
```

Example:

```
./filtergen.py -f1 10000000 -f2 11000000 -p 3 -t band-pass

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

C1 = 3.18 nF, in parallel with 72.34 nH
C3 = 3.18 nF, in parallel with 72.34 nH
L2 = 15.92 uH, in series with 14.47 pF
```

Also includes **coil calculator**:

```
usage: coilcalc.py [-h] [-i INDUCTANCE] [-c CARCASS_DIAMETER] [-d1 DIAMETER1]
                   [-d2 DIAMETER2] [-t TURNS] [-l LENGTH] [-r]

Calculate number of turns and winding length for a given coil inductance, or
do a reverse calculation

optional arguments:
  -h, --help            show this help message and exit
  -i INDUCTANCE, --inductance INDUCTANCE
                        Target inductance in uH (default: 0)
  -c CARCASS_DIAMETER, --carcass-diameter CARCASS_DIAMETER
                        Carcass diameter in mm (default: 0)
  -d1 DIAMETER1, --diameter1 DIAMETER1
                        Wire diameter without insulation in mm (default: 0)
  -d2 DIAMETER2, --diameter2 DIAMETER2
                        Wire diameter with insulation in mm (default: 0)
  -t TURNS, --turns TURNS
                        Number of turns (only for --reverse) (default: 0)
  -l LENGTH, --length LENGTH
                        Winding length in mm (only for --reverse) (default: 0)
  -r, --reverse         Reverse calculation: calculate inductance of a given
                        coil. Requires -c, -t, -l. (default: False)
```
