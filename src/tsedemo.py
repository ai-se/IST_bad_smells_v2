#http://unbox.org/stuff/var/timm/12/left/rc/
import sys; sys.dont_write_bytecode=True
from rfun import *
from bag  import Bag

print "\nDemo1: finds three ranks: neural-net: g-measure"

rc([Bag("orig",[38,	57,	45,	37,	43,	20,	39,	14,	41, 18]),
    Bag("m",[32, 19,	57,	20,	39,	33,	38,	15,	44,	28]),
    Bag("m10",[59,	60,	65,	45,	56,	46,	58,	35,	58,	52]),
    Bag("m20",[56,	60,	59,	49,	63,	47,	69,	35,	57,	47]),
    Bag("m40",[62,	63,	52,	53,	51,	63,	68,	37,	62,	45]),
    Bag("s10",[38,	43,	52,	33,	29,	0,	44,	9,	35,	13]),
    Bag("s20",[51,	42,	51,	18,	48,	20,	42,	13,	35,	26]),
    Bag("s40",[44,	47,	58,	19,	20,	20,	46,	15,	39,	13]),
    Bag("k2",[32,	68,	44,	42,	67,	20,	41,	19,	36,	18]),
    Bag("k4",[0,	0,	0,	7,	14,	0,	3,	5,	13,	16]) ])



print "\nDemo1: finds three ranks: svm: g-measure"

