import math

n = eval( input() )
s = eval( input() )

area = ( n * s**2)/(4*math.tan(math.pi/n))

print("Area = {:.4f}".format(area))
