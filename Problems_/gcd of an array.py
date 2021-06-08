class Solution:
     def gcd(self,n,arr):
          arr.sort()
          c=arr[0]
          m=1
          for i in range(2,c+1):
               for j in range(0,n):
                    if arr[j]%i==0:
                         m=m*i
                    print(m)
                   
          return m

arr=[4,8,6,12,16]
num=Solution()
k=num.gcd(5,arr)