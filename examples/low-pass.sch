EESchema Schematic File Version 4
LIBS:filter-examples-cache
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 2 7
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
L pspice:0 #GND02
U 1 1 5B8946D1
P 2250 1850
F 0 "#GND02" H 2250 1750 50  0001 C CNN
F 1 "0" H 2250 1937 50  0000 C CNN
F 2 "" H 2250 1850 50  0001 C CNN
F 3 "" H 2250 1850 50  0001 C CNN
	1    2250 1850
	1    0    0    -1  
$EndComp
$Comp
L pspice:VSOURCE V1
U 1 1 5B8947F6
P 1150 1400
F 0 "V1" H 1378 1446 50  0000 L CNN
F 1 "dc 0 ac 1" H 1378 1355 50  0000 L CNN
F 2 "" H 1150 1400 50  0001 C CNN
F 3 "" H 1150 1400 50  0001 C CNN
	1    1150 1400
	1    0    0    -1  
$EndComp
$Comp
L pspice:C C1
U 1 1 5B8948C3
P 2250 1350
F 0 "C1" H 2428 1396 50  0000 L CNN
F 1 "300p" H 2428 1305 50  0000 L CNN
F 2 "" H 2250 1350 50  0001 C CNN
F 3 "" H 2250 1350 50  0001 C CNN
	1    2250 1350
	1    0    0    -1  
$EndComp
$Comp
L pspice:INDUCTOR L1
U 1 1 5B894985
P 2750 1050
F 0 "L1" H 2750 1265 50  0000 C CNN
F 1 "1.6u" H 2750 1174 50  0000 C CNN
F 2 "" H 2750 1050 50  0001 C CNN
F 3 "" H 2750 1050 50  0001 C CNN
	1    2750 1050
	1    0    0    -1  
$EndComp
$Comp
L pspice:C C2
U 1 1 5B8949B6
P 3300 1350
F 0 "C2" H 3478 1396 50  0000 L CNN
F 1 "300p" H 3478 1305 50  0000 L CNN
F 2 "" H 3300 1350 50  0001 C CNN
F 3 "" H 3300 1350 50  0001 C CNN
	1    3300 1350
	1    0    0    -1  
$EndComp
$Comp
L pspice:R R2
U 1 1 5B894B98
P 3850 1350
F 0 "R2" H 3782 1304 50  0000 R CNN
F 1 "50" H 3782 1395 50  0000 R CNN
F 2 "" H 3850 1350 50  0001 C CNN
F 3 "" H 3850 1350 50  0001 C CNN
	1    3850 1350
	-1   0    0    1   
$EndComp
$Comp
L pspice:0 #GND04
U 1 1 5B894C25
P 3850 1850
F 0 "#GND04" H 3850 1750 50  0001 C CNN
F 1 "0" H 3850 1937 50  0000 C CNN
F 2 "" H 3850 1850 50  0001 C CNN
F 3 "" H 3850 1850 50  0001 C CNN
	1    3850 1850
	1    0    0    -1  
$EndComp
$Comp
L pspice:0 #GND01
U 1 1 5B894C3C
P 1150 1850
F 0 "#GND01" H 1150 1750 50  0001 C CNN
F 1 "0" H 1150 1937 50  0000 C CNN
F 2 "" H 1150 1850 50  0001 C CNN
F 3 "" H 1150 1850 50  0001 C CNN
	1    1150 1850
	1    0    0    -1  
$EndComp
$Comp
L pspice:0 #GND03
U 1 1 5B894C53
P 3300 1850
F 0 "#GND03" H 3300 1750 50  0001 C CNN
F 1 "0" H 3300 1937 50  0000 C CNN
F 2 "" H 3300 1850 50  0001 C CNN
F 3 "" H 3300 1850 50  0001 C CNN
	1    3300 1850
	1    0    0    -1  
$EndComp
Wire Wire Line
	1150 1100 1150 1050
Wire Wire Line
	2500 1050 2250 1050
Wire Wire Line
	2250 1050 2250 1100
Connection ~ 2250 1050
Wire Wire Line
	2250 1600 2250 1850
Wire Wire Line
	1150 1850 1150 1700
Wire Wire Line
	3000 1050 3300 1050
Wire Wire Line
	3850 1050 3850 1100
Wire Wire Line
	3300 1600 3300 1850
Wire Wire Line
	3850 1850 3850 1600
Wire Wire Line
	3300 1100 3300 1050
Connection ~ 3300 1050
Wire Wire Line
	3300 1050 3850 1050
Text GLabel 4050 1050 2    50   Output ~ 0
LP_OUT
Wire Wire Line
	1150 1050 1400 1050
$Comp
L pspice:R R1
U 1 1 5B894A82
P 1650 1050
F 0 "R1" V 1445 1050 50  0000 C CNN
F 1 "50" V 1536 1050 50  0000 C CNN
F 2 "" H 1650 1050 50  0001 C CNN
F 3 "" H 1650 1050 50  0001 C CNN
	1    1650 1050
	0    1    1    0   
$EndComp
Wire Wire Line
	1900 1050 2250 1050
Wire Wire Line
	3850 1050 4050 1050
Connection ~ 3850 1050
$EndSCHEMATC
