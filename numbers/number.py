from decimal import *
# prevent using Decimal with floats 
getcontext().traps[FloatOperation] = True
a = Decimal('0.8')
b = Decimal('0.7')
c = a - b
print(c)
getcontext().prec = 6
d = Decimal('1.2345678') + 1
print(d)

from fractions import Fraction
two_thrirds = Fraction(2,3)
four_fifths = Fraction(4,5)
print(two_thrirds + four_fifths)
print(two_thrirds * four_fifths)
print(two_thrirds / four_fifths)
print(four_fifths - two_thrirds)
bin(100)

from datetime import *
start = date(2019, 9, 13)
end   = date.today()
end.strftime('%A %d %B %Y')
print(end-start)

a = datetime(year=2019, month=5, day=8, hour=14, minute=22)
b = datetime(year=2019, month=3, day=14, hour=12, minute=9)
print(a-b)

pst = timezone(timedelta(hours=-8), "PST")
departure= datetime(year=2019, month=11, day=9, hour=23, minute=30, tzinfo=pst)
arrival = datetime(year=2019, month=11, day=10, hour=18, minute=15, tzinfo=timezone.utc)
flight_duration = arrival - departure
print(flight_duration)

def sign():
	return (x > 0) - (x < 0)

def orientation(p, q, r):
	p = (Fraction(p[0]), Fraction(p[1]))
	q = (Fraction(q[0]), Fraction(q[1]))
	r = (Fraction(r[0]), Fraction(r[1]))

	# take cross product of vector pq and pr 
	# | 1  px py | 1 px
	# | 1  qx qy | 1 qx
	# | 1  rx ry | 1 rx

	d = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1])*(r[0] - p[0])
	return sign(d)