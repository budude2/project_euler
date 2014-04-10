#Project Euler Problem #1

v1 = 1
v2 = 1
v3 = 1
sum = 0
temp1 = 0
temp2 = 0
temp3 = 0
num = 1000

while temp1 < num:  # All multiples of 3
    temp1 = 3 * v1
    if temp1 < num and temp1%5 > 0:
        sum = sum + temp1
    v1 += 1

while temp2 < num:  #All multiples of 5
    temp2 = 5 * v2
    if temp2 < num and temp2%3 > 0:
        sum = sum + temp2
    v2 += 1

while temp3 < num:  #All multiples of 3 and 5
    temp3 = 5 * v3
    if temp3 < num and temp3%3 == 0 and temp3%5 == 0:
        sum = sum + temp3
    v3 += 1

print(sum)
