#Project Euler Problem #2

#Fibonacci Function
num = 0
num2 = 1
total = 0
while num2 < 4000000:
    num2 = num + num2
    num = num2 - num
    if num2%2 == 0 and num2 < 4000000:
        total = total + num2
print("Total: " + str(total))
