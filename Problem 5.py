#Project Euler
#Problem #5

n1 = 20
n2 = n1 - 1
gcdv = None
lcmv = None

while (n2 != 1):
    def gcd(a,b):
        r = None
        while (r != 0):
            r = a%b
            a = b #a will be the GCD at the end
            b = r
        return a

    def lcm(a,b,c):
        result = (a * b)/c
        return result

    gcdv = gcd(n1,n2)
    n1 = lcm(n1, n2, gcdv)
    n2 -= 1
print(n1)
