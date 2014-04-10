#Project Euler
#Problem 6

sums = 0
sq = 0
total = 0

for x in range(1,101):
    sums = x**2 + sums

for y in range(1,101):
    sq = sq + y

total = sq**2 - sums
print(total)
