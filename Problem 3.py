#Project Euler Problem #3
#Prime Factor

num = int(input("Number:\n"))
r = []

#Calculate prime factors
while num != 1:
    md = 1
    x = 2
    while md != 0:
        md = num%x
        x = x+1
    r.append(x-1)
    num = num / (x-1)
print(r)
