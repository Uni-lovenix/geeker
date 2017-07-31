#! /usr/bin/env python
"""
*******************************************************************
This program using to solve function:
squ(a)*cube(b) - ab[2squ(c)+1+(a-1)squ(1+b)*squ(0.35)]+squ(c) = 0
You need put value a and c 
*******************************************************************
"""
from decimal import *

def varname(p):
	for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
		m = re.search(r'\bvarname\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
		if m:
			return m.group(1)

def solve(a, b,c):
	variable = Decimal(0.1225)
	v1 = (c*c) + (b*b*b)*(a*a - variable*a*a+ 0.35*a) + a*a*(2*b - 2*b*b)*variable
	result = v1 / ((2*c*c*a) + a + variable*a*a - variable*a)
	return result

def B(a, c):
	b = 4.00000
	while b < 7.00000:
		result = solve(a, b, c)
		if abs(b-result) <= 0.00001:
			print 'b = %f'
		b += 0.0000001

def start():
	while True:
		a = raw_input('Input value a:').strip()
		c = raw_input('Input value c:').strip()
		try:
			a = Decimal(a)
			c = float()
		except (ValueError):
			print 'a or c not a number.Please enter again.'
			continue
		break

	print '%#s = %f\n%#s = %f' % ('a', a, 'c', c)
	B(a,c)

if __name__ == '__main__':
	start()