class Solution:
     t=1000000007
     def f(self,n):
          if n==1:
               return 0
          if n==2:
               return 1
          return (self.f(n-1)%self.t + self.f(n-2)%self.t)%self.t

     def nthEvenFibonacci (self,n):
          k=3*n+1
          return self.f(k)%self.t

num=Solution()
print(num.nthEvenFibonacci(10))