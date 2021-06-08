def gcd(a,b):
     if a==0:
          return b
     if b==0:
          return a
     return gcd(b,a%b)
def lcm(a,b):
     k=(a*b)//gcd(a,b)
     return k
def addFraction(num1, den1, num2, den2):
     den=den1 * den2
     num=num1*den2 + num2*den1
     k=gcd(num,den)
     # m=f"{num//k}/{den//k}"
     m=str(num//k) + "/"+ str(den//k)
     return m

h=addFraction(3,4,1,4)
print(h)


