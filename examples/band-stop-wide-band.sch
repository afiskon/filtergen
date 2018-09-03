EESchema Schematic File Version 4
LIBS:filter-examples-cache
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 6 7
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L pspice:VSOURCE V?
U 1 1 5B898506
P 1300 1650
AR Path="/5B8944E1/5B898506" Ref="V?"  Part="1" 
AR Path="/5B8944F3/5B898506" Ref="V?"  Part="1" 
AR Path="/5B89451A/5B898506" Ref="V5"  Part="1" 
F 0 "V5" H 1528 1696 50  0000 L CNN
F 1 "dc 0 ac 1" H 1528 1605 50  0000 L CNN
F 2 "" H 1300 1650 50  0001 C CNN
F 3 "" H 1300 1650 50  0001 C CNN
	1    1300 1650
	1    0    0    -1  
$EndComp
$Comp
L pspice:INDUCTOR L?
U 1 1 5B898514
P 3500 850
AR Path="/5B8944E1/5B898514" Ref="L?"  Part="1" 
AR Path="/5B8944F3/5B898514" Ref="L?"  Part="1" 
AR Path="/5B89451A/5B898514" Ref="L9"  Part="1" 
F 0 "L9" H 3500 1065 50  0000 C CNN
F 1 "1.71u" H 3500 974 50  0000 C CNN
F 2 "" H 3500 850 50  0001 C CNN
F 3 "" H 3500 850 50  0001 C CNN
	1    3500 850 
	1    0    0    -1  
$EndComp
$Comp
L pspice:R R?
U 1 1 5B89851B
P 1800 1300
AR Path="/5B8944E1/5B89851B" Ref="R?"  Part="1" 
AR Path="/5B8944F3/5B89851B" Ref="R?"  Part="1" 
AR Path="/5B89451A/5B89851B" Ref="R9"  Part="1" 
F 0 "R9" V 1595 1300 50  0000 C CNN
F 1 "50" V 1686 1300 50  0000 C CNN
F 2 "" H 1800 1300 50  0001 C CNN
F 3 "" H 1800 1300 50  0001 C CNN
	1    1800 1300
	0    1    1    0   
$EndComp
$Comp
L pspice:R R?
U 1 1 5B898522
P 4900 1600
AR Path="/5B8944E1/5B898522" Ref="R?"  Part="1" 
AR Path="/5B8944F3/5B898522" Ref="R?"  Part="1" 
AR Path="/5B89451A/5B898522" Ref="R10"  Part="1" 
F 0 "R10" H 4832 1554 50  0000 R CNN
F 1 "50" H 4832 1645 50  0000 R CNN
F 2 "" H 4900 1600 50  0001 C CNN
F 3 "" H 4900 1600 50  0001 C CNN
	1    4900 1600
	-1   0    0    1   
$EndComp
$Comp
L pspice:0 #GND?
U 1 1 5B898529
P 4900 2100
AR Path="/5B8944E1/5B898529" Ref="#GND?"  Part="1" 
AR Path="/5B8944F3/5B898529" Ref="#GND?"  Part="1" 
AR Path="/5B89451A/5B898529" Ref="#GND024"  Part="1" 
F 0 "#GND024" H 4900 2000 50  0001 C CNN
F 1 "0" H 4900 2187 50  0000 C CNN
F 2 "" H 4900 2100 50  0001 C CNN
F 3 "" H 4900 2100 50  0001 C CNN
	1    4900 2100
	1    0    0    -1  
$EndComp
$Comp
L pspice:0 #GND?
U 1 1 5B89852F
P 1300 2100
AR Path="/5B8944E1/5B89852F" Ref="#GND?"  Part="1" 
AR Path="/5B8944F3/5B89852F" Ref="#GND?"  Part="1" 
AR Path="/5B89451A/5B89852F" Ref="#GND020"  Part="1" 
F 0 "#GND020" H 1300 2000 50  0001 C CNN
F 1 "0" H 1300 2187 50  0000 C CNN
F 2 "" H 1300 2100 50  0001 C CNN
F 3 "" H 1300 2100 50  0001 C CNN
	1    1300 2100
	1    0    0    -1  
$EndComp
Wire Wire Line
	1300 1350 1300 1300
Wire Wire Line
	1300 1300 1550 1300
Wire Wire Line
	1300 2100 1300 1950
Wire Wire Line
	4900 2100 4900 1850
Text GLabel 5100 1300 2    50   Output ~ 0
BSW_OUT
$Comp
L pspice:C C?
U 1 1 5B898545
P 3500 1300
AR Path="/5B8944E1/5B898545" Ref="C?"  Part="1" 
AR Path="/5B8944F3/5B898545" Ref="C?"  Part="1" 
AR Path="/5B89451A/5B898545" Ref="C15"  Part="1" 
F 0 "C15" H 3678 1346 50  0000 L CNN
F 1 "530.5p" H 3678 1255 50  0000 L CNN
F 2 "" H 3500 1300 50  0001 C CNN
F 3 "" H 3500 1300 50  0001 C CNN
	1    3500 1300
	0    -1   -1   0   
$EndComp
Wire Wire Line
	4900 1300 4900 1350