rc([Bag("orig",[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    Bag("m",[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    Bag("m10",[62, 67, 70, 54, 40, 68, 60, 43, 66, 46]),
    Bag("m20",[75, 59, 71, 25, 50, 48, 73, 27, 61, 48]),
    Bag("m40",[75, 56, 67, 30, 55, 35, 65, 18, 62, 42]),
    Bag("s10",[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    Bag("s20",[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    Bag("s40",[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    Bag("k2",[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    Bag("k4",[0, 0, 0, 0, 0, 0, 5, 0, 24, 0]) ])
    
    
    
print "\nDemo1: finds three ranks: nb: g-measure"

rc([Bag("orig",[26,	36,	62,	24,	14,	0,	69,	11,	60,	34]),
    Bag("m",[26,	31,	62,	23,	14,	0,	67,	10,	60,	34]),
    Bag("m10",[42,	59,	51,	52,	20,	70,	54,	31,	41,	40]),
    Bag("m20",[59,	64,	59,	61,	34,	72,	64,	35,	51,	42]),
    Bag("m40",[68,	66,	62,	64,	54,	70,	71,	44,	55,	44]),
    Bag("s10",[26,	36,	62,	24,	7,	0,	67,	10,	58,	30]),
    Bag("s20",[26,	31,	47,	17,	14,	0,	62,	10,	56,	31]),
    Bag("s40",[18,	36,	47,	16,	0,	0,	63,	9,	58,	30]),
    Bag("k2",[18,	31,	55,	20,	20,	0,	52,	9,	58,	31]),
    Bag("k4",[18,	31,	55,	19,	14,	0,	48,	9,	54,	29]) ])
    


print "\nDemo1: finds three ranks: neural-net: pd"

rc([Bag("orig",[25,	44,	31,	23,	30,	11,	26,	7,	27,	10]),
		Bag("m",[20,	11,	46,	11,	26,	22,	25,	8,	30,	17]),
		Bag("m10",[70,	59,	69,	31,	74,	44,	52,	34,	64,	56]),
		Bag("m20",[65,	59,	62,	36,	78,	44,	73,	37,	59,	35]),
		Bag("m40",[65,	74,	46,	40,	70,	56,	68,	29,	65,	32]),
		Bag("s10",[25,	30,	38,	21,	19,	0,	30,	5,	22,	7]),
		Bag("s20",[35,	30,	38,	10,	33,	11,	29,	7,	22,	15]),
		Bag("s40",[30,	33,	46,	11,	11,	11,	32,	8,	25,	7]),
		Bag("k2",[20,	59,	31,	29,	59,	11,	29,	11,	23,	10]),
		Bag("k4",[0,	0,	0,	4,	7,	0,	1,	3,	7,	8]) ])



print "\nDemo1: finds three ranks: svm: pd"

rc([Bag("orig",[0,	0,	0,	0,	0,	0,	0,	0,	0,	0]),
		Bag("m",[0,	0,	0,	0,	0,	0,	0,	0,	0,	0]),
		Bag("m10",[90,	70,	85,	41,	63,	67,	90,	44,	70,	45]),
		Bag("m20",[70,	44,	62,	14,	59,	33,	65,	16,	56,	39]),
		Bag("m40",[70,	41,	54,	18,	56,	22,	51,	10,	63,	28]),
		Bag("s10",[0,	0,	0,	0,	0,	0,	0,	0,	0,	0]),
		Bag("s20",[0,	0,	0,	0,	0,	0,	0,	0,	0,	0]),
		Bag("s40",[0,	0,	0,	0,	0,	0,	0,	0,	0,	0]),
		Bag("k2",[0,	0,	0,	0,	0,	0,	0,	0,	0,	0]),
		Bag("k4",[0,	0,	0,	0,	0,	0,	3,	0,	14,	0]) ])



print "\nDemo1: finds three ranks: nb: pd"

rc([Bag("orig",[15,	22,	46,	13,	7,	0,	57,	6,	49,	21]),
		Bag("m",[15,	19,	46,	13,	7,	0,	55,	5,	48,	21]),
		Bag("m10",[95,	81,	92,	84,	96,	89,	92,	64,	92,	51]),
		Bag("m20",[85,	67,	77,	78,	89,	89,	88,	41,	89,	42]),
		Bag("m40",[90,	59,	62,	54,	78,	78,	81,	35,	88,	34]),
		Bag("s10",[15,	22,	46,	13,	4,	0,	55,	5,	47,	18]),
		Bag("s20",[15,	19,	31,	9,	7,	0,	48,	5,	44,	18]),
		Bag("s40",[10,	22,	31,	9,	0,	0,	48,	5,	45,	18]),
		Bag("k2",[10,	19,	38,	11,	11,	0,	36,	5,	47,	18]),
		Bag("k4",[10,	19,	38,	11,	7,	0,	32,	5,	42,	17]) ])



print "\nDemo1: finds three ranks: neural-net: pf"

rc([Bag("orig",[17,	22,	19,	16,	23,	19,	20,	4,	17,	9]),
		Bag("m",[18,	22,	25,	16,	23,	36,	20,	12,	20,	11]),
		Bag("m10",[50,	40,	38,	20,	54,	53,	34,	63,	46,	51]),
		Bag("m20",[51,	40,	43,	25,	48,	50,	34,	67,	46,	31]),
		Bag("m40",[41,	45,	41,	25,	60,	28,	31,	47,	41,	24]),
		Bag("s10",[20,	20,	22,	10,	38,	14,	20,	20,	13,	11]),
		Bag("s20",[7,	26,	24,	9,	17,	11,	18,	4,	13,	11]),
		Bag("s40",[15,	20,	21,	8,	17,	8,	19,	10,	17,	11]),
		Bag("k2",[20,	20,	24,	23,	24,	11,	25,	14,	18,	14]),
		Bag("k4",[7,	7,	6,	6,	1,	0,	8,	0,	11,	6]) ])
		
		
		
print "\nDemo1: finds three ranks: svm: pf"

rc([Bag("orig",[0,	0,	0,	0,	0,	0,	0,	0,	0,	0]),
		Bag("m",[0,	0,	0,	0,	0,	0,	0,	0,	0,	0]),
		Bag("m10",[52,	36,	41,	20,	70,	31,	54,	57,	37,	52]),
		Bag("m20",[20,	14,	16,	2,	56,	14,	16,	16,	34,	38]),
		Bag("m40",[18,	9,	13,	4,	46,	14,	9,	10,	38,	14]),
		Bag("s10",[0,	0,	0,	0,	0,	0,	0,	0,	0,	0]),
		Bag("s20",[0,	0,	0,	0,	0,	0,	0,	0,	0,	0]),
		Bag("s40",[0,	0,	0,	0,	0,	0,	0,	0,	0,	0]),
		Bag("k2",[0,	0,	0,	0,	0,	0,	0,	0,	0,	0]),
		Bag("k4",[0,	0,	0,	0,	0,	0,	0,	0,	2,	0]) ])
		
		
		
print "\nDemo1: finds three ranks: nb: pf"

rc([Bag("orig",[5,	5,	5,	4,	7,	8,	12,	12,	24,	9]),
		Bag("m",[7,	5,	5,	4,	5,	8,	12,	12,	22,	9]),
		Bag("m10",[73,	54,	64,	63,	89,	42,	62,	80,	74,	67]),
		Bag("m20",[55,	38,	52,	50,	79,	39,	50,	69,	64,	59]),
		Bag("m40",[46,	26,	38,	22,	59,	36,	36,	41,	60,	36]),
		Bag("s10",[5,	5,	3,	4,	7,	8,	12,	8,	23,	9]),
		Bag("s20",[5,	5,	4,	3,	7,	3,	11,	8,	22,	8]),
		Bag("s40",[5,	5,	4,	3,	3,	3,	10,	8,	20,	10]),
		Bag("k2",[7,	5,	4,	4,	7,	3,	9,	10,	24,	7]),
		Bag("k4",[7,	5,	4,	4,	6,	3,	8,	10,	23,	7]) ])
