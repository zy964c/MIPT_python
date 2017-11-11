import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

x_one = ((-1*b + math.sqrt((b*b) - (4*a*c)))/(2*a))
x_two = ((-1*b - math.sqrt((b*b) - (4*a*c)))/(2*a))

print(int(x_two))
print(int(x_one))