$Comp
L pspice:INDUCTOR L?
U 1 1 5B89854F
P 3950 1600
AR Path="/5B8944E1/5B89854F" Ref="L?"  Part="1" 
AR Path="/5B8944F3/5B89854F" Ref="L?"  Part="1" 
AR Path="/5B89451A/5B89854F" Ref="L10"  Part="1" 
F 0 "L10" H 3950 1815 50  0000 C CNN
F 1 "2.65u" H 3950 1724 50  0000 C CNN
F 2 "" H 3950 1600 50  0001 C CNN
F 3 "" H 3950 1600 50  0001 C CNN
	1    3950 1600
	0    1    1    0   
$EndComp
Wire Wire Line
	3750 1300 3850 1300
Wire Wire Line
	3950 1300 3950 1350
Connection ~ 3950 1300
$Comp
L pspice:C C?
U 1 1 5B898568
P 3950 2200
AR Path="/5B8944E1/5B898568" Ref="C?"  Part="1" 
AR Path="/5B8944F3/5B898568" Ref="C?"  Part="1" 
AR Path="/5B89451A/5B898568" Ref="C14"  Part="1" 
F 0 "C14" H 4128 2246 50  0000 L CNN
F 1 "341p" H 4128 2155 50  0000 L CNN
F 2 "" H 3950 2200 50  0001 C CNN
F 3 "" H 3950 2200 50  0001 C CNN
	1    3950 2200
	1    0    0    -1  
$EndComp
$Comp
L pspice:0 #GND?
U 1 1 5B89856F
P 3950 2650
AR Path="/5B8944E1/5B89856F" Ref="#GND?"  Part="1" 
AR Path="/5B8944F3/5B89856F" Ref="#GND?"  Part="1" 
AR Path="/5B89451A/5B89856F" Ref="#GND021"  Part="1" 
F 0 "#GND021" H 3950 2550 50  0001 C CNN
F 1 "0" H 3950 2737 50  0000 C CNN
F 2 "" H 3950 2650 50  0001 C CNN
F 3 "" H 3950 2650 50  0001 C CNN
	1    3950 2650
	1    0    0    -1  
$EndComp
$Comp
L pspice:INDUCTOR L?
U 1 1 5B898BF6
P 2900 1600
AR Path="/5B8944E1/5B898BF6" Ref="L?"  Part="1" 
AR Path="/5B8944F3/5B898BF6" Ref="L?"  Part="1" 
AR Path="/5B89451A/5B898BF6" Ref="L11"  Part="1" 
F 0 "L11" H 2900 1815 50  0000 C CNN
F 1 "2.65u" H 2900 1724 50  0000 C CNN
F 2 "" H 2900 1600 50  0001 C CNN
F 3 "" H 2900 1600 50  0001 C CNN
	1    2900 1600
	0    1    1    0   
$EndComp
$Comp
L pspice:C C?
U 1 1 5B898C5C
P 2900 2200
AR Path="/5B8944E1/5B898C5C" Ref="C?"  Part="1" 
AR Path="/5B8944F3/5B898C5C" Ref="C?"  Part="1" 
AR Path="/5B89451A/5B898C5C" Ref="C13"  Part="1" 
F 0 "C13" H 3078 2246 50  0000 L CNN
F 1 "341p" H 3078 2155 50  0000 L CNN
F 2 "" H 2900 2200 50  0001 C CNN
F 3 "" H 2900 2200 50  0001 C CNN
	1    2900 2200
	1    0    0    -1  
$EndComp
$Comp
L pspice:0 #GND?
U 1 1 5B898CEB
P 2900 2650
AR Path="/5B8944E1/5B898CEB" Ref="#GND?"  Part="1" 
AR Path="/5B8944F3/5B898CEB" Ref="#GND?"  Part="1" 
AR Path="/5B89451A/5B898CEB" Ref="#GND022"  Part="1" 
F 0 "#GND022" H 2900 2550 50  0001 C CNN
F 1 "0" H 2900 2737 50  0000 C CNN
F 2 "" H 2900 2650 50  0001 C CNN
F 3 "" H 2900 2650 50  0001 C CNN
	1    2900 2650
	1    0    0    -1  
$EndComp
Wire Wire Line
	3950 1300 4900 1300
Wire Wire Line
	3750 850  3850 850 
Wire Wire Line
	3850 850  3850 1300
Wire Wire Line
	3850 1300 3950 1300
Connection ~ 3850 1300
Wire Wire Line
	3250 850  3150 850 
Wire Wire Line
	3150 850  3150 1300
Wire Wire Line
	3150 1300 3250 1300
Connection ~ 3150 1300
Wire Wire Line
	2900 1300 2900 1350
Wire Wire Line
	2900 1300 3150 1300
Connection ~ 2900 1300
Wire Wire Line
	2900 1850 2900 1950
Wire Wire Line
	2900 2450 2900 2650
Wire Wire Line
	3950 2650 3950 2450
Wire Wire Line
	3950 1950 3950 1850
Wire Wire Line
	2050 1300 2900 1300
Wire Wire Line
	4900 1300 5100 1300
Connection ~ 4900 1300
$EndSCHEMATC
