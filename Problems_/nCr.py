class Solution:
    def f(self,a):
        if a==0 or a==1:
            return 1
        return a*(self.f(a-1))
    
    def nCr(self,n, r):
        if r>n:
            return 0
        m=self.f(n)//(self.f(n-r)*self.f(r))
        return m%1000000007

num=Solution()
print(num.nCr(13,2))
