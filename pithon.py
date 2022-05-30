import math
from decimal import *

getcontext().prec = 100

pi = 0
nosides = 6
sidelngth = 1
perimeter = 6
diameter = 2

while nosides < 1000000000000000000000000000000000000:
	sidelngth2 = Decimal(sidelngth) / Decimal(2)
	radius_a = Decimal(((1**2)-(sidelngth/2)**2)).sqrt()
	radius_b = Decimal(1) - Decimal(radius_a)
	sidelngthnew = Decimal((radius_b**2)+(sidelngth2**2)).sqrt()
	polycircum = Decimal(nosides * sidelngth)
	pi = polycircum / diameter
	sidelngth = sidelngthnew
	nosides = nosides * 2
	print('π:', format(pi, '1'))




