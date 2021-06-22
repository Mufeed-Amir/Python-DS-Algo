class Solution:
     def isPerfectNumber(self, n):
          arr=[]
          for i in range(1,(n+2)//2):
               if n%i==0:
                    arr.append(i)

          s=sum(arr)

          if n==s:
               return 1
          else:
               return 0



num=Solution()
m=num.isPerfectNumber(8)
print(m)