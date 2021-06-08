# f(n)=n%10 + f(n//10)
def sumOFditgits(n):
     assert int(n)==n,"INTEGERS ONLY !!"
     if n<=0:
          n=-n
     
     if n==0:
          return 0   
     return n%10 + sumOFditgits(n//10)

print(sumOFditgits(123456789))



