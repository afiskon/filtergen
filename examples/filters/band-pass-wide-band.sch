EESchema Schematic File Version 4
LIBS:filter-examples-cache
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 4 7
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
U 1 1 5B89536B
P 1300 1550
AR Path="/5B8944E1/5B89536B" Ref="V?"  Part="1" 
AR Path="/5B8944F3/5B89536B" Ref="V3"  Part="1" 
F 0 "V3" H 1528 1596 50  0000 L CNN
F 1 "dc 0 ac 1" H 1528 1505 50  0000 L CNN
F 2 "" H 1300 1550 50  0001 C CNN
F 3 "" H 1300 1550 50  0001 C CNN
	1    1300 1550
	1    0    0    -1  
$EndComp
$Comp
L pspice:C C?
U 1 1 5B895372
P 2450 1550
AR Path="/5B8944E1/5B895372" Ref="C?"  Part="1" 
AR Path="/5B8944F3/5B895372" Ref="C6"  Part="1" 
F 0 "C6" H 2628 1596 50  0000 L CNN
F 1 "454p" H 2628 1505 50  0000 L CNN
F 2 "" H 2450 1550 50  0001 C CNN
F 3 "" H 2450 1550 50  0001 C CNN
	1    2450 1550
	1    0    0    -1  
$EndComp
$Comp
L pspice:INDUCTOR L?
U 1 1 5B895379
P 2750 1200
AR Path="/5B8944E1/5B895379" Ref="L?"  Part="1" 
AR Path="/5B8944F3/5B895379" Ref="L4"  Part="1" 
F 0 "L4" H 2750 1415 50  0000 C CNN
F 1 "2.3u" H 2750 1324 50  0000 C CNN
F 2 "" H 2750 1200 50  0001 C CNN
F 3 "" H 2750 1200 50  0001 C CNN
	1    2750 1200
	1    0    0    -1  
$EndComp
$Comp
L pspice:R R?
U 1 1 5B895380
P 1800 1200
AR Path="/5B8944E1/5B895380" Ref="R?"  Part="1" 
AR Path="/5B8944F3/5B895380" Ref="R5"  Part="1" 
F 0 "R5" V 1595 1200 50  0000 C CNN
F 1 "50" V 1686 1200 50  0000 C CNN
F 2 "" H 1800 1200 50  0001 C CNN
F 3 "" H 1800 1200 50  0001 C CNN
	1    1800 1200
	0    1    1    0   
$EndComp
$Comp
L pspice:R R?
U 1 1 5B895387
P 4900 1500
AR Path="/5B8944E1/5B895387" Ref="R?"  Part="1" 
AR Path="/5B8944F3/5B895387" Ref="R6"  Part="1" 
F 0 "R6" H 4832 1454 50  0000 R CNN
F 1 "50" H 4832 1545 50  0000 R CNN
F 2 "" H 4900 1500 50  0001 C CNN
F 3 "" H 4900 1500 50  0001 C CNN
	1    4900 1500
	-1   0    0    1   
$EndComp
$Comp
L pspice:0 #GND?
U 1 1 5B89538E
P 4900 2000
AR Path="/5B8944E1/5B89538E" Ref="#GND?"  Part="1" 
AR Path="/5B8944F3/5B89538E" Ref="#GND013"  Part="1" 
F 0 "#GND013" H 4900 1900 50  0001 C CNN
F 1 "0" H 4900 2087 50  0000 C CNN
F 2 "" H 4900 2000 50  0001 C CNN
F 3 "" H 4900 2000 50  0001 C CNN
	1    4900 2000
	1    0    0    -1  
$EndComp
$Comp
L pspice:0 #GND?
U 1 1 5B895394
P 1300 2000
AR Path="/5B8944E1/5B895394" Ref="#GND?"  Part="1" 
AR Path="/5B8944F3/5B895394" Ref="#GND09"  Part="1" 
F 0 "#GND09" H 1300 1900 50  0001 C CNN
F 1 "0" H 1300 2087 50  0000 C CNN
F 2 "" H 1300 2000 50  0001 C CNN
F 3 "" H 1300 2000 50  0001 C CNN
	1    1300 2000
	1    0    0    -1  
$EndComp
$Comp
L pspice:0 #GND?
U 1 1 5B89539A
P 3100 2000
AR Path="/5B8944E1/5B89539A" Ref="#GND?"  Part="1" 
AR Path="/5B8944F3/5B89539A" Ref="#GND011"  Part="1" 
F 0 "#GND011" H 3100 1900 50  0001 C CNN
F 1 "0" H 3100 2087 50  0000 C CNN
F 2 "" H 3100 2000 50  0001 C CNN
F 3 "" H 3100 2000 50  0001 C CNN
	1    3100 2000
	1    0    0    -1  
