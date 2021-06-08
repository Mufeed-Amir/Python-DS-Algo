class Solution:
    
     def gcd(self,a,b):
          if a==0:
               return b
          if b==0:
               return a
          return self.gcd(b,a%b)
     def lcm(self,a,b):
          k=(a*b)//(self.gcd(a,b))
          return k
     def lcmAndgcd(self,a,b):
          g=self.gcd(a,b)
          l=self.lcm(a,b)
          return g,l

num=Solution()
r=num.lcmAndgcd(77,88)
print(r)