#Problem 4
#Largest Palindrome

strg = None
v = []

for x in range(100,999,1):
    for y in range(100,999,1):
        z = x * y
        strg = str(z)
        if strg == strg[::-1]:
            print("Palindrome Found.\n")
            v.append(z)

print("The largest Palindrome is:")
print(max(v))