$EndComp
Wire Wire Line
	1300 1250 1300 1200
Wire Wire Line
	1300 1200 1550 1200
Wire Wire Line
	1300 2000 1300 1850
Wire Wire Line
	4900 2000 4900 1750
Text GLabel 5100 1200 2    50   Output ~ 0
BPW_OUT
$Comp
L pspice:C C?
U 1 1 5B8953AE
P 3500 1200
AR Path="/5B8944E1/5B8953AE" Ref="C?"  Part="1" 
AR Path="/5B8944F3/5B8953AE" Ref="C8"  Part="1" 
F 0 "C8" H 3678 1246 50  0000 L CNN
F 1 "796p" H 3678 1155 50  0000 L CNN
F 2 "" H 3500 1200 50  0001 C CNN
F 3 "" H 3500 1200 50  0001 C CNN
	1    3500 1200
	0    -1   -1   0   
$EndComp
Wire Wire Line
	4650 1200 4900 1200
Wire Wire Line
	4900 1200 4900 1250
$Comp
L pspice:INDUCTOR L?
U 1 1 5B8953BA
P 3950 1500
AR Path="/5B8944E1/5B8953BA" Ref="L?"  Part="1" 
AR Path="/5B8944F3/5B8953BA" Ref="L5"  Part="1" 
F 0 "L5" H 3950 1715 50  0000 C CNN
F 1 "995n" H 3950 1624 50  0000 C CNN
F 2 "" H 3950 1500 50  0001 C CNN
F 3 "" H 3950 1500 50  0001 C CNN
	1    3950 1500
	0    1    1    0   
$EndComp
$Comp
L pspice:0 #GND?
U 1 1 5B8953C1
P 3950 2000
AR Path="/5B8944E1/5B8953C1" Ref="#GND?"  Part="1" 
AR Path="/5B8944F3/5B8953C1" Ref="#GND012"  Part="1" 
F 0 "#GND012" H 3950 1900 50  0001 C CNN
F 1 "0" H 3950 2087 50  0000 C CNN
F 2 "" H 3950 2000 50  0001 C CNN
F 3 "" H 3950 2000 50  0001 C CNN
	1    3950 2000
	1    0    0    -1  
$EndComp
Wire Wire Line
	3950 1750 3950 2000
$Comp
L pspice:C C?
U 1 1 5B8953C8
P 4400 1200
AR Path="/5B8944E1/5B8953C8" Ref="C?"  Part="1" 
AR Path="/5B8944F3/5B8953C8" Ref="C9"  Part="1" 
F 0 "C9" H 4578 1246 50  0000 L CNN
F 1 "796p" H 4578 1155 50  0000 L CNN
F 2 "" H 4400 1200 50  0001 C CNN
F 3 "" H 4400 1200 50  0001 C CNN
	1    4400 1200
	0    -1   -1   0   
$EndComp
Wire Wire Line
	3750 1200 3950 1200
Wire Wire Line
	3950 1200 3950 1250
Connection ~ 3950 1200
Wire Wire Line
	3950 1200 4150 1200
$Comp
L pspice:C C?
U 1 1 5B895992
P 3100 1550
AR Path="/5B8944E1/5B895992" Ref="C?"  Part="1" 
AR Path="/5B8944F3/5B895992" Ref="C7"  Part="1" 
F 0 "C7" H 3278 1596 50  0000 L CNN
F 1 "454p" H 3278 1505 50  0000 L CNN
F 2 "" H 3100 1550 50  0001 C CNN
F 3 "" H 3100 1550 50  0001 C CNN
	1    3100 1550
	1    0    0    -1  
$EndComp
$Comp
L pspice:0 #GND?
U 1 1 5B8959ED
P 2450 2000
AR Path="/5B8944E1/5B8959ED" Ref="#GND?"  Part="1" 
AR Path="/5B8944F3/5B8959ED" Ref="#GND010"  Part="1" 
F 0 "#GND010" H 2450 1900 50  0001 C CNN
F 1 "0" H 2450 2087 50  0000 C CNN
F 2 "" H 2450 2000 50  0001 C CNN
F 3 "" H 2450 2000 50  0001 C CNN
	1    2450 2000
	1    0    0    -1  
$EndComp
Wire Wire Line
	3000 1200 3100 1200
Wire Wire Line
	2450 1200 2450 1300
Connection ~ 2450 1200
Wire Wire Line
	2450 1200 2500 1200
Wire Wire Line
	3100 1200 3100 1300
Connection ~ 3100 1200
Wire Wire Line
	3100 1200 3250 1200
Wire Wire Line
	2450 1800 2450 2000
Wire Wire Line
	3100 2000 3100 1800
Wire Wire Line
	5100 1200 4900 1200
Connection ~ 4900 1200
Wire Wire Line
	2050 1200 2450 1200
$EndSCHEMATC
