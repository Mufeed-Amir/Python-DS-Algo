def maxSlidingWindow(nums,k):
     n=len(nums)
     if k>n:
          return -1
     elif k==n:
          return [max(nums)]
     a=[]
     for i in range(0,n-k+1):
          m=max([nums[i] for i in range(i,k+i)])
          a.append(m)

     return a
          



print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))



     