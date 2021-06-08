from typing import *
class Solution:
     def decimalTobinary(self,n):
          k=0
          i=0
          while n>0:
               r=n%2
               n=n//2
               k=k+r*(10**i)
               i=i+1
          return str(k)
     def addBinary(self, a: str, b: str) -> str:
          a1=len(a)
          b1=len(b)
          i=0
          k=0
          while i<a1:
               k=k+2**(a1-i-1) * int(a[i])
               i=i+1
          i=0
          k1=0
          while i<b1:
               k1=k1+2**(b1-i-1) * int(b[i])
               i=i+1
          s=k+k1
          m=self.decimalTobinary(s)
          return m

     def addBinary2(self, a: str, b:str) -> str:
          arr=[]
          i,j=len(a)-1,len(b)-1
          carry=0
          while i>=0 or j>=0 or carry:
               total=carry
               if i>=0:
                    total +=int(a[i])
                    i=i-1
               if j>=0:
                    total +=int(b[j])
                    j=j-1
          
               arr.append(f'{total%2}')
               carry=total//2
          
          arr.reverse()
          return arr


     def AddBinary(self, a: str, b:str) -> str:
          la=len(a)
          lb=len(b)
          if la<lb:
               c=a
               a=b
               b=c
          arr=[]
          carry=0
          for i in range(1,lb+1):
               if int(a[-i])+int(b[-i]) == 2:
                    carry=1
                    arr.append('0')
               elif int(a[-i])+int(b[-i])  + carry == 2:
                    carry=1
                    arr.append("0")
               elif int(a[-i])+int(b[-i])  + carry == 1:
                    arr.append("1")
                    carry=0

          if carry==0:
               for i in range(lb+1,la+1):
                    arr.append(a[-i])
          else:
               for i in range(lb+1,la+1):
                    if int(a[-i])+carry==2:
                         arr.append('0')
                         carry=1
                    elif int(a[-i]) + carry==1:
                         arr.append('1')
                         carry=0
          if carry==1:
               arr.append('1')
          arr.reverse()
          k="".join(arr)
          return k
          


elisha=Solution()
print(elisha.addBinary2("1111","1"))