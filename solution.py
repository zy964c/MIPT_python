import sys

sum = 0
digit_string = sys.argv[1]
for i in digit_string:
    sum += int(i)
print(sum)
    
